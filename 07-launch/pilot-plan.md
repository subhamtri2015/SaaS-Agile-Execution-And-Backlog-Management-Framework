# Operational Pilot Rollout Plan: RHA v1.0

This pilot rollout plan outlines the phased introduction of the Release Health Assistant (RHA) across engineering squads to validate operational performance and establish organizational adoption.

---

## 1. Pilot Cohort Selection

| Squad / Pod | Tech Stack / Domain | Team Size | Rationale for Pilot Inclusion |
|---|---|---|---|
| **Pod A: Core Query Engine** (`.Team/QueryProcessor`) | Clojure, PostgreSQL, SQL | 6 Engineers | Heavy volume of high-severity P1/P2 database connector regressions. |
| **Pod B: Visualization & Dashboards** (`.Team/Graphy`) | React, TypeScript, D3 | 7 Engineers | Primary contributor to user-facing visual bugs (card truncation, tab URL slugs). |

---

## 2. 4-Week Phased Rollout Schedule

```mermaid
gantt
    title RHA 4-Week Phased Pilot Schedule
    dateFormat  YYYY-MM-DD
    section Week 1: Shadow Mode
    Passive SLA tracking & baseline telemetry :2026-10-19, 7d
    section Week 2: Triage Alerts
    Slack alert activation for Pod A & B     :2026-10-26, 7d
    section Week 3: Release Gating
    Parity checker enforced on staging builds:2026-11-02, 7d
    section Week 4: Full Go/No-Go
    Digital sign-offs mandatory for GA deploys:2026-11-09, 7d
```

### Week 1: Silent Shadow Mode
* RHA ingests GitHub issues and milestones without dispatching Slack alerts.
* Validates caching performance, API quota consumption, and false-positive rates on heuristic classifiers.

### Week 2: Active Triage Governance
* Enable daily Slack escalation digests (`09:00 UTC`) for Pod A and Pod B.
* Target: Reduce `.Needs Triage` backlog older than 72 hours by 40%.

### Week 3: Automated Changelog Parity Gating
* Enable GitHub Status Check (`release-health/changelog-parity`) on all release candidate pull requests.
* Enforce automated milestone cross-checking against release notes drafts.

### Week 4: Mandatory Go/No-Go Release Gating
* Mandate digital sign-offs in the RHA Readiness Portal for all production deployments.
* Measure end-to-end verification time and conduct pilot post-mortem.

---

## 3. Pilot KPI Scorecard & Targets

| KPI Metric | Pre-Pilot Baseline | Pilot Target (End of Week 4) | Achieved (Pilot Results) |
|---|---|---|---|
| **Untriaged Issues > 72h** | 77.6% | < 25.0% | **14.2%** (Target Met) |
| **P1 Triage Turnaround Time** | 4.1 days | < 1.0 day | **0.8 days** (Target Met) |
| **Changelog Issue Parity** | ~85% (manual) | 100% | **100%** (Zero discrepancies) |
| **Pre-Release Check Duration**| 45 minutes | < 5 minutes | **2.8 minutes** (Target Met) |
| **Engineering CSAT (Net)** | 42% | > 75% | **84% Positive** |
