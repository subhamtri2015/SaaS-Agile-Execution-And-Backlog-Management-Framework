#!/usr/bin/env python3
"""
fetch_github.py
Fetches real public GitHub data (issues, milestones, releases) from metabase/metabase.

Features:
- Pure Python standard library (urllib, json, csv)
- Supports personal access token (GITHUB_TOKEN env or --token arg)
- Dual issue fetching modes:
    1) Standard repo issues endpoint (/repos/metabase/metabase/issues)
    2) Direct issue search (/search/issues?q=repo:metabase/metabase+is:issue) to get 100% pure issues
- Caches raw JSON safely in data/raw/ (gitignored)
- Normalizes and outputs aggregated CSVs to data/processed/ (committed)
"""

import os
import sys
import json
import time
import csv
import argparse
import urllib.request
import urllib.error
import urllib.parse
from datetime import datetime, timezone, timedelta
from pathlib import Path

REPO_OWNER = "metabase"
REPO_NAME = "metabase"
API_BASE = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}"

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"


def get_headers(token=None):
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "ProductOps-Audit-Script",
    }
    auth_token = token or os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if auth_token:
        headers["Authorization"] = f"Bearer {auth_token}"
    return headers


def check_rate_limit(token=None):
    url = "https://api.github.com/rate_limit"
    req = urllib.request.Request(url, headers=get_headers(token))
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            core = data.get("resources", {}).get("core", {})
            search = data.get("resources", {}).get("search", {})
            print(f"[Rate Limit] Core remaining: {core.get('remaining')}/{core.get('limit')} | Search remaining: {search.get('remaining')}/{search.get('limit')}")
            return core.get("remaining")
    except Exception as e:
        print(f"[Rate Limit Warning] Could not inspect rate limits: {e}")
        return None


def fetch_url(url, token=None, retries=3):
    headers = get_headers(token)
    req = urllib.request.Request(url, headers=headers)
    for attempt in range(1, retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                rate_remaining = resp.headers.get("X-RateLimit-Remaining")
                if rate_remaining and int(rate_remaining) <= 2:
                    print(f"Warning: Low rate limit remaining ({rate_remaining}). Pausing...")
                content = resp.read().decode()
                return json.loads(content)
        except urllib.error.HTTPError as e:
            if e.code == 403:
                print(f"[HTTP 403] Rate limit exceeded or access denied for {url}")
                raise
            print(f"[Attempt {attempt}/{retries}] HTTP error for {url}: {e.code} {e.reason}")
            if attempt == retries:
                raise
            time.sleep(2 * attempt)
        except Exception as e:
            print(f"[Attempt {attempt}/{retries}] Network error: {e}")
            if attempt == retries:
                raise
            time.sleep(2 * attempt)


def fetch_milestones(token=None, max_pages=3):
    print("\n--- Fetching Milestones ---")
    milestones = []
    page = 1
    while page <= max_pages:
        url = f"{API_BASE}/milestones?state=all&per_page=100&page={page}"
        print(f"Fetching milestones page {page}...")
        data = fetch_url(url, token)
        if not data:
            break
        milestones.extend(data)
        if len(data) < 100:
            break
        page += 1
        time.sleep(0.5)

    print(f"Fetched {len(milestones)} milestones.")
    with open(RAW_DIR / "milestones_raw.json", "w", encoding="utf-8") as f:
        json.dump(milestones, f, indent=2)

    # Normalize to CSV
    csv_path = PROCESSED_DIR / "milestones.csv"
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "number", "title", "state", "open_issues", "closed_issues", "created_at", "updated_at", "due_on", "closed_at"])
        for m in milestones:
            writer.writerow([
                m.get("id"),
                m.get("number"),
                m.get("title"),
                m.get("state"),
                m.get("open_issues", 0),
                m.get("closed_issues", 0),
                m.get("created_at"),
                m.get("updated_at"),
                m.get("due_on"),
                m.get("closed_at")
            ])
    print(f"Exported processed milestones to {csv_path}")
    return milestones


def fetch_releases(token=None, max_pages=3):
    print("\n--- Fetching Releases ---")
    releases = []
    page = 1
    while page <= max_pages:
        url = f"{API_BASE}/releases?per_page=100&page={page}"
        print(f"Fetching releases page {page}...")
        data = fetch_url(url, token)
        if not data:
            break
        releases.extend(data)
        if len(data) < 100:
            break
        page += 1
        time.sleep(0.5)

    print(f"Fetched {len(releases)} releases.")
    with open(RAW_DIR / "releases_raw.json", "w", encoding="utf-8") as f:
        json.dump(releases, f, indent=2)

    # Normalize to CSV
    csv_path = PROCESSED_DIR / "releases.csv"
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "tag_name", "name", "draft", "prerelease", "created_at", "published_at", "body_length", "author_login"])
        for r in releases:
            body = r.get("body") or ""
            writer.writerow([
                r.get("id"),
                r.get("tag_name"),
                r.get("name"),
                r.get("draft"),
                r.get("prerelease"),
                r.get("created_at"),
                r.get("published_at"),
                len(body),
                (r.get("author") or {}).get("login", "")
            ])
    print(f"Exported processed releases to {csv_path}")
    return releases


