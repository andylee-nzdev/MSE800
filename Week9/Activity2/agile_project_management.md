# Jira Sprint Plan

**Project Title:** 
Peer-to-Peer Bicycle Rental Platform

**Group Name:** 
Group-D

**Team Members:**
- Dongfang Wang
- Xiaoning Li

## 1. Purpose of the Jira Sprint Plan

This document describes how the Peer-to-Peer Bicycle Rental Platform project will be managed using Jira. The project will follow a Scrum-based approach with three one-week sprints. Each sprint will have a clear goal, deliverables, assigned issues, and acceptance criteria.

The project will be completed by a two-person development team within a three-week development period. Jira will be used to manage the backlog, sprint planning, task assignment, progress tracking, testing, and final delivery preparation.

---

## 2. Project Management Approach

The project will use an agile Scrum-style workflow. The full project will be divided into three sprints, with each sprint representing one week of development.

Each sprint will focus on a specific set of features:

| Sprint   | Focus Area                                                   |
| -------- | ------------------------------------------------------------ |
| Sprint 1 | Project setup, authentication, and user profile              |
| Sprint 2 | Bike listing, upload, search, and admin approval             |
| Sprint 3 | Booking, deposit, damage report, admin review, testing, deployment, and documentation |

The Jira board will be used to track all project issues from planning to completion.

---

## 3. Jira Issue Structure

The Jira project will use the following issue types:

| Issue Type | Purpose                                                     |
| ---------- | ----------------------------------------------------------- |
| Epic       | Represents a large feature area or major module             |
| Story      | Represents user-facing functionality                        |
| Task       | Represents technical work, setup, testing, or documentation |
| Sub-task   | Represents smaller work items under a Story or Task         |
| Bug        | Represents defects found during development or testing      |

---

## 4. Jira Epics

The project will be divided into eight main epics.

| Epic ID | Epic Name                               | Description                                                  |
| ------- | --------------------------------------- | ------------------------------------------------------------ |
| EPIC-1  | Project Setup & Development Environment | Repository setup, Docker, backend, frontend, and database configuration |
| EPIC-2  | Authentication & User Profile           | User registration, login, JWT authentication, and role selection |
| EPIC-3  | Bike Listing Management                 | Bike creation, editing, deletion, photo upload, and ownership evidence upload |
| EPIC-4  | Search & Listing Approval               | Bike search, filtering, and admin approval or rejection      |
| EPIC-5  | Booking & Rental Workflow               | Booking request, approval, rejection, handover, return, and rental status tracking |
| EPIC-6  | Deposit & Damage Report                 | Simulated deposit calculation, deposit confirmation, and damage report submission |
| EPIC-7  | Admin Review & Dashboard                | Admin dispute review, deposit release or deduction, and dashboard views |
| EPIC-8  | Testing, Deployment & Documentation     | Testing, CI workflow, deployment preparation, README, report, and demo script |

---

## 5. Jira Workflow

The Jira board will use a simple workflow suitable for a small academic development team.

| Status      | Meaning                                                      |
| ----------- | ------------------------------------------------------------ |
| To Do       | The issue has been planned but not started                   |
| In Progress | The issue is currently being worked on                       |
| Code Review | The implementation is ready for review by the other team member |
| Testing     | The issue is being tested manually or automatically          |
| Done        | The issue has been completed and accepted                    |

This workflow is simple enough for a two-person team but still supports visibility, accountability, and quality control.

---

## 6. Sprint Overview

| Sprint   | Duration | Main Goal                                                    | Expected Issue Count |
| -------- | -------- | ------------------------------------------------------------ | -------------------- |
| Sprint 1 | Week 1   | Build project foundation and authentication flow             | 8–10 issues          |
| Sprint 2 | Week 2   | Complete bike listing, upload, search, and approval          | 10–12 issues         |
| Sprint 3 | Week 3   | Complete booking, deposit, damage review, testing, deployment, and final documents | 16–20 issues         |

The full Jira project is expected to contain approximately **35 to 42 issues**.

---

## 7. Sprint 1: Project Foundation and Authentication

### Sprint Goal

The goal of Sprint 1 is to establish the full-stack development environment and complete the basic user authentication and profile system.

By the end of this sprint, the application should run locally, and users should be able to register, log in, and select their roles.

### Sprint 1 Issues

