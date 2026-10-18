# User Journey Map: B2B SaaS Triage to Release

This journey map models the end-to-end lifecycle of product feedback, from initial user submission through engineering triage, sprint execution, and final release communication.

---

## 1. Multi-Persona Journey Map

```mermaid
journey
    title B2B SaaS Product Operations: Triage to Release Lifecycle
    section 1. Ingestion & Triage
      User submits issue on GitHub / Portal: 4: End User
      Issue tagged with .Needs Triage: 3: Maintainer
      Triage SLA breaches (>72 hrs, 77.6% debt): 1: Product Ops
      Priority assigned (P1-P4) & assigned to team: 4: Product Ops
    section 2. Sprint Backlog & Planning
      Issue selected into sprint milestone: 5: Engineering Lead
      Story points estimated & acceptance criteria validated: 4: Product Manager
      Engineers begin active development: 4: Software Engineer
    section 3. Release Readiness & Go/No-Go
      PR merged and issue marked closed in Milestone: 5: Software Engineer
      Release candidate built: 4: DevOps
      Changelog cross-checked against milestone issues: 2: Release Manager
      Go/No-Go readiness checklist verified: 3: Release Manager
    section 4. Deployment & Communication
      Release published to Cloud & GitHub: 5: DevOps
      Release notes broadcast to customers: 4: Product Marketing
      Customer verifies fix in production: 5: End User
```

---

## 2. Stage Breakdown, Friction Points & Opportunities

| Stage | Persona & Goal | Key Operational Friction (From Audit) | Product Opportunity (Release Health Assistant) |
|---|---|---|---|
| **1. Intake & Triage** | **Product Ops / Maintainers:** Rapidly filter duplicates, classify defects, assign priority. | **77.6% of issues linger in `.Needs Triage`.** High risk of P1 regressions being buried under P3 cosmetics. | **Automated SLA Breach Alarms:** Alert on untriaged issues > 72 hours; suggest priority based on stack trace. |
| **2. Sprint Planning** | **PM & Eng Lead:** Select issues into milestones, balance bugs (63%) vs features (19%). | High inbound defect volume squeezes roadmap capacity; manual story grooming is inconsistent. | **Standardized Jira Templates:** Clear Gherkin acceptance criteria to prevent ambiguous story scope. |
| **3. Release Gate** | **Release Manager:** Ensure milestone issues match changelog notes and pass regression gates. | Maintainer comments reveal changelog compilation relies on manual cross-referencing with closed milestones. | **Milestone-Changelog Parity Checker:** Automated diff ensuring 100% of closed milestone issues are accounted for. |
| **4. Customer Launch** | **Product Marketing & Support:** Notify customers with clear, accurate release notes. | Customers miss fixes or discover unannounced changes when notes omit patch items. | **Automated Release Notes Generator:** Transform closed milestone tickets into categorized customer notes. |
