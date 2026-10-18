# Scope & Methodology

## 1. Executive Summary & Objective
This repository contains an end-to-end Product Operations Audit and subsequent Product Delivery response for a horizontal B2B SaaS platform. The audit leverages real, public engineering telemetry extracted from **Metabase** (`metabase/metabase`), an industry-leading open-source Business Intelligence platform used globally by enterprise data teams.

The objective is twofold:
1. **Part A (Empirical Audit):** Audit real-world backlog health, triage speed, release readiness, and user feedback themes using quantitative SQL queries against GitHub API records.
2. **Part B (Product Response & Simulated Delivery):** Formulate a comprehensive Product Requirements Document (PRD) for an operational tool called the **"Release Health Assistant (RHA)"**, and simulate its agile execution across 3 structured sprints with Jira boards, burndown metrics, release notes, and launch collateral.

```mermaid
flowchart LR
    A[Real GitHub Data\nmetabase/metabase] --> B[SQL Metrics Engine\nscripts/build_metrics.py]
    B --> C[Audit Findings\n02-audit/]
    C --> D[PRD & Backlog\n04-requirements/]
    D --> E[3 Simulated Sprints\n05-sprints-simulated/]
    E --> F[Release Notes & Checklist\n06-docs/]
    F --> G[Pilot & Demo Launch\n07-launch/]
```

---

## 2. Methodology & Ingestion Workflow

### A. Data Ingestion Architecture
* **Source:** Official GitHub REST API (`v3`).
* **Tooling:** Python 3 standard library script (`scripts/fetch_github.py`) with zero third-party dependencies.
* **Authentication:** Supports `GITHUB_TOKEN` environment variable or `--token` CLI argument, expanding API rate limits from 60 to 5,000 requests/hour.
* **Pagination & Rate Limit Protection:** Inspects `X-RateLimit-Remaining` headers dynamically; applies exponential backoff when API thresholds fall below safety margins.
* **PR Filtering:** GitHub's standard `/issues` endpoint commingles Issues and Pull Requests. A strict key-filter (`if 'pull_request' in item: continue`) ensures only pure user and maintainer issues enter the pipeline.

### B. Analytical Transformation
* Processed records are normalized into three CSV schemas in `data/processed/`:
  1. `issues.csv`: Number, state, title, creation timestamp, close timestamp, priority, type, `.Needs Triage` flag, reactions, comments.
  2. `milestones.csv`: Milestone title, open/closed issues, due dates, closed dates.
  3. `releases.csv`: Release tag, publication date, prerelease flag, changelog byte size.
* The analysis engine (`scripts/build_metrics.py` and `scripts/build_metrics.sql`) instantiates an in-memory SQLite analytical database to execute standard Product Operations queries.

---

## 3. Scope Definition

| Dimension | Included in Scope | Explicitly Excluded |
|---|---|---|
| **Data Timeframe** | Active releases, active milestones, and recent 200 pure issues | Historical git commit logs, code diffs, raw Git blobs |
| **Telemetry Boundaries** | Publicly visible issue metadata, label taxonomy, and release tags | Private Metabase Cloud telemetry, internal Jira/Linear workspaces |
| **Audit Focus** | Backlog hygiene, triage bottlenecks, release cadence, user pain points | Deep-dive code reviews, internal team performance reviews |
| **Part B Execution** | Realistic agile simulation with ceremonies, burndown charts, and PRD | Real-world software deployment to production cloud clusters |
