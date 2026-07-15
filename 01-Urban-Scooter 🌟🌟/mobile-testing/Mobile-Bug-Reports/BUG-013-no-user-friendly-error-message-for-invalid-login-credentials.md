# BUG-013: No User-Friendly Error Message Is Displayed for Invalid Login Credentials

## Summary

When a user attempts to log in with credentials that do not belong to any registered courier, the application does not display a clear and user-friendly error message.

Instead, the application displays a technical `HTTP 404 Not Found` error at the bottom of the screen without explaining what went wrong or how the user should proceed.

## Preconditions

* The Urban Scooter application is installed on the Android emulator.
* The login screen is accessible.
* The provided login credentials do not belong to any registered courier.

## Steps to Reproduce

1. Open the Urban Scooter application on the Android emulator.
2. Tap the question mark icon in the bottom-right corner.
3. Enter the application URL.
4. Enter login credentials that do not belong to any existing courier.
5. Attempt to log in.
6. Observe the error message displayed by the application.

## Expected Result

The application should display a clear validation or authentication error message informing the user that the provided login credentials are invalid or that the courier could not be found.

For example:

> "Invalid username or password."

or another appropriate user-friendly message according to the application's requirements.

## Actual Result

The application displays the following technical error:

```text id="tqddlu"
HTTP 404 Not Found
```

The error is displayed at the bottom of the screen, but no clear message explains the problem to the user.

## Impact

The technical error message does not provide enough information for the user to understand why the login attempt failed.

This may lead to confusion and creates a poor user experience because a backend HTTP error is exposed without being properly handled by the application interface.

## Testing Environment

* **Device:** Pixel 5
* **Operating System:** Android
* **API Level:** 37
* **Environment:** Android Emulator

## Testing Tools

* Android Emulator
* Pixel 5 virtual device

## Defect Tracking

The original defect was identified and documented in Jira during the mobile testing process.