| Issue Type | Summary                                                      | Epic                                    | Assignee | Priority | Story Points |
| ---------- | ------------------------------------------------------------ | --------------------------------------- | -------- | -------- | ------------ |
| Task       | Create GitHub repository and branch workflow                 | Project Setup & Development Environment | Shared   | High     | 2            |
| Task       | Configure Docker Compose for backend, frontend, and PostgreSQL | Project Setup & Development Environment | Member 1 | High     | 3            |
| Task       | Create Django REST Framework backend project                 | Project Setup & Development Environment | Member 1 | High     | 3            |
| Task       | Create React Vite frontend project                           | Project Setup & Development Environment | Member 2 | High     | 2            |
| Task       | Configure environment variables for backend and database     | Project Setup & Development Environment | Member 1 | Medium   | 2            |
| Story      | As a user, I want to register an account                     | Authentication & User Profile           | Member 1 | High     | 3            |
| Story      | As a user, I want to log in using JWT authentication         | Authentication & User Profile           | Member 1 | High     | 5            |
| Story      | As a user, I want to select my role as renter, lender, or both | Authentication & User Profile           | Member 2 | High     | 3            |
| Task       | Create basic React layout and navigation                     | Project Setup & Development Environment | Member 2 | Medium   | 3            |
| Task       | Create initial API endpoint documentation                    | Testing, Deployment & Documentation     | Shared   | Medium   | 2            |

### Sprint 1 Deliverables

- GitHub repository created
- Docker Compose environment configured
- Django backend project created
- React frontend project created
- PostgreSQL connected
- User registration implemented
- JWT login implemented
- User role selection implemented
- Basic frontend navigation completed
- Initial API endpoint notes created

---

## 8. Sprint 2: Bike Listing, Upload, Search, and Admin Approval

### Sprint Goal

The goal of Sprint 2 is to allow lenders to create bike listings, upload bike photos and ownership evidence, and allow admins to approve or reject listings.

Renters should also be able to search and view approved bikes.

### Sprint 2 Issues

| Issue Type | Summary                                                      | Epic                                | Assignee | Priority | Story Points |
| ---------- | ------------------------------------------------------------ | ----------------------------------- | -------- | -------- | ------------ |
| Task       | Implement Bike, BikeImage, and OwnershipEvidence models      | Bike Listing Management             | Member 1 | High     | 5            |
| Story      | As a lender, I want to create a bike listing                 | Bike Listing Management             | Member 1 | High     | 5            |
| Story      | As a lender, I want to upload bike photos                    | Bike Listing Management             | Member 1 | High     | 5            |
| Story      | As a lender, I want to upload ownership evidence             | Bike Listing Management             | Member 1 | High     | 5            |
| Story      | As a lender, I want to edit and delete my own listings       | Bike Listing Management             | Member 1 | High     | 5            |
| Task       | Add listing approval status: pending, approved, rejected     | Search & Listing Approval           | Member 2 | High     | 3            |
| Story      | As an admin, I want to approve or reject bike listings       | Search & Listing Approval           | Member 2 | High     | 5            |
| Story      | As a renter, I want to search approved bikes                 | Search & Listing Approval           | Member 2 | High     | 5            |
| Task       | Add filters by location, type, size, price, condition, and availability | Search & Listing Approval           | Member 2 | High     | 5            |
| Task       | Build bike detail page                                       | Bike Listing Management             | Member 2 | Medium   | 3            |
| Task       | Add backend tests for listing permissions and approval       | Testing, Deployment & Documentation | Shared   | Medium   | 3            |
| Task       | Integrate frontend listing pages with backend APIs           | Bike Listing Management             | Shared   | High     | 5            |

### Sprint 2 Deliverables

- Lenders can create bike listings
- Lenders can upload bike photos
- Lenders can upload ownership evidence
- Only bike owners can edit or delete their own listings
- Listings have approval status
- Admins can approve or reject listings
- Renters can search approved bikes
- Basic search filters work
- Bike detail page is available
- Basic backend tests for listing and approval are completed

---

## 9. Sprint 3: Booking, Deposit, Damage Review, Testing, and Deployment

### Sprint Goal

The goal of Sprint 3 is to implement the core rental workflow, complete the remaining admin workflow, improve system quality, prepare deployment, and produce final assessment materials.

