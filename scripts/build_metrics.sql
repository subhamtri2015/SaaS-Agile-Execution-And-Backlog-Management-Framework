-- build_metrics.sql
-- Standalone SQL reference queries for Metabase Product-Ops Audit
-- Can be executed in SQLite or DuckDB against issues, milestones, and releases tables.

-- 1. Backlog Health: Prioritization Coverage & Triage Backlog Debt
SELECT 
    COUNT(*) as total_open_issues,
    SUM(CASE WHEN priority != 'Unassigned' THEN 1 ELSE 0 END) as open_with_priority,
    ROUND(SUM(CASE WHEN priority != 'Unassigned' THEN 1.0 ELSE 0.0 END) / COUNT(*) * 100.0, 2) as pct_prioritized,
    SUM(CASE WHEN needs_triage = 1 THEN 1 ELSE 0 END) as awaiting_triage,
    ROUND(SUM(CASE WHEN needs_triage = 1 THEN 1.0 ELSE 0.0 END) / COUNT(*) * 100.0, 2) as pct_needs_triage
FROM issues
WHERE state = 'open';

-- 2. Open Issues Breakdown by Priority
SELECT 
    priority,
    COUNT(*) as issue_count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM issues WHERE state = 'open'), 1) as percentage
FROM issues
WHERE state = 'open'
GROUP BY priority
ORDER BY issue_count DESC;

-- 3. Cycle Time & Triage Speed by Priority
SELECT 
    priority,
    COUNT(*) as closed_count,
    ROUND(AVG(julianday(closed_at) - julianday(created_at)), 1) as avg_days_to_close
FROM issues
WHERE state = 'closed' AND closed_at IS NOT NULL
GROUP BY priority
ORDER BY priority;

-- 4. Milestone Completion Rate (Sprint Velocity Proxy)
SELECT 
    title as milestone_name,
    state,
    open_issues,
    closed_issues,
    (open_issues + closed_issues) as total_milestone_issues,
    ROUND(closed_issues * 100.0 / CASE WHEN (open_issues + closed_issues) = 0 THEN 1 ELSE (open_issues + closed_issues) END, 1) as completion_rate_pct
FROM milestones
WHERE (open_issues + closed_issues) > 0
ORDER BY id DESC
LIMIT 15;

-- 5. Voice of Customer / Top Pain Points by Weighted Community Engagement
SELECT 
    number as issue_number,
    title,
    priority,
    type,
    comments_count,
    reactions_count,
    (comments_count + reactions_count * 2) as engagement_score
FROM issues
ORDER BY engagement_score DESC
LIMIT 10;
