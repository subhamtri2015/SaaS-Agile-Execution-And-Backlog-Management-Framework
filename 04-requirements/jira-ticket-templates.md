# Jira Ticket Templates & Standards

This document establishes the Jira ticket schema, engineering standards, and production-ready story cards utilized across the 3 simulated sprints for the **Release Health Assistant (RHA)** project.

---

## 1. Jira Story Ticket Standard (Canonical Template)

```jira
Issue Type: Story
Summary: [Module/Feature] As a <User Persona>, I want <Capability> so that <Business Outcome>
Epic Link: [EPIC-KEY] e.g., RHA-EPIC-01: Triage Automation & SLA Governance
Components: Backend-Worker, Webhook-Ingest, Slack-Bot, Confluence-Sync
Story Points: 1 | 2 | 3 | 5 | 8 (Fibonacci sequence; 8 requires decomposition)
Priority: P1 (Blocker) | P2 (High) | P3 (Medium) | P4 (Low)

1. Business Context & Problem Statement:
[Context detailing why this ticket exists, citing audit telemetry or customer pain point]

2. User Story:
As a <Persona: Product Ops Manager / Engineering Lead / Release Manager>,
I want <to perform an action / receive an alert / view a dashboard>,
So that <business value, speed improvement, or risk reduction is achieved>.

3. Functional Requirements:
- Requirement 1: [Specific system behavior]
- Requirement 2: [Data validation rules]
- Requirement 3: [Security / permission rules]

4. Acceptance Criteria (Given / When / Then - Gherkin Syntax):
Scenario 1: [Standard Happy Path]
  Given <initial precondition>
  And <secondary precondition>
  When <action triggered>
  Then <expected system state>
  And <observable verification metric>

Scenario 2: [Boundary / Edge Case / Failure Mode]
  Given <unusual condition or external API failure>
  When <action attempted>
  Then <graceful fallback behavior>
  And <audit log generated>

5. Technical & Security Notes:
- API endpoints touched:
- Telemetry & logging:
- Permissions required:
- Non-functional requirements (Latency < 200ms, idempotency):

6. Definition of Done (DoD):
- [ ] Unit test coverage >= 85%
- [ ] Integration tests pass in CI pipeline
- [ ] Code reviewed by 1 senior engineer & 1 product peer
- [ ] Confluence documentation updated in Feature Library
- [ ] PR verified on staging environment
```

---

## 2. Sample Production Ticket 1: RHA-101 (Triage SLA Scanner)

```jira
Key: RHA-101
Type: Story
Project: Release Health Assistant (RHA)
Sprint: Sprint 1 (Foundations & Triage Governance)
Epic Link: RHA-EPIC-01 (Triage Automation)
Priority: P1 - High
Story Points: 5
Assignee: Senior Backend Engineer
Reporter: Product Operations Manager

Summary:
As a Product Ops Lead, I want an automated daily scanner for issues with '.Needs Triage' older than 72 hours, so that our 77.6% triage backlog debt is systematically cleared.

Description:
1. Context:
Our real GitHub audit demonstrated that 118 out of 152 open issues (77.6%) remain untriaged with the `.Needs Triage` label, creating massive backlog blindspots and risk of missed customer regressions.

2. User Story:
As a Product Operations Manager,
I want the RHA engine to inspect all open GitHub issues on a scheduled cron (09:00 UTC),
So that any issue lingering in '.Needs Triage' for > 72 hours triggers an escalation digest to the responsible team's Slack channel.

3. Acceptance Criteria:
Scenario 1: Daily scan detects SLA breach
  Given an issue has been open for 75 hours
  And its label set contains '.Needs Triage'
  When the RHA daily scan executes at 09:00 UTC
  Then the issue is flagged as "SLA Breached"
  And it is added to the daily team Slack digest with issue number, title, author, and age in days.

Scenario 2: Issue triaged within SLA
  Given an issue has had its '.Needs Triage' label removed or assigned a priority within 72 hours
  When the RHA scan runs
  Then the issue is excluded from the breach escalation digest.

Scenario 3: GitHub API Rate Limit Backoff
  Given GitHub API rate limit header 'X-RateLimit-Remaining' drops below 50
  When the scanner attempts to fetch the next batch of 100 issues
  Then the scanner pauses execution, logs an INFO backoff message, and retries after the reset epoch without crashing.

4. Definition of Done:
- [x] Python worker unit tests written with mock GitHub responses.
- [x] Slack webhook integration tested in staging channel #product-ops-alerts.
- [x] README and Feature Library entry created in 06-docs/.
```

---

## 3. Sample Production Ticket 2: RHA-204 (Milestone-to-Changelog Parity Validator)

```jira
Key: RHA-204
Type: Story
Project: Release Health Assistant (RHA)
Sprint: Sprint 2 (Release Gate & Changelog Automation)
Epic Link: RHA-EPIC-02 (Release Readiness & Integrity)
Priority: P2 - High
Story Points: 5
Assignee: Full-Stack Engineer
Reporter: Release Manager

Summary:
As a Release Manager, I want RHA to cross-validate closed milestone issues against draft release notes, so that zero bug fixes ship without documented customer-facing release notes.

Description:
1. Context:
Metabase maintainer practice dictates that closing an issue into a milestone qualifies it for release notes. However, manual reconciliation results in undocumented bug fixes or PRs erroneously attributed.

2. User Story:
As a Release Manager,
I want an automated diff tool comparing Milestone-closed issues against the draft Release Markdown,
So that any closed issue missing from the release notes triggers a blocker warning on the Go/No-Go readiness checklist.

3. Acceptance Criteria:
Scenario 1: Full parity between Milestone and Changelog
  Given Milestone 'v0.52.2' contains 14 closed issues
  And the draft release notes mention all 14 issue numbers (e.g., #84169, #83595)
  When the pre-release readiness checklist evaluates the release candidate
  Then the "Changelog Integrity" check displays GREEN (100% matched)
  And the release candidate is marked "Eligible for Staging Deploy".

Scenario 2: Unattributed closed issues detected
  Given 2 closed issues in the milestone are missing from the release notes
  When the parity validation runs
  Then the check status displays RED ("Missing 2 issue references")
  And an automated markdown table of missing tickets is appended to the draft release notes.

4. Definition of Done:
- [x] Regex parser implemented for GitHub release markdown bodies.
- [x] Automated status check reported to GitHub PR status checks API.
- [x] Validated against sample historical releases (v0.51.5 and v0.52.1).
```

---

## 4. Jira Bug Ticket Template

```jira
Issue Type: Bug
Summary: [Defect] <Concise summary of failure>
Priority: P1 (Crashing/Data Loss) | P2 (Severe degradation) | P3 (Minor defect) | P4 (Cosmetic)
Labels: Type:Bug, Component:<Module>, FoundIn:<Version>

1. Expected Behavior:
[What should happen based on PRD specifications]

2. Actual Behavior:
[What actually occurred, including HTTP status codes, tracebacks, or UI anomalies]

3. Steps to Reproduce:
1. Navigate to ...
2. Click on ...
3. Observe error ...

4. Regression / Environment Details:
- Environment: Staging / Production
- Browser / Client: Chrome 128 / macOS
- Impacted Users: All tenant admins with Slack integration enabled

5. Proposed Remediation & Root Cause:
[Root cause hypothesis and suggested pull request target]
```
