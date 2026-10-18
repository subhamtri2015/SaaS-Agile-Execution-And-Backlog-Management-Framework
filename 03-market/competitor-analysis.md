# Competitor & Market Analysis

## Purpose

Compare documented workflow capabilities relevant to issue intake and release operations, using only the source notes below (checked 2026-10-18). “Not found in docs read” means the reviewed source did not describe the capability; it does not mean the product lacks it. “Not researched” means no fact was supplied or verified for that cell.

## Capability Comparison

| Capability | Jira Automation | Linear Triage | GitHub release notes | RHA proposed |
|---|---|---|---|---|
| Triage queue / intake review | Not researched | Documented | Not researched | Designed |
| Auto-routing or assignment rules | Documented | Partial / plan-limited | Not researched | Designed |
| Alerts when an issue waits too long untriaged | Partial / plan-limited | Not found in docs read | Not found in docs read | Designed |
| Release-event automation | Documented | Not researched | Not researched | Designed |
| Release-notes generation | Not researched | Not researched | Documented | Designed |
| Closed-issue vs release-notes parity check | Not found in docs read | Not found in docs read | Not found in docs read | Designed |
| Go/No-Go release gate with sign-offs | Not found in docs read | Not found in docs read | Not found in docs read | Designed |

**RHA status:** Proposed design (not built). The “Designed” cells describe scope in this portfolio, not a functioning product.

## Where RHA Differs (Hypothesis)

These tools cover parts of the flow in different products; RHA proposes joining triage-wait alerts, changelog parity and a readiness gate in one workflow. This is a hypothesis to validate with users.

## Where RHA Does Not Compete

RHA is not proposed as a replacement for Jira, Linear, or GitHub. The design assumes those systems remain the systems of record for issues, work planning, release artifacts, and source control. RHA is a proposed coordination layer only.

Direct customer notification is not part of the proposed initial workflow. It is a Later / proposed idea and would require separate validation and ownership.

## Limitations

- This is a limited comparison of the exact documentation links listed below, not a full product evaluation.
- “Not found in docs read” and “Not researched” are evidence labels, not product capability verdicts.
- The audit sample only supports this statement: **In the audit sample, 118 of 152 open issues (77.6%) still carried the `.Needs Triage` label.** It does not establish issue age, assignment, customer churn, or Metabase internal practices.
- Any current/future journey beyond that sample observation is a **Hypothesis based on public tracker data**.
- RHA is a **Proposed design (not built)**. Emotion scores in the journey map are illustrative, not measured.

## Sources

- Linear, [Triage](https://linear.app/docs/triage).
- Linear, [Triage sources](https://linear.app/enablement/guide/triage-sources).
- Atlassian, [Jira Automation triggers](https://confluence.atlassian.com/automation0800/jira-automation-triggers-1189780166.html).
- GitHub Docs, [Automatically generated release notes](https://docs.github.com/en/repositories/releasing-projects-on-github/automatically-generated-release-notes).
- Sources checked 2026-10-18; capability descriptions above are limited to the supplied fact notes.
