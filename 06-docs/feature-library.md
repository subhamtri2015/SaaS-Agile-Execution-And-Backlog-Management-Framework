# Feature Library: Release Health Assistant (RHA)

*Confluence Knowledge Base Reference · Space: Product Operations · Page ID: RHA-DOC-001*

---

## 1. Feature Index

| Feature Code | Feature Name | Core Function | Target Users |
|---|---|---|---|
| **FEAT-01** | Triage SLA Monitor | Daily scan and alert on `.Needs Triage` tickets > 72h | Product Ops, Engineering Leads |
| **FEAT-02** | Priority Heuristic Classifier | Regex & keyword scoring for crash/security detection | Triage Engineers |
| **FEAT-03** | Milestone Parity Checker | Bi-directional validation of closed issues vs changelogs | Release Managers |
| **FEAT-04** | Go/No-Go Readiness Portal | Live release gate dashboard with digital sign-offs | QA, DevOps, Release Leads |
| **FEAT-05** | Multi-Target Notes Publisher | Automated push to GitHub Releases and Confluence KB | Product Marketing, Release Leads |

---

## 2. Technical Feature Deep-Dives

### FEAT-01: Triage SLA Monitor
* **Execution Trigger:** Configurable cron job (Default: `0 9 * * 1-5` - 09:00 UTC weekdays).
* **Ingestion Logic:** Queries GitHub API endpoint `/search/issues` filtering `state:open`, label `.Needs Triage`, and creation date `< (NOW - 72h)`.
* **Output Payload:** Constructs a Slack block kit message grouping delinquent tickets by sub-team label.

### FEAT-03: Milestone Parity Checker
* **Validation Algorithm:**
  1. Fetch all issues in Milestone where `state = 'closed'`.
  2. Parse release markdown text searching for tokens matching `#[0-9]+` or `Issue [0-9]+`.
  3. Compute Set Difference:
     $$\Delta_{\text{missing}} = \text{Milestone Issues} \setminus \text{Changelog Issues}$$
  4. If $|\Delta_{\text{missing}}| > 0$, inject status check failure `release-health/changelog-parity: Missing N issues`.

### FEAT-04: Go/No-Go Readiness Portal
* **Evaluation Matrix:**
  - Mandatory Gate 1: Unresolved P1 Bugs == 0.
  - Mandatory Gate 2: CI / CD Test Pipeline == 100% Green.
  - Mandatory Gate 3: Milestone Parity Discrepancies == 0.
  - Mandatory Gate 4: QA Sign-off == Signed.
  - Mandatory Gate 5: Product Ops Sign-off == Signed.
  - Mandatory Gate 6: Engineering Lead Sign-off == Signed.
* **Failure State:** If any mandatory gate evaluates to False, the "Publish Release" action button is physically disabled in the UI.
