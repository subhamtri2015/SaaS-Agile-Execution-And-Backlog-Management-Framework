# Blocker & Operational Risk Log (Simulated)

This log tracks all technical and operational blockers raised during standups and sprint execution, along with their resolution paths and impact assessments.

---

## 1. Blocker Resolution Log

| Blocker ID | Sprint | Ticket | Description & Impact | Resolution Path | Owner | Resolution Time |
|---|---|---|---|---|---|---|
| **BLK-01** | Sprint 1 | RHA-101 | GitHub API secondary rate limit triggered during bulk issue search; workers paused. | Implemented local SQLite caching with 10-minute TTL and added HTTP 429 exponential backoff jitter. | Tech Lead | 4 hours |
| **BLK-02** | Sprint 2 | RHA-202 | Release notes markdown parser failed on unlinked issue numbers (e.g., "Issue 84169" instead of "#84169"). | Updated regex tokenizer to support flexible issue prefix patterns (`#`, `Issue`, `GH-`). | Full-Stack Eng | 2 hours |
| **BLK-03** | Sprint 2 | RHA-204 | GitHub Actions workflow permissions blocked PR status check writes from fork PRs. | Switched status check triggers to `workflow_run` on the primary branch with scoped write tokens. | DevOps Eng | 5 hours |
| **BLK-04** | Sprint 3 | RHA-301 | Go/No-Go checklist UI experienced state desynchronization during simultaneous reviewer approvals. | Added optimistic UI concurrency locking and database transaction row locks in SQLite. | Frontend Eng | 3 hours |

---

## 2. Ongoing Operational Risks & Watchlist

| Risk ID | Category | Description | Likelihood | Impact | Current Mitigation |
|---|---|---|---|---|---|
| **RSK-01** | Operational | Engineering teams ignore Slack triage alerts due to channel volume. | Medium | High | Daily digest is routed strictly to domain sub-channels (`#team-graphy`, `#team-query-processor`) rather than an all-hands channel. |
| **RSK-02** | Process | Engineers merge PRs without tagging the associated GitHub milestone. | Medium | High | Automated GitHub Action blocks PR merge if milestone field is empty when PR closes an issue. |
| **RSK-03** | Technical | Network latency spikes between RHA and Confluence Cloud API during release publication. | Low | Medium | Asynchronous retry queue with automatic fallback to local markdown export. |
