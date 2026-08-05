
# Restful Booker API Testing

## Project Overview

This project demonstrates manual API testing for the **Restful Booker REST API** using **Postman**.

The objective of this project is to validate the API's CRUD operations, authentication, request and response handling, and automated test scripts using JavaScript.

> **Note:** Restful Booker is an open-source practice API. Since it is designed for testing purposes, the database is periodically reset, meaning previously created bookings and authentication tokens may no longer be available.
>
> ## Objectives

The main objective of this project was to strengthen my understanding of REST API testing by working with a complete CRUD workflow in Postman.

During this project, I focused on:

- Validating API endpoints using different HTTP methods.
- Testing authentication and authorization workflows.
- Creating and managing reusable Postman environments.
- Writing JavaScript test scripts to validate responses.
- Automatically storing authentication tokens and booking IDs using environment variables.
- Practicing request chaining to simulate real API workflows.

- ## Skills

- API Testing
- RESTful API Testing
- CRUD Operations
- HTTP Methods (GET, POST, PUT, PATCH, DELETE)
- Authentication Testing
- JavaScript Test Scripts
- Environment Variables
- JSON Response Validation
- Request Chaining

- ## API Endpoints Tested

| HTTP Method | Endpoint | Description | Tested |
|-------------|----------|-------------|:------:|
| GET | `/booking` | Retrieve all bookings | ✅ |
| GET | `/booking/{id}` | Retrieve a specific booking | ✅ |
| POST | `/auth` | Generate an authentication token | ✅ |
| POST | `/booking` | Create a new booking | ✅ |
| PUT | `/booking/{id}` | Update an existing booking | ✅ |
| PATCH | `/booking/{id}` | Partially update an existing booking | ✅ |
| DELETE | `/booking/{id}` | Delete an existing booking | ✅ |

## Test Validations

The following validations were implemented using Postman test scripts:

- HTTP status code validation
- Response body validation
- JSON property validation
- Response time validation
- Authentication token validation
- Error response validation
- Environment variable validation
- Automatic token extraction and storage
- Automatic booking ID extraction and storage

- ## Key Learnings

Throughout this project, I strengthened my understanding of:

- REST API architecture and the purpose of each HTTP method.
- Authentication workflows using tokens.
- Creating and managing reusable Postman environments.
- Working with environment variables to store and reuse dynamic data.
- Writing JavaScript test scripts to validate API responses.
- Extracting and storing values such as authentication tokens and booking IDs.
- Building request chains to execute complete API workflows.
- Validating HTTP responses, response bodies, and error scenarios.

- ## How to Run the Project

1. Import the Postman Collection.
2. Import the Environment file.
3. Select the imported Environment.
4. Execute the **POST /auth** request to generate an authentication token.
5. Execute the **POST /booking** request to create a booking and automatically store the booking ID.
6. Run the remaining requests in the collection (GET, PUT, PATCH, and DELETE).
