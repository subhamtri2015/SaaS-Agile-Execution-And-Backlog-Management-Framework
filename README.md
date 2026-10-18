# From Issue Tracker to Release Notes
### A B2B SaaS Product Operations Audit & Automated Release Governance Pipeline

<p align="center">
  <img src="https://img.shields.io/badge/Data-Real%20GitHub%20API-2ea44f?style=for-the-badge&logo=github"/>
  <img src="https://img.shields.io/badge/Product-Metabase%20BI-509EE3?style=for-the-badge&logo=metabase&logoColor=white"/>
  <img src="https://img.shields.io/badge/Delivery-Simulated%20Agile-orange?style=for-the-badge&logo=scrumalliance"/>
  <img src="https://img.shields.io/badge/Stack-Jira%20%7C%20Confluence%20%7C%20SQL%20%7C%20Python-blue?style=for-the-badge"/>
</p>

---

## 🌟 Executive Overview

![Product Operations Hero Banner](./assets/hero-banner.svg)

This repository presents an end-to-end Product Operations case study and systems architecture built on real engineering telemetry from **Metabase** (`metabase/metabase`), the leading open-source Business Intelligence platform. 

It executes a two-phase operational transformation:
1. **Part A (Empirical Audit):** Quantitative SQL analysis of 200 issues, 200 milestones, and 200 releases to diagnose backlog health, triage latency, release cadence, and customer pain themes.
2. **Part B (Product Response):** The specification and simulated delivery of the **Release Health Assistant (RHA)**—an automated governance platform that resolves triage debt, guarantees milestone-to-changelog parity, and enforces automated Go/No-Go release gates.

---

## 📊 Live Audit KPI Scorecard

![Audit Telemetry Dashboard](./assets/audit-dashboard.svg)

### 📌 Empirical Findings Summary

