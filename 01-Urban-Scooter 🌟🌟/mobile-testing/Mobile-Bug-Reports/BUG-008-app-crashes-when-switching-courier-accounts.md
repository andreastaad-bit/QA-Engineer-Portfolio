# BUG-008: Application Crashes When Switching Courier Accounts

## Summary

After logging out of one courier account, the application may crash when attempting to log in with a different courier account.

In some cases, the application displays an error and does not allow the user to continue using the application, even after closing and reopening it.

## Preconditions

* The Urban Scooter application is installed on the Android emulator.
* At least two valid courier accounts are available.
* The courier credentials were previously created through Postman.

## Steps to Reproduce

1. Open the Urban Scooter application on the Pixel 5 emulator.
2. Enter the application URL using the question mark icon in the bottom-right corner.
3. Log in using the credentials of the first courier.
4. Log out of the application.
5. Attempt to log in using the credentials of a different courier.
6. Observe the application behavior.
7. If the application crashes or displays an error, close and reopen the application.
8. Attempt to continue using the application.

## Expected Result

The application should allow the user to log out from one courier account and log in with a different valid courier account without any issues.

## Actual Result

The application crashes when attempting to switch between courier accounts.

An error is displayed, and the user is unable to continue using the application. In some cases, closing and reopening the application does not resolve the issue.

## Impact

This issue prevents users from switching between valid courier accounts and may leave the application in an unusable state.

The crash can interrupt the user workflow and prevent the application from being used even after restarting it.

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