By the end of this sprint, renters should be able to request bookings, lenders should be able to approve or reject them, and the system should support deposit calculation, handover confirmation, return confirmation, rental status tracking, damage reporting, admin review, testing, deployment preparation, and final documentation.

### Sprint 3 Issues

| Issue Type | Summary                                                      | Epic                                | Assignee | Priority | Story Points |
| ---------- | ------------------------------------------------------------ | ----------------------------------- | -------- | -------- | ------------ |
| Task       | Design Booking model and status transition rules             | Booking & Rental Workflow           | Member 2 | High     | 5            |
| Story      | As a renter, I want to create a booking request              | Booking & Rental Workflow           | Member 2 | High     | 5            |
| Story      | As a lender, I want to approve or reject booking requests    | Booking & Rental Workflow           | Member 2 | High     | 5            |
| Task       | Implement booking status transitions                         | Booking & Rental Workflow           | Member 2 | High     | 8            |
| Task       | Implement simulated deposit calculation                      | Deposit & Damage Report             | Member 2 | High     | 3            |
| Story      | As a renter, I want to confirm simulated deposit payment     | Deposit & Damage Report             | Member 2 | High     | 3            |
| Story      | As a renter and lender, I want to confirm handover           | Booking & Rental Workflow           | Member 2 | High     | 5            |
| Story      | As a renter and lender, I want to confirm return             | Booking & Rental Workflow           | Member 2 | High     | 5            |
| Story      | As a user, I want to view rental status tracking             | Booking & Rental Workflow           | Member 1 | Medium   | 5            |
| Task       | Build renter booking management page                         | Booking & Rental Workflow           | Member 1 | High     | 5            |
| Task       | Build lender booking management page                         | Booking & Rental Workflow           | Member 1 | High     | 5            |
| Task       | Write tests for booking status transitions and deposit calculation | Testing, Deployment & Documentation | Shared   | Medium   | 5            |
| Story      | As a user, I want to submit a damage report with evidence    | Deposit & Damage Report             | Member 2 | High     | 5            |
| Story      | As an admin, I want to review damage disputes and decide deposit release or deduction | Admin Review & Dashboard | Member 2 | High | 8 |
| Task       | Add renter, lender, and admin dashboard views                | Admin Review & Dashboard            | Member 1 | Medium   | 5            |
| Task       | Improve frontend validation, loading, empty, and error states | Testing, Deployment & Documentation | Member 1 | Medium   | 5            |
| Task       | Complete backend and manual end-to-end tests for key workflows | Testing, Deployment & Documentation | Shared   | High     | 8            |
| Task       | Configure GitHub Actions and Docker Compose deployment preparation | Testing, Deployment & Documentation | Member 1 | Medium   | 5            |
| Task       | Write README, API documentation, final report, demo script, and screenshots | Testing, Deployment & Documentation | Shared | High | 8 |

### Sprint 3 Deliverables

- Renters can create booking requests
- Lenders can approve or reject booking requests
- Booking status transitions are implemented
- Simulated deposit calculation works
- Renters can confirm simulated deposit payment
- Handover confirmation works
- Return confirmation works
- Rental status tracking page is available
- Renter and lender booking management pages are implemented
- Booking and deposit tests are completed
- Damage report submission works
- Damage evidence upload works
- Admin dispute review works
- Deposit release or partial deduction works
- Dashboard views are available
- Frontend validation and error handling are improved
- Loading, empty, and error states are added
- Key backend tests are completed
- Manual end-to-end testing is completed
- GitHub Actions workflow is configured
- Deployment configuration is prepared
- README and API documentation are completed
- Final report and demo script are ready

---

## 10. Story Point Estimation Guide

The project will use story points to estimate the relative complexity of Jira issues.

| Story Point | Meaning                                                      |
| ----------- | ------------------------------------------------------------ |
| 1           | Very small task                                              |
| 2           | Small technical task                                         |
| 3           | Standard task or simple feature                              |
| 5           | Medium feature with backend or frontend integration          |
| 8           | Complex feature involving multiple models, APIs, frontend pages, and tests |
| 13          | Too large and should be split into smaller issues            |

Each sprint should ideally contain around **18 to 30 story points per person**, depending on the complexity of the work and available study time.

---

## 11. Team Responsibility Plan

The team will divide work by business modules rather than strictly separating frontend and backend.

### Member 1 Responsibilities

