## Example: Translating a Vague Request into Actionable Jira Work

### Input (Business Request)
“We need to automate employee onboarding for new hires.”

---

### Clarification Process
**Goal:** Translate a high-level request into actionable Jira work while aligning stakeholders.

Questions asked:
- Which systems require access (Slack, Jira, Confluence, email, internal tools)?  
- What approvals are needed (manager, HR, security, IT)?  
- Are there role-based templates for different departments?  
- Expected metrics: time-to-fully-onboard, missing access requests  
- Dependencies with other processes or tools?

Stakeholder alignment:
- Sessions with HR, IT, and Security teams  
- Documented requirements in Confluence before Jira implementation  

---

### Output (Jira Structure)

**Epic:** New Employee Onboarding Automation  
**Goal:** Standardize and automate onboarding across departments

**User Stories:**
1. As IT, I want automated account creation for standard roles to reduce manual setup  
2. As HR, I want automated welcome emails and Confluence onboarding guide assignment  
3. As Security, I want automated access review reminders for managers  

**Implementation Details:**
- **Issue Types:** Onboarding Task (standardized across departments)  
- **Screens & Fields:** Required fields: Employee Name, Department, Role, Start Date, Systems Access Needed  
- **Workflows:**  
  - Draft → Pending Approvals → Provisioning → Completed  
- **Automation Rules:**  
  - Notify IT when task enters Pending Approvals  
  - Auto-generate subtasks for each system access  
  - Send reminder emails for pending approvals  
- **SLA:** Access fully provisioned within 48h of hire approval  
- **Dashboard:** Track onboarding completion, bottlenecks, and SLA adherence  

---

### Key Outcomes
- Clear and actionable Jira structure from an ambiguous request  
- Standardized onboarding reduces manual work and errors  
- Automation ensures SLA compliance and timely provisioning  
- Metrics: time-to-fully-onboard, % of tasks automated, completion rate by department