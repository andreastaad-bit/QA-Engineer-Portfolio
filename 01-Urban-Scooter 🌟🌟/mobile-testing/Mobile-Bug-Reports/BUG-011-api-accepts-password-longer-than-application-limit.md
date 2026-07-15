# BUG-011: API Accepts a Password Longer Than the Application Limit

## Summary

The application limits the courier password field to a maximum of four digits. However, the API accepts a password containing five digits when a courier is created through Postman.

As a result, a courier account can be created with a password that cannot be entered through the application's login form.

## Preconditions

* The Urban Scooter application is available on the Android emulator.
* Access to the courier creation API is available.
* The request can be sent using Postman.

## Steps to Reproduce

1. Open the Urban Scooter application on the Android emulator.
2. Access the application URL using the question mark icon in the bottom-right corner.
3. Send a request to create a new courier using the following request body:

```json
{
  "login": "Andrea",
  "password": "12345",
  "firstName": "sas"
}
```

4. Submit the request.
5. Verify the API response.
6. Attempt to log in to the application using the newly created courier credentials.

## Expected Result

The system should reject the request because the password contains more than the allowed four digits.

The password validation rules should be consistent between the application and the API.

## Actual Result

The API accepts the request and successfully creates the courier with a five-digit password.

However, the application only allows users to enter a maximum of four digits in the password field.

As a result, the created password cannot be entered completely through the application.

## Impact

The API allows the creation of an account with credentials that cannot be used through the application's login interface.

This creates an inconsistency between frontend and backend validation and may result in inaccessible user accounts.

## Testing Environment

* **Device:** Pixel 5
* **Operating System:** Android
* **API Level:** 37
* **Environment:** Android Emulator

## Testing Tools

* Android Emulator
* Pixel 5 virtual device
* Postman

## Defect Tracking

The original defect was identified and documented in Jira during the mobile testing process.
