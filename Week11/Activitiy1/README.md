# Functional and Non-Functional Requirements

## Project

**Peer-to-Peer Bicycle Rental Platform**

This document provides a detailed list of functional and non-functional requirements for Assessment 2. Each requirement includes a brief description and the sprint in which it belongs.

---

## Functional Requirements


| ID    | Requirement                          | Brief Description                                                                                                                         | Sprint   |
| ----- | ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| FR-01 | User registration                    | Users can create an account with username, email, and password.                                                                           | Sprint 1 |
| FR-02 | JWT login and logout                 | Users can log in using JWT authentication and log out by clearing frontend authentication state.                                          | Sprint 1 |
| FR-03 | Protected routes                     | Authenticated-only pages redirect unauthenticated users to login.                                                                         | Sprint 1 |
| FR-04 | User profile management              | Authenticated users can view and update their own profile details.                                                                        | Sprint 1 |
| FR-05 | Renter and lender role selection     | Users can select renter role, lender role, or both roles.                                                                                 | Sprint 1 |
| FR-06 | Bicycle listing creation             | Lenders can create bicycle listings with type, size, condition, location, price, age, and description.                                    | Sprint 2 |
| FR-07 | Lender-only listing creation         | Only users with lender role can create bicycle listings.                                                                                  | Sprint 2 |
| FR-08 | Bicycle photo upload                 | Lenders can upload bicycle photos for their own listings.                                                                                 | Sprint 2 |
| FR-09 | Ownership evidence upload            | Lenders can upload ownership evidence for their own bicycles.                                                                             | Sprint 2 |
| FR-10 | Listing ownership permissions        | Only the listing owner or an admin can update or delete a bicycle listing.                                                                | Sprint 2 |
| FR-11 | Listing approval workflow            | New bicycle listings are pending by default and admins can approve or reject them.                                                        | Sprint 2 |
| FR-12 | Public bicycle search                | Renters and visitors can browse approved and available bicycles only.                                                                     | Sprint 2 |
| FR-13 | Search and filtering                 | Users can filter bicycle search results by nearby location, radius, type, condition, size, and price where supported by the API.          | Sprint 2 |
| FR-14 | Bicycle detail page                  | Users can view detailed bicycle information and photos before booking.                                                                    | Sprint 2 |
| FR-15 | Booking request creation             | Renters can submit booking requests for approved and available bicycles.                                                                  | Sprint 3 |
| FR-16 | Booking validation rules             | The system prevents renters from booking their own bicycles, unavailable bicycles, or invalid date ranges.                                | Sprint 3 |
| FR-17 | Lender booking approval or rejection | Lenders can approve or reject booking requests for bicycles they own.                                                                     | Sprint 3 |
| FR-18 | Rental status workflow               | Booking status moves through pending, deposit pending, handover pending, active, return pending, completed, disputed, or rejected stages. | Sprint 3 |
| FR-19 | Simulated deposit calculation        | The system calculates a deposit after booking approval based on bicycle value, age, and condition.                                        | Sprint 3 |
| FR-20 | Deposit confirmation                 | Renters can confirm simulated deposit payment before handover.                                                                            | Sprint 3 |
| FR-21 | Handover confirmation                | Renter and lender can both confirm bicycle handover before the rental becomes active.                                                     | Sprint 3 |
| FR-22 | Return confirmation                  | Renter and lender can confirm return; completed rentals release the deposit when no dispute exists.                                       | Sprint 3 |
| FR-23 | Booking management page              | Users can view renter and lender bookings, current status, total cost, and deposit status.                                                | Sprint 3 |
| FR-24 | Damage report submission             | Renter or lender can submit a damage report with optional evidence during valid rental stages.                                            | Sprint 4 |
| FR-25 | Dispute status update                | Submitting a valid damage report moves the related booking into disputed status.                                                          | Sprint 4 |
| FR-26 | Admin dispute review                 | Admin users can review damage reports and record a decision, deduction amount, and notes.                                                 | Sprint 4 |
| FR-27 | Deposit release or partial deduction | Admin review updates deposit release status and deduction amount, then completes the booking.                                             | Sprint 4 |
| FR-28 | Dashboard views                      | Users can view profile, bookings, owned bicycles, and admin summary data where permitted.                                                 | Sprint 4 |
| FR-29 | Admin listing dashboard              | Admin users can view pending listings and approve or reject them from the admin page.                                                     | Sprint 4 |
| FR-30 | Health check endpoint                | The backend exposes a simple health endpoint for local checks and deployment verification.                                                | Sprint 1 |


---

## Non-Functional Requirements


| ID     | Requirement                                 | Brief Description                                                                                                                            | Sprint          |
| ------ | ------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| NFR-01 | Technology stack compliance                 | The project uses Django REST Framework, React, Vite, Axios, PostgreSQL, JWT, Docker, and GitHub Actions as required by the assessment scope. | Sprint 1        |
| NFR-02 | Local Docker-based development              | The full stack can run locally using Docker Compose for repeatable development and demonstration.                                            | Sprint 1        |
| NFR-03 | Secure password storage                     | User passwords are stored through Django's built-in user system rather than in plain text.                                                   | Sprint 1        |
| NFR-04 | JWT-protected API access                    | Protected API requests require a valid JWT token.                                                                                            | Sprint 1        |
| NFR-05 | Role-based access control                   | Renter, lender, and admin actions are restricted according to user role and ownership.                                                       | Sprints 1-4     |
| NFR-06 | Data validation                             | Forms and APIs validate required data, ownership, booking dates, deduction amounts, and workflow state.                                      | Sprints 1-4     |
| NFR-07 | Clear API error handling                    | Invalid or unauthorized actions return clear JSON error responses.                                                                           | Sprints 1-4     |
| NFR-08 | Maintainable project structure              | Frontend, backend, deployment, and documentation are separated into clear directories.                                                       | Sprint 1        |
| NFR-09 | Testability                                 | Key business rules can be verified with automated backend tests.                                                                             | Sprints 3-4     |
| NFR-10 | Deployment readiness                        | The project includes production-oriented Docker Compose and Nginx configuration for demonstration deployment.                                | Sprint 4        |
| NFR-11 | Configuration through environment variables | Secrets, database connection details, allowed hosts, CORS, and CSRF settings are configurable outside source code.                           | Sprints 1 and 4 |
| NFR-12 | Usable academic MVP interface               | The frontend provides simple pages, navigation, loading messages, empty states, and clear action buttons for demonstration.                  | Sprints 1-4     |
| NFR-13 | Documentation support                       | Project setup, sprint planning, deployment, and requirements are documented for assessment review.                                           | Sprint 4        |
| NFR-14 | CI support                                  | GitHub Actions are used to check backend and frontend quality gates.                                                                         | Sprint 4        |
| NFR-15 | File upload support for MVP evidence        | The system supports local media upload for bicycle photos, ownership evidence, and damage evidence.                                          | Sprints 2 and 4 |


---

## Sprint Coverage Summary


| Sprint   | Requirement Coverage                                                                                                                                                                       |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Sprint 1 | Project setup, authentication, protected routes, user profile, role selection, health check, Docker development environment, secure password handling, JWT setup.                          |
| Sprint 2 | Bicycle listings, owner permissions, image and evidence upload, admin listing approval, search, filtering, and bicycle detail pages.                                                       |
| Sprint 3 | Booking requests, booking validation, lender approval or rejection, rental status workflow, simulated deposit calculation, deposit confirmation, handover, return, and booking management. |
| Sprint 4 | Damage reports, dispute handling, admin reviews, deposit release or deduction, dashboards, testing, CI, deployment readiness, and final documentation.                                     |


