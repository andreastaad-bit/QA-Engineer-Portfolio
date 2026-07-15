
# API Bug Reports

## Overview

This folder contains defects identified during the API testing phase of the Urban Scooter project.

The reported issues were identified by validating API responses, business logic, database behavior, and the expected behavior of different order states.

The defects were originally documented in Jira during the testing process and are presented here in a structured format as part of my QA portfolio.

## Testing Focus

The reported defects cover the following areas:

* API response validation.
* HTTP status code validation.
* Order cancellation functionality.
* Courier deletion.
* Database integrity.
* Business logic validation.
* Order state management.
* Error handling for non-existent resources.

## Bug Reports

| ID                                                                         | Description                                                                                         | Area               |
| -------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | ------------------ |
| [BUG-001](./BUG-001-courier-deletion-does-not-remove-associated-orders.md) | Associated orders remain in the database after deleting a courier                                   | Database Integrity |
| [BUG-002](./BUG-002-cancel-existing-order-returns-400.md)                  | Cancelling an existing order returns `400 Bad Request` instead of successfully cancelling the order | Order Cancellation |
| [BUG-003](./BUG-003-cancel-accepted-order-returns-incorrect-error.md)      | Cancelling an accepted order returns an incorrect error response                                    | Business Logic     |
| [BUG-004](./BUG-004-cancel-non-existent-order-returns-incorrect-error.md)  | Cancelling a non-existent order returns an incorrect error response                                 | Error Handling     |

## Key Findings

During testing, I identified several cases where the API returned an unexpected response or where the backend behavior did not match the expected business logic.

Some examples include:

* An order remaining in the database after the associated courier was deleted.
* An existing order returning a `400 Bad Request` response when it should have been successfully cancelled.
* An order that was already being processed returning an incorrect error response.
* A non-existent order returning a `400 Bad Request` instead of a `404 Not Found` response.

## Testing Tools

* **Postman** — API request execution and response validation.
* **Remote Terminal** — Backend and database validation.
* **Emulator** — Validation of order status and courier interactions.
* **Jira** — Defect reporting and tracking.

## Key Takeaway

These defects demonstrated the importance of validating more than just whether an API request was successfully sent.

Effective API testing also requires verifying:

* Whether the returned HTTP status code matches the expected behavior.
* Whether the response message accurately describes the problem.
* Whether the business logic is working correctly.
* Whether related data remains consistent in the database.
* Whether different application states produce the correct responses.

This testing process helped me strengthen my understanding of backend validation, API testing, business logic, and data integrity.
