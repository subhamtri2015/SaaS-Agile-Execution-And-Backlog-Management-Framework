# Methodological Limitations & Ground Rules

To ensure transparency and rigorous analytical integrity, this audit explicitly documents all proxies, assumptions, and data limitations.

---

## 1. Disclaimers & Non-Affiliation
* **Independent Third-Party Analysis:** This audit is conducted strictly for educational and portfolio demonstration purposes. The author is **not affiliated with, endorsed by, or employed by Metabase, Inc.**
* **Neutral Observation:** All metrics, evaluations, and observations are based solely on publicly available issue trackers. No internal company processes, undocumented discussions, or private customer ticketing channels are implied or evaluated.

---

## 2. Proxies & Operational Assumptions

| Metric | Real World Meaning | GitHub Data Proxy | Known Limitation |
|---|---|---|---|
| **Sprint Velocity** | Story points or tickets delivered within a fixed 2-week agile sprint | **Milestone Completion Rate:** Ratio of closed issues to total issues in a GitHub Milestone | Milestones in open-source projects may span variable lengths (from 1 week to several months) and are adjusted dynamically as issues are deferred. |
| **Triage Latency** | Time elapsed from ticket creation until first triage and assignment | **.Needs Triage Status & Resolution Speed:** Time to close or presence of `.Needs Triage` label | Public data only captures final state transitions; intermediate unlabelled time before first label assignment is not timestamped in basic REST summaries. |
| **Customer Pain** | Enterprise churn risk or ticket revenue impact | **Reaction and Comment Volume:** Aggregated emoji reactions and thread lengths | Public community activity over-indexes on tech-savvy open-source power users compared to quiet enterprise cloud buyers. |

---

## 3. Data & Privacy Compliance
1. **Zero Full-Text Commit:** Issue markdown bodies, user emails, and raw comment text are excluded from version control to respect author copyright and prevent PII leakage.
2. **Aggregated Artifacts:** All committed data files in `data/processed/` are scrubbed, high-level structural metrics.
3. **Simulated vs. Real Demarcation:**
   - **Real:** All charts, tables, and statistics in `02-audit/` and `data/` are derived from the live GitHub REST API.
   - **Simulated:** All sprint ceremony artifacts, burndown curves, and pilot rollouts in `05-sprints-simulated/` and `07-launch/` are structured simulations based on the real audit findings.
