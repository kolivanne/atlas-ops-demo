## Example: Translating a Vague Request into Actionable Jira Work

### Input (Business Request)
"We need better tracking for bugs"

---

### Clarification Process
**Goal:** Translate a high-level request into actionable Jira work while aligning stakeholders.

Questions asked:
- Which teams and systems are affected?
- What metrics or KPIs should be tracked?
- Are SLAs or priority levels required?
- Dependencies with other projects or tools?
- Expected reporting / dashboards for managers?

Stakeholder alignment:
- Quick session with development leads and QA manager
- Documented requirements in Confluence before Jira implementation

---

### Output (Jira Structure)

**Epic:** Bug Tracking Standardization  
**Goal:** Standardize bug reporting and tracking across teams

**User Stories:**
1. As a developer, I want standardized bug fields (Severity, Component, Steps to Reproduce) to ensure consistent reporting.
2. As a manager, I want visibility on resolution time via dashboards to monitor team performance.
3. As a QA engineer, I want automated notifications for critical bugs to prioritize remediation.

**Implementation Details:**
- **Issue Type:** New Bug schema with required fields: Severity, Component
- **Screens & Fields:** Custom fields configured to enforce standard input
- **Workflows:** Standardized bug workflow (To Do → In Progress → QA Review → Done)
- **SLAs & Automation:**
  - SLA: 48h response time for critical bugs
  - Automation: Notify assignee if bug remains in To Do > 24h
  - Dashboard: Track open bugs, resolution times, SLA compliance

---

### Key Outcomes
- Clear and actionable Jira structure from ambiguous request
- Standardized bug reporting improves data quality and team alignment
- Automation reduces manual follow-up and ensures SLA compliance
- Metrics: # of standardized bugs reported, average resolution time, SLA adherence