Member 1 will mainly focus on:

- Project environment setup
- Authentication support
- User profile
- Bike listing models and APIs
- Bike image and ownership evidence upload
- Lender listing management
- Search page support
- Dashboard views
- Deployment configuration
- Testing and documentation support

### Member 2 Responsibilities

Member 2 will mainly focus on:

- React project setup
- Role selection UI
- Admin listing approval
- Search and filter UI
- Booking model and APIs
- Rental status transitions
- Deposit calculation
- Handover and return confirmation
- Damage report
- Admin dispute review
- Testing and documentation support

### Shared Responsibilities

Both members will share responsibility for:

- Requirements refinement
- API contract discussion
- Code review
- Manual end-to-end testing
- Bug fixing
- README
- Final report
- Demo script
- Presentation preparation

---

## 12. Definition of Done

An issue will be considered complete only when it satisfies the following conditions:

- The backend API or frontend component is implemented.
- The feature meets the acceptance criteria.
- Required permissions and validations are applied.
- Success and error responses are handled.
- The feature has been manually tested.
- Important backend logic has automated tests where practical.
- The code has been reviewed by the other team member.
- The issue is moved to the `Done` column in Jira.
- Any related documentation or endpoint notes are updated.

---

## 13. Example Jira Story

### Story: Create Bike Listing

**Issue Type:** Story

**Summary:**  
As a lender, I want to create a bike listing.

**Description:**  
As a lender, I want to create a bicycle listing with title, type, size, condition, location, rental price, original price, purchase date, and description, so that renters can view and request my bike after admin approval.

**Acceptance Criteria:**

- The lender must be logged in.
- The lender can submit a bike listing form.
- Required fields must be validated.
- A new listing must have the default status `pending`.
- Only the bike owner can edit or delete the listing.
- The API must return clear success and error responses.
- The frontend form must connect to the backend API.

**Epic:** Bike Listing Management  
**Sprint:** Sprint 2  
**Priority:** High  
**Story Points:** 5  
**Assignee:** Member 1

---

## 14. Example Jira Story

### Story: Create Booking Request

**Issue Type:** Story

**Summary:**  
As a renter, I want to create a booking request.

**Description:**  
As a renter, I want to select an approved bike and submit a booking request with rental start and end time, so that the lender can approve or reject the request.

**Acceptance Criteria:**

- The renter must be logged in.
- The bike must be approved and available.
- The renter can select rental start and end time.
- The system validates that the end time is after the start time.
- The booking status is initially set to `pending`.
- The lender can view the booking request.
- The renter can view the booking status.
- Invalid requests return clear error messages.

**Epic:** Booking & Rental Workflow  
**Sprint:** Sprint 3  
**Priority:** High  
**Story Points:** 5  
**Assignee:** Member 2

---

## 15. Risk Management in Jira

Risks will be tracked during sprint planning and sprint review.

| Risk                                        | Impact                                              | Mitigation                                            |
| ------------------------------------------- | --------------------------------------------------- | ----------------------------------------------------- |
| Scope becomes too large                     | The project may not be completed within three weeks | Keep advanced features out of the MVP                 |
| Booking status logic becomes complex        | Bugs may appear in the rental workflow              | Define allowed status transitions early and test them |
| File upload causes integration problems     | Listings or reports may not show evidence correctly | Implement local media upload first                    |
| Frontend and backend integration is delayed | Features may work separately but fail together      | Agree on API contracts before implementation          |
| Deployment problems occur near the deadline | Final demonstration may be affected                 | Keep a local demo version working at all times        |
| Limited team size                           | Some features may be rushed                         | Prioritise must-have features before polish           |

---

## 16. Final Jira Plan Summary

The Jira project will contain:

| Item         | Recommended Count              |
| ------------ | ------------------------------ |
| Sprints      | 3                              |
| Epics        | 8                              |
| Stories      | 18–24                          |
| Tasks        | 12–16                          |
| Bugs         | Added during testing if needed |
| Total Issues | Approximately 35–42            |

Each sprint will contain around **8 to 20 Jira issues**, with the final sprint carrying additional testing and delivery work.  
Each team member will normally take **4 to 10 issues per sprint**, depending on the complexity and timing of the sprint.

This structure keeps the project manageable for a two-person MSE Master team while still showing clear planning, agile process, task ownership, and development progress.
