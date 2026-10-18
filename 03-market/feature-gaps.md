# Market & Feature Gaps Analysis

This analysis combines a public GitHub issue sample with a limited review of official Jira and Linear workflow documentation. It identifies a product opportunity to test, not a verified universal market gap.

---

## 1. Feature Gap Matrix

| Opportunity | Evidence and limits | Existing documented capabilities | Product response to explore |
|---|---|---|---|
| **1. Aging triage visibility** | 118 of 152 open issues in the sample (77.6%) carried `.Needs Triage` at any age. Age-specific waiting time and assignment state were not measured. | Jira documents configurable automation, including auto-assignment and Slack/GitHub integrations. Linear documents a triage inbox, rules, and triage responsibility. | Specify an aging scan and human-reviewed digest; evaluate usefulness in a pilot before making an outcome claim. |
| **2. Milestone-to-notes review** | The sample includes milestone and release records, but does not measure omissions or observe maintainers' internal reconciliation process. | Jira offers flexible automation; the reviewed Linear triage documentation focuses on intake and routing. The reviewed sources do not establish whether either product supports this exact workflow natively. | Prototype a comparison between a selected milestone issue set and draft release notes; present gaps for review. |
| **3. Release readiness coordination** | No production release-gate behavior was measured in the audit. | Existing workflow tools provide automation primitives; detailed release-gate coverage was not evaluated in this limited review. | Specify a readiness checklist and sign-off record as a proposed workflow, not a delivered capability. |

---

## 2. Product Strategy Response
The proposed **Release Health Assistant (RHA)** in [`04-requirements/`](../04-requirements/) explores these connected workflows. It is not implemented: the 72-hour value is a proposed target, parity is not measured, and no release-readiness behavior has been executed. For feature references and sources, see the [competitor comparison](./competitor-table.md).
