# Jira Governance & Strategy

## Key Decisions
- Only IT can create or modify workflows
  - Workflow change requests submitted via Jira Service Desk
- Teams can manage boards, sprints, and filters
- Custom fields require IT approval via request process
- Exceptions must be documented and approved

## Standardization

### Allowed Issue Types
- Epic
- Story
- Task
- Bug
- Optional: Sub-task, Spike (requires approval)

### Workflow Strategy
- One standard workflow per business function (e.g., Product, Tech)
- Avoid team-specific workflows unless formally approved
- Status categories standardized:
  - To Do / In Progress / Done
- Exceptions logged in an approval table

### Naming Conventions
- Workflows: `[Function] - [Workflow Name]`
- Custom fields: `[Team] - [Field Purpose]`

## Stale Ticket Handling
- **Criteria**
  - StatusCategory = "To Do" or "In Progress"
  - Not updated for 30+ days
  - Not in active sprint
  - Not high priority
- **Actions**
  - Add label `stale`
  - Notify assignee via automation
  - Escalate to team lead after 7 days
  - Auto-close after 60 days unless exception applied
- **Monitoring**
  - Stale ticket dashboard for managers
  - Quarterly review of auto-closure accuracy

## Audit & Review
- Monthly Jira workflow and field audit by IT admins
- KPI tracking:
  - % of tickets following standard workflows
  - number of workflow/custom field requests
  - Reduction in duplicate workflows

## Tradeoffs
- Reduced flexibility for teams
- Increased clarity, maintainability, and reporting accuracy

## Communication & Training
- Governance rules documented in Confluence space
- Teams trained on standard workflows, issue types, and request process
- Ongoing support via Jira Service Desk for questions or exceptions