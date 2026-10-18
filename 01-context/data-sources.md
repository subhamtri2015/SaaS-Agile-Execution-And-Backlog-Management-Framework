# Data Sources & Schema Reference

All raw and processed data utilized in this audit originates directly from the official **Metabase** GitHub repository via authenticated GitHub REST API endpoints.

---

## 1. Endpoints Utilized

| Entity | GitHub API Endpoint | Query Parameters | Fields Extracted |
|---|---|---|---|
| **Issues** | `GET /repos/metabase/metabase/issues` or `/search/issues` | `q=repo:metabase/metabase is:issue`, `per_page=100` | `number`, `state`, `title`, `created_at`, `closed_at`, `labels`, `milestone`, `comments`, `reactions` |
| **Milestones** | `GET /repos/metabase/metabase/milestones` | `state=all`, `per_page=100` | `id`, `number`, `title`, `state`, `open_issues`, `closed_issues`, `due_on`, `closed_at` |
| **Releases** | `GET /repos/metabase/metabase/releases` | `per_page=100` | `id`, `tag_name`, `name`, `draft`, `prerelease`, `published_at`, `body` |

---

## 2. Processed Schemas (`data/processed/`)

### `issues.csv`
* `number`: Unique GitHub issue number.
* `state`: Issue lifecycle state (`open` or `closed`).
* `title`: Cleaned issue title string.
* `created_at`: ISO-8601 creation timestamp.
* `closed_at`: ISO-8601 resolution timestamp (or NULL if open).
* `comments_count`: Total comment interactions.
* `reactions_count`: Total reaction emoji interactions (👍, ❤️, 🚀, etc.).
* `priority`: Normalized priority string (`P1`, `P2`, `P3`, or `Unassigned`) observed in this sample.
* `type`: Issue classification (`Bug`, `New Feature`, `Documentation`, or `Unassigned`).
* `needs_triage`: Binary integer flag (1 if tagged `.Needs Triage`, else 0).
* `milestone_title`: Associated milestone name (e.g. `0.52.1`).
* `labels_csv`: Semicolon-delimited list of raw label strings.

### `milestones.csv`
* `id`: Milestone unique database ID.
* `number`: Milestone sequence number.
* `title`: Semantic version title (e.g., `0.51.5`).
* `state`: `open` or `closed`.
* `open_issues`: Count of unresolved tickets in the milestone.
* `closed_issues`: Count of resolved tickets in the milestone.
* `created_at`: Milestone kickoff date.
* `due_on`: Target completion date.
* `closed_at`: Formal milestone closure timestamp.

### `releases.csv`
* `id`: GitHub release ID.
* `tag_name`: Git release tag (e.g., `v0.64.1`).
* `name`: Public release title.
* `draft`: Boolean flag indicating draft status.
* `prerelease`: Boolean flag indicating Beta/RC vs General Availability.
* `created_at`: Tag creation timestamp.
* `published_at`: Public deployment timestamp.
* `body_length`: Character length of published release notes.
* `author_login`: Deploying engineer/bot handle.
