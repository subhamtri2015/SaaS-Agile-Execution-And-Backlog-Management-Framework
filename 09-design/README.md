# Design Handoff

## Status

The app prototype URL is available below. A separate Figma design-file view URL and PNG exports have not been supplied yet. No Figma screenshots are represented as complete. Add the remaining links after creating and sharing the files:

- Figma view: [pending]
- Clickable app prototype: [Release Health Assistant](https://www.figma.com/make/13NZrWaErDzkE7RG2Kq8Tu/Release-Health-Assistant-App?t=Fj9kotGJ3uU33jWD-1)

Export these hand-built Figma frames to this folder when available:

- `screen-1-triage.png`
- `screen-2-parity.png`
- `screen-3-readiness.png`
- `prd-at-a-glance.png`

Do not use the Metabase name or logo in the design. Existing SVG assets elsewhere in this repository are illustrations, not screenshots of a working app. Any mock figures, including 41 breaching and 94% parity, must retain a visible **Sample data** label and must not be presented as measured results.

## PRD at a Glance: 1440 x 1024 Frame

Use a title bar and a two-column grid of six boxes. Keep each box concise and use the copy below as the source. Personas are hypothetical. Metrics labeled assumption are targets, not results.

### Problem

- 77.6% of open issues in the sample (118/152) carried `.Needs Triage` at any age.
- We hypothesize that manual reconciliation of closed milestone issues and release notes could cause omissions. Internal process was not observed.

### Users

- **Hypothetical: Alex**, Product Ops Lead; monitors triage and routes issues.
- **Hypothetical: Priya**, Release Manager; reviews release scope and readiness.
- **Hypothetical: Marcus**, Engineering Lead; clarifies work and tracks delivery risks.

### Goals / Non-goals

- **G1:** Reduce open issues with `.Needs Triage` older than 72 hours to <15%; baseline not measured.
- **G2:** Detect release-note parity gaps; 100% verification is an assumption/target.
- **G3:** Reduce readiness review to <3 minutes; baseline and target are assumptions.
- **NG1:** No autonomous code changes or bot PRs.
- **NG2:** Does not replace GitHub or Jira.
- **NG3:** No customer-facing portal rewrite.

### Scope

- **Epic 1, Triage Automation:** 19 points; scan, alert, telemetry, API/cache spike, optional P1 suggestion.
- **Epic 2, Parity Validator:** 21 points; extract milestone issues, parse notes, compare, check status, draft notes.
- **Epic 3, Readiness:** 22 points; readiness UI, sign-off, publishing, pilot feedback, proposed integration testing.
- **Total backlog:** 62 points, matching `04-requirements/backlog.csv`. Delivery artifacts are simulated.

### Metrics: Baseline to Target

| Metric | Baseline | Target |
|---|---|---|
| `.Needs Triage`, any age | 77.6% (118/152 open sampled issues) | <15% older than 72h; baseline for this definition not measured |
| P1 time to first priority label | Not measured; needs issue events | <1 day (assumption) |
| Changelog parity | Not measured (assumption: ~85%) | 100% (assumption) |
| Readiness sign-off time | Not measured (assumption: ~45 min) | <3 min (assumption) |

### Risks and Mitigations

- **API rate limits:** authenticated requests where available, caching, and retry/backoff; numeric limits are targets.
- **Alert fatigue:** configurable mute/snooze controls and team mapping review.
- **Incomplete milestone data:** surface missing, transferred, and reopened issues for human resolution; do not treat milestones as formal sprints.

## Figma Make / Credits

Figma's [pricing page](https://www.figma.com/pricing/) currently lists Starter with 150 AI credits per day, up to 500 AI credits per month. Its [Figma Make help page](https://help.figma.com/hc/en-us/articles/31304412302231-Explore-Figma-Make) says Make is available for Full seats on paid plans and can be tried on other seats and plans. These pages do not substantiate the third-party article's claim about sharing three Make files, so no such limit is asserted here.
