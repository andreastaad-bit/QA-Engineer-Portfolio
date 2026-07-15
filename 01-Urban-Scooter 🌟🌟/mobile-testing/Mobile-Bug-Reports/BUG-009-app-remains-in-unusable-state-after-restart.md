# BUG-009: Application Remains in an Unusable State After Restart

## Summary

After encountering a previous application error, restarting the emulator and reopening the Urban Scooter application does not resolve the issue.

The application continues to open directly in the faulty state, preventing further testing or normal use. The issue can only be resolved by uninstalling and reinstalling the application.

## Preconditions

* The Urban Scooter application is installed on the Android emulator.
* The application has previously encountered the account-switching error described in BUG-008.

## Steps to Reproduce

1. Stop the Android emulator.
2. Restart the emulator.
3. Open the Urban Scooter application.
4. Observe the initial screen and application behavior.
5. Attempt to continue using the application.
6. If the problem persists, uninstall the application.
7. Reinstall the application.
8. Open the application again.

## Expected Result

After restarting the emulator and reopening the application, the application should recover from the previous error and allow the user to continue using it normally.

## Actual Result

The application continues to open directly in the faulty state.

The user is unable to continue using the application normally.

The issue can only be resolved by uninstalling and reinstalling the application.

## Impact

This issue prevents the application from recovering from an error state after a restart.

Requiring a complete reinstallation to continue using the application creates a significant usability problem and may result in loss of application data or configuration.

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
