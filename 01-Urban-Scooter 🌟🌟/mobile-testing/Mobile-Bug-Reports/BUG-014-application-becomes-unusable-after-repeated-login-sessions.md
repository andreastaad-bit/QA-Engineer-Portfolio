# BUG-014: Application Becomes Unusable After Repeated Login Sessions

## Summary

After using the Urban Scooter application in the emulator for several hours and repeatedly logging in and out of a courier account, the application may enter an unstable state.

The issue prevents the courier account from being used correctly and may also affect the behavior of the Android emulator, resulting in problems such as a black screen and difficulty accessing the emulator settings to uninstall and reinstall the application.

## Preconditions

* The Urban Scooter application is installed on the Android emulator.
* A valid application URL is configured.
* A courier account can be created and used to log in.

## Steps to Reproduce

1. Open the Urban Scooter application on the Android emulator.
2. Create a new courier account.
3. Log in using the newly created courier account.
4. Log out of the application.
5. Log in again using the courier account.
6. Repeat the login and logout process several times while using the application over an extended period of time.
7. Observe the application and emulator behavior.

## Expected Result

As long as the application URL is valid, the application should continue to function correctly after repeatedly logging in and out of a valid courier account.

## Actual Result

The application enters an unstable state and prevents the courier account from being used correctly.

Additional issues may occur in the emulator, including:

* A black screen.
* Unresponsive or unstable emulator behavior.
* Difficulty accessing the emulator settings.
* Difficulty uninstalling the application to resolve the issue.

Reinstalling the application is required to remove the problem and continue testing.

## Impact

This issue significantly affects the application's stability and prevents continued use of the courier account.

The problem may also disrupt the testing environment itself, making it difficult to recover the emulator and requiring a complete application reinstallation.

## Testing Environment

* **Device:** Pixel 5
* **Operating System:** Android
* **API Level:** 37
* **Environment:** Android Emulator
* **Usage duration:** Several hours of repeated application access

## Testing Tools

* Android Emulator
* Pixel 5 virtual device

## Defect Tracking

The original defect was identified and documented in Jira during the mobile testing process.