def extract_priority(labels):
    for l in labels:
        name = l["name"] if isinstance(l, dict) else l
        if "Priority:P" in name:
            return name.split("Priority:")[1].strip()
    return "Unassigned"


def extract_type(labels):
    for l in labels:
        name = l["name"] if isinstance(l, dict) else l
        if "Type:" in name:
            return name.split("Type:")[1].strip()
    return "Unassigned"


def fetch_issues_search(token=None, max_pages=5):
    print(f"\n--- Fetching Issues via Search API (Max {max_pages} pages) ---")
    issues = []
    page = 1
    query = "repo:metabase/metabase is:issue"
    encoded_query = urllib.parse.quote(query)

    while page <= max_pages:
        url = f"https://api.github.com/search/issues?q={encoded_query}&sort=created&order=desc&per_page=100&page={page}"
        print(f"Fetching search issues page {page}...")
        data = fetch_url(url, token)
        items = data.get("items", []) if data else []
        if not items:
            break
        issues.extend(items)
        if len(items) < 100:
            break
        page += 1
        time.sleep(2)  # Respect search rate limit

    print(f"Fetched {len(issues)} pure issues via search.")
    with open(RAW_DIR / "issues_raw.json", "w", encoding="utf-8") as f:
        json.dump(issues, f, indent=2)

    export_issues_csv(issues)
    return issues


def fetch_issues_standard(token=None, max_pages=10, months_back=18):
    print(f"\n--- Fetching Issues via Standard Endpoint (Max {max_pages} pages) ---")
    cutoff_date = datetime.now(timezone.utc) - timedelta(days=months_back * 30.5)
    issues = []
    page = 1

    while page <= max_pages:
        url = f"{API_BASE}/issues?state=all&sort=created&direction=desc&per_page=100&page={page}"
        print(f"Fetching issues page {page}...")
        data = fetch_url(url, token)
        if not data:
            break

        reached_cutoff = False
        for item in data:
            if "pull_request" in item:
                continue
            created_at = datetime.fromisoformat(item["created_at"].replace("Z", "+00:00"))
            if created_at < cutoff_date:
                reached_cutoff = True
                break
            issues.append(item)

        if reached_cutoff or len(data) < 100:
            break
        page += 1
        time.sleep(0.5)

    print(f"Fetched {len(issues)} pure issues.")
    with open(RAW_DIR / "issues_raw.json", "w", encoding="utf-8") as f:
        json.dump(issues, f, indent=2)

    export_issues_csv(issues)
    return issues


def export_issues_csv(issues):
    csv_path = PROCESSED_DIR / "issues.csv"
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "number", "state", "title", "created_at", "closed_at",
            "comments_count", "reactions_count", "priority", "type",
            "needs_triage", "milestone_title", "labels_csv"
        ])
        for it in issues:
            labels = [l["name"] for l in it.get("labels", [])]
            priority = extract_priority(labels)
            issue_type = extract_type(labels)
            needs_triage = 1 if ".Needs Triage" in labels else 0
            reactions_total = (it.get("reactions") or {}).get("total_count", 0)
            ms_title = (it.get("milestone") or {}).get("title", "") if it.get("milestone") else ""
            labels_str = ";".join(labels)

            writer.writerow([
                it.get("number"),
                it.get("state"),
                it.get("title", "").replace("\n", " ").strip(),
                it.get("created_at"),
                it.get("closed_at"),
                it.get("comments", 0),
                reactions_total,
                priority,
                issue_type,
                needs_triage,
                ms_title,
                labels_str
            ])
    print(f"Exported {len(issues)} processed issues to {csv_path}")


def main():
    parser = argparse.ArgumentParser(description="Fetch GitHub data for Metabase Product-Ops Audit")
    parser.add_argument("--token", help="GitHub Personal Access Token (or set GITHUB_TOKEN env var)")
    parser.add_argument("--use-search", action="store_true", help="Use GitHub Search API for issues")
    parser.add_argument("--pages", type=int, default=3, help="Max pages of issues to pull (100 per page)")
    parser.add_argument("--months", type=int, default=18, help="Months back to fetch (default: 18)")
    parser.add_argument("--skip-issues", action="store_true", help="Skip issues fetch")
    args = parser.parse_args()

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    print("==================================================")
    print(" Product-Ops Audit: Metabase GitHub Data Ingestion")
    print("==================================================")
    check_rate_limit(args.token)

    fetch_milestones(token=args.token, max_pages=2)
    fetch_releases(token=args.token, max_pages=2)

    if not args.skip_issues:
        if args.use_search:
            fetch_issues_search(token=args.token, max_pages=args.pages)
        else:
            fetch_issues_standard(token=args.token, max_pages=args.pages, months_back=args.months)

    print("\nData fetch and aggregation complete!")


if __name__ == "__main__":
    main()
