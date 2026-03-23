# Atlassian Governance Demo

This project demonstrates how I would standardize, clean up, and scale an Atlassian ecosystem in a fast-growing company. The goal is to simplify workflows, make information easy to find, and create a structured, maintainable environment for all teams.

---

## Scenario

A scaling company is experiencing growing pains:

- 30+ Jira workflows with inconsistent logic  
- 1000+ custom fields, many unused  
- Cluttered Confluence spaces  
- No consistent governance or process for tooling  

**Impact:** Teams face slower onboarding, confusing workflows, reduced productivity, and a higher risk of mistakes.

---

## Goals

- Cut complexity in Jira and Confluence by half  
- Standardize workflows, issue types, and fields  
- Improve the quality and accessibility of the Knowledge Base  
- Introduce clear, enforceable processes for tool usage  

**How success will be measured:**  
- Workflows reduced from 30+ → 15  
- Custom fields reduced by 50%  
- 40% of outdated Confluence pages archived or reorganized  
- Consistent process for requests and approvals in Jira  

---

## Approach

1. **Jira Governance**  
   - Consolidate workflows and standardize issue types across teams  
   - Implement approval processes for new fields  
   - Automate reminders and notifications for stale or overdue tickets  

2. **Confluence Cleanup**  
   - Archive pages that are outdated or no longer relevant  
   - Assign ownership for spaces and templates  
   - Restructure the Knowledge Base for better navigation and discoverability  

3. **Process Governance**  
   - Introduce consistent request handling and approval processes  
   - Define responsibilities and ownership for workflows, fields, and spaces  
   - Monitor usage with dashboards and reports  

4. **Automation Strategy**  
   - Leverage native Jira automation wherever possible  
   - Use lightweight scripts to analyze multiple projects or track compliance  
   - Automate repetitive tasks to free up team time for meaningful work  

---

## Supporting Tools

This repository includes small utilities to help simulate:

- Detecting stale tickets or pages  
- Validating that requests follow the correct process  
- Triggering reminders or notifications based on workflow conditions  

> These tools are **enhancements**, not replacements for core Jira or Confluence functionality.

---

## Case Study Details

See the `/case-study` folder for:

- Governance decisions and workflow standards  
- Automation rules and example triggers  
- Examples of request handling and stakeholder alignment  
- Knowledge Base restructuring strategies  

---

## Explore the Repo

1. Start with `/case-study` to understand how governance is applied  
2. Look at `/src` for examples of automation scripts 
3. Continue with `/.github/workflows` for examples of automation workflows 
