# BUG-010: Korean Characters Are Accepted in the Courier Login Field

## Summary

The courier creation request accepts Korean characters in the `login` field, even though this type of input should not be allowed.

The request is processed successfully with a `201 Created` response, and the newly created courier account can subsequently be used to log in to the application.

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
  "login": "안녕",
  "password": "1234",
  "firstName": "saske"
}
```

4. Submit the request.
5. Verify the API response.
6. Attempt to log in to the application using the newly created courier credentials.

## Expected Result

The application or API should reject the request because the `login` field contains Korean characters that are not allowed.

The courier account should not be created successfully.

## Actual Result

The request is accepted successfully and returns:

```text
201 Created
```

The courier account is created successfully and can also be used to log in to the application.

## Impact

The system allows invalid characters in the courier login field and creates an account that should have been rejected.

This may lead to inconsistent data validation and allow users to create accounts that do not comply with the expected input requirements.

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