> **🔍 Backlog Prioritization vs. Triage Latency:**  
> Prioritization coverage is high at **94.7%** (144 / 152 open issues). However, **77.6%** (118 / 152) linger in `.Needs Triage`, proving that **intake triage latency**—not engineering resolution speed—is the core operational bottleneck.
> 
> **⏱️ Resolution Speed by Severity:**  
> Critical P1 crash/security defects are resolved in an average of **4.1 days**, while P2 major functional defects average **9.3 days** (2.3x longer) due to cross-team dependencies across database connectors and visualization layers.
> 
> **🚀 Release Cadence & Milestone Delivery:**  
> The engineering team ships General Availability (GA) releases **every 2.7 days** across active maintenance branches, maintaining **100% milestone completion** at formal release closure.
> 
> **💡 Customer Engagement & Friction Themes:**  
> Top community engagement centers on KPI number card title truncation ([#84334](https://github.com/metabase/metabase/issues/84334)), embedded on-demand query execution ([#83595](https://github.com/metabase/metabase/issues/83595)), and tab URL slug deep-linking ([#84169](https://github.com/metabase/metabase/issues/84169)).

---

## 🛠️ The Product Response: Release Health Assistant (RHA)

To eliminate the 77.6% triage backlog debt and prevent release notes desynchronization during rapid 2.7-day deployment cycles, we engineered the **Release Health Assistant**.

![Release Health Assistant UI Mockup](./assets/rha-interface-mockup.svg)

### Core Capabilities
* **Automated Triage SLA Monitor:** Daily cron scanner identifying issues tagged `.Needs Triage` older than 72 hours, automatically dispatching scoped Slack digests to sub-teams (`.Team/Graphy`, `.Team/QueryProcessor`, `.Team/UXWest`).
* **Milestone-to-Changelog Parity Validator:** Bi-directional validator ensuring 100% of closed milestone issues appear in customer-facing release notes. Reports status directly to GitHub PR Check Runs.
* **Go/No-Go Readiness Portal:** Automated pre-flight gate enforcing zero P1 blockers, 100% test pass rate, changelog parity, and tamper-proof digital sign-offs before production deployment.

---

## 🚀 Agile Execution: Jira Board & Burndown Velocity

The Release Health Assistant was delivered across **3 simulated agile sprints**, achieving **100% predictability** (64 committed story points delivered across 30 engineering days).

![Jira Sprint Delivery Board & Burndown](./assets/jira-board-burndown.svg)

### Velocity Breakdown Across Sprints

| Sprint | Epic / Focus Area | Committed Points | Delivered Points | Predictability | Primary Milestone |
|---|---|---|---|---|---|
| **Sprint 1** | Foundations & Triage Governance | 19 | 19 | **100%** | Scheduled triage scanner, SQLite caching, Slack alerting |
| **Sprint 2** | Release Gate & Changelog Automation | 21 | 21 | **100%** | Markdown notes parser, regex tokenizer, PR status check |
| **Sprint 3** | Readiness Portal, Pilot & Launch | 24 | 24 | **100%** | Interactive Go/No-Go UI, digital sign-off trail, E2E suite |
| **Total** | **Full Platform Delivery** | **64** | **64** | **100%** | **Pilot deployed; triage debt dropped from 77.6% to 14.2%** |

*(Explore full sprint ceremonies, standups, and retrospectives in [`05-sprints-simulated/`](./05-sprints-simulated/))*

---

## 📑 Core Documentation Architecture

### Upstream PRD vs. Downstream Release Documentation

A central principle of this repository is maintaining strict separation between upstream product requirements and downstream release documentation:

| Dimension | Upstream PRD ([`04-requirements/`](./04-requirements/)) | Downstream Release Documentation ([`06-docs/`](./06-docs/)) |
|---|---|---|
| **Lifecycle Phase** | Authored **before** engineering commences | Authored **after** development during release packaging |
| **Core Purpose** | Defines problem statement, user personas, functional specs & Gherkin scenarios | Documents user-facing changes, validates test passes & records Go/No-Go sign-offs |
| **Key Artifacts** | [`PRD-release-health-assistant.md`](./04-requirements/PRD-release-health-assistant.md) · [`jira-ticket-templates.md`](./04-requirements/jira-ticket-templates.md) | [`release-notes.md`](./06-docs/release-notes.md) · [`readiness-checklist.md`](./06-docs/readiness-checklist.md) · [`test-record.md`](./06-docs/test-record.md) |

---

## 🎯 Production Jira Ticket Standard

Every engineering ticket adheres to strict user-story structure with Gherkin acceptance criteria:

```jira
Key: RHA-101 | Component: Ingest-Worker | Priority: P1 | Points: 5
Summary: As a Product Ops Lead, I want a daily scan for '.Needs Triage' issues > 72 hours,
         so that our 77.6% triage backlog debt is systematically cleared.

Acceptance Criteria (Gherkin):
  Scenario 1: Daily scan detects SLA breach
    Given an issue has been open for > 72 hours
    And its label set contains '.Needs Triage'
    When the RHA scan runs at 09:00 UTC
    Then the issue is flagged as 'SLA Breached'
    And a formatted summary is posted to the team's Slack channel (#team-graphy).

  Scenario 2: Issue triaged within SLA
    Given an issue has had its '.Needs Triage' label removed within 48 hours
    When the RHA scan runs
    Then the issue is excluded from the breach escalation digest.
```

---

## 🧠 Strategic Decisions Log

Key engineering and product-ops trade-offs documented during this project:

1. **Target Product Selection:** Chose Metabase over vertical robotics because B2B BI operations universally demonstrate the standard triage → backlog → sprint → release-notes lifecycle with legal, public REST API access.
2. **Issue Fetch Optimization:** Replaced standard `/issues` pagination (which returns 90% pull requests) with direct GitHub Search API queries (`q=repo:metabase/metabase is:issue`) to retrieve 100% pure issues.
3. **Milestone Completion as Velocity Proxy:** Grounded in maintainer comments (issue #10139) confirming that closing an issue into a milestone is how the team determines release note inclusion.
4. **Data Minimization:** Raw JSON responses are cached locally and `.gitignore`d; only normalized, aggregated metrics and CSVs are committed to protect author privacy.
5. **Scope Guardrails:** Deferred autonomous bot PR generation to future roadmap, prioritizing deterministic SLA monitoring and changelog parity verification.

*(Full rationale in [`01-context/decisions-log.md`](./01-context/decisions-log.md))*

---

## 🗺️ Product Roadmap (Now / Next / Later)

![Product Roadmap](./assets/roadmap.svg)

---

## 📁 Repository Directory Structure

```
saas-product-ops-audit/
├── README.md                      # Executive Showcase & Technical Documentation
├── assets/                        # SVG Visualizations & Architecture Diagrams
│   ├── hero-banner.svg            # Executive overview header
│   ├── audit-dashboard.svg        # Live audit telemetry & metric cards
│   ├── rha-interface-mockup.svg   # 3-view Release Health Assistant UI
│   ├── jira-board-burndown.svg    # Sprint board & velocity burndown chart
│   └── roadmap.svg                # Visual 3-horizon product roadmap
├── data/
│   ├── processed/                 # Committed aggregate datasets
│   │   ├── issues.csv             # 200 normalized issues with priority/triage tags
│   │   ├── milestones.csv         # 200 milestone records
│   │   ├── releases.csv           # 200 release records
│   │   └── metrics_summary.json   # Computed metric summary
│   └── raw/                       # Cached raw JSON responses (gitignored)
├── scripts/
│   ├── fetch_github.py            # API ingestion script with rate-limit protection
│   ├── build_metrics.py           # In-memory SQLite analytics engine
│   └── build_metrics.sql          # Pure SQL reference queries
├── 01-context/                    # Scope, methodology, data sources & decisions log
├── 02-audit/                      # Real audit findings (Backlog, Triage, Cadence, Themes)
├── 03-market/                     # Competitor table, user journey & feature gaps
├── 04-requirements/               # PRD, backlog CSV & Jira ticket standards
├── 05-sprints-simulated/          # 3 Sprints, ceremonies, burndown & risk log
├── 06-docs/                       # Release notes, feature library, test record, checklist
└── 07-launch/                     # 5-min demo script, 4-week pilot plan & announcement
```

---

## 💻 Quickstart: Reproducing the Audit

To run the data ingestion and metrics engine locally:

```bash
# 1. Fetch live telemetry from GitHub (milestones, releases, pure issues)
python3 scripts/fetch_github.py --use-search --pages 2

# 2. Compute audit metrics via SQLite engine
python3 scripts/build_metrics.py

# 3. View summary output in data/processed/metrics_summary.json
cat data/processed/metrics_summary.json
```
