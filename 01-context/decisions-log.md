# Decisions Log: Product Operations & Engineering Strategy

This log records major product-ops and architectural decisions made throughout the audit and product response phases, articulating the alternatives evaluated, the chosen solution, and the accompanying trade-offs.

---

### Decision 1: Target Product Selection (Horizontal B2B SaaS vs. Vertical Robotics)
* **Date:** 2026-10-18
* **Status:** Approved
* **Context:** The initial proposal explored vertical robotics data. However, robotics issue trackers lack standardized public SaaS telemetry and have niche terminology unfamiliar to generalist hiring managers.
* **Options Considered:**
  1. *Vertical Robotics internal logs:* Highly specialized, limited public data, requires NDA/synthetic masking.
  2. *Proprietary B2B CRM scraping:* High risk of ToS violations, fragile HTML selectors.
  3. *(Chosen) Metabase Public GitHub Data:* Universally recognized open-source B2B analytics platform with rigorous issue labeling (`Priority:P1-P4`, `.Needs Triage`, `Type:Bug`), milestones mapped to release notes, and legal REST API access.
* **Trade-off:** Metabase issues mix open-source community bug reports with enterprise feature requests; pull requests are included in GitHub's `/issues` endpoint and must be filtered out systematically.

---

### Decision 2: Data Extraction Strategy & Proxy Mapping
* **Date:** 2026-10-18
* **Status:** Approved
* **Context:** GitHub does not have a formal native "Sprint" concept like Jira; it uses Milestones and Issues.
* **Options Considered:**
  1. *Fabricate 100% synthetic sprint data from scratch:* High flexibility, but zero defensibility in an audit.
  2. *Direct 1:1 mapping of Milestones as Sprints without caveats:* Inaccurate, because milestones in open-source often span longer or irregular timeframes.
  3. *(Chosen) Hybrid Proxy Architecture:* Extract real Metabase issues, milestones, and releases for Part A (Audit), while explicitly labeling Milestone completion as a **Sprint Velocity Proxy**. Use real audit findings to seed a grounded, simulated delivery cycle in Part B.
* **Trade-off:** Explicit labeling required across all documentation so hiring managers understand the boundary between real audit telemetry and simulated execution.

---

### Decision 3: Storage & Licensing Compliance (Zero Issue Text Storage)
* **Date:** 2026-10-18
* **Status:** Approved
* **Context:** GitHub public data contains user-authored text, comments, and profile information subject to author copyright and GitHub Acceptable Use terms.
* **Options Considered:**
  1. *Commit raw JSON dumps with full issue bodies to Git:* Violates data minimization, inflates repository size, risks exposing sensitive author PII.
  2. *(Chosen) Gitignored Raw Cache + Committed Aggregate Schemas:* Cache raw JSON locally in `data/raw/` (strictly `.gitignore`d). Commit only anonymized, normalized metrics and aggregated CSVs in `data/processed/`.
* **Trade-off:** External reviewers must run `scripts/fetch_github.py` with their own API token if they wish to inspect raw issue strings locally, but repository integrity and legal hygiene are protected.

---

### Decision 4: PRD vs. Release Documentation Separation
* **Date:** 2026-10-18
* **Status:** Approved
* **Context:** A common failure mode in product portfolios is conflating the upstream Product Requirements Document (PRD) with downstream release documentation (Release Notes & Readiness Checklists).
* **Options Considered:**
  1. *Combine PRD, sprint stories, and release notes into a single monolithic document.*
  2. *(Chosen) Distinct Lifecycle Segregation:*
     - **04-requirements/PRD-release-health-assistant.md:** Upstream specification (Problem Statement, Personas, Goals & Non-goals, Functional Specs, Gherkin Acceptance Criteria, Risks).
     - **06-docs/release-notes.md & readiness-checklist.md:** Downstream operational artifacts created when code is packaged for deployment (Changelog, breaking changes, test sign-offs, go/no-go criteria).
* **Trade-off:** Requires maintaining two distinct document formats, but visually proves senior-level PM methodology to recruiters.

---

### Decision 5: Scope & Delivery Phasing for Part B (Simulated Sprints)
* **Date:** 2026-10-18
* **Status:** Approved
* **Context:** The audit revealed that **77.6%** of open issues languish in `.Needs Triage`, and release readiness checks are manually synchronized between milestones and changelogs.
* **Options Considered:**
  1. *Build a full-stack automated triage bot with autonomous merge privileges:* High complexity, excessive scope, unsafe for production deployments.
  2. *(Chosen) "Release Health Assistant" - MVP in 3 Sprints:*
     - **Sprint 1 (Foundations):** Triage aging scanner & SLA breach alerting engine.
     - **Sprint 2 (Release Gate):** Milestone-to-Changelog automated reconciler.
     - **Sprint 3 (Pilot & Operations):** Readiness checklist dashboard & stakeholder sign-off portal.
* **Trade-off:** Scope strictly constrained to 3 sprints (60 story points total) with non-goals (autonomous code fixing) explicitly deferred to Future Roadmap.
