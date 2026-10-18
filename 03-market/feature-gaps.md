# Market & Feature Gaps Analysis

Combining the empirical findings from our Metabase GitHub audit with broader competitive intelligence reveals critical operational and product feature gaps.

---

## 1. Feature Gap Matrix

| Identified Gap | Evidence from Real Data | Competitive Comparison | Urgency & Impact |
|---|---|---|---|
| **1. Automated Triage & SLA Enforcement** | **77.6%** of open issues remain stuck in `.Needs Triage`. Triage is largely asynchronous and manual. | Commercial platforms (Jira Service Management, Linear Triage) automate routing rules and SLA timers out of the box. | **High:** Primary bottleneck slowing down overall backlog velocity. |
| **2. Milestone-to-Changelog Reconciliation** | Maintainer issue #10139 confirms milestone tagging is the sole mechanism driving release notes, requiring manual cross-checking. | Modern CI/CD platforms (Release Drafter, GitHub Releases auto-generate) integrate PR labels directly into release markdown. | **High:** Risk of customer blindspots during Metabase's rapid 2.7-day release cycles. |
| **3. Granular Embedded Query Controls** | Issue #83595 (top feedback engagement: 10 comments) requests manual rerun triggers in embedded mode when automatic reruns are paused. | Looker and Power BI provide explicit embedded SDK events to trigger cache invalidation and query reruns. | **Medium:** Direct blocker for B2B SaaS customers using Metabase as an embedded tenant portal. |
| **4. Visual Layout Truncation Overrides** | Issue #84334 (P1 defect) documents titles on KPI number cards disappearing on compact dashboards. | Superset and Tableau allow dynamic responsive typography scaling and customizable card padding. | **Medium:** Diminishes executive dashboard readability on mobile or embedded widgets. |

---

## 2. Product Strategy Response
To directly solve Gaps 1 and 2 (the operational gaps within Product Operations' direct sphere of control), we designed the **Release Health Assistant (RHA)** detailed in `04-requirements/`. The RHA automates triage SLA enforcement, verifies release readiness, and guarantees 100% parity between closed milestone issues and published release notes.
