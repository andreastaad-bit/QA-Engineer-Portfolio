# API Testing Checklist

## Overview

This section contains the API testing checklist used to validate the backend functionality of the Urban Scooter application.

The checklist includes the test scenarios performed, the expected results, the actual results, and the defects identified during testing.

## Testing Scope

For this part of the project, I focused on testing the functionality related to the creation of delivery couriers.

The testing focused on verifying that:

* The API correctly handled `POST` requests for creating new couriers.
* Required data was validated correctly.
* The expected response codes and response messages were returned.
* Notifications and backend logic behaved as expected.
* The information was correctly saved in the database.
* The stored data was updated when necessary.
* Passwords were properly hashed and stored securely.

## Tools

* **Postman** — Used to create and execute API requests and validate responses.
* **Terminal** — Used to connect remotely to the server and verify backend information, including hashed passwords.
* **Jira** — Used to document and track defects identified during testing.
* **Excel** — Used to organize the API testing checklist and document test results.

## Testing Approach

The testing process involved more than simply verifying whether an API returned a successful status code.

I also validated the behavior behind the API by checking whether:

* The backend processed the request correctly.
* The expected information was stored in the database.
* Data was updated when required.
* Passwords were stored as hashes rather than plain text.
* The application logic and notifications behaved as expected.

## Key Takeaway

This testing activity helped me strengthen my understanding of backend validation and API testing.

I learned that a successful response code does not always mean that the backend is functioning correctly. Effective API testing also requires validating the data, business logic, database behavior, and security-related aspects of the application.

The complete API testing checklist is available in the Excel file included in this folder.
