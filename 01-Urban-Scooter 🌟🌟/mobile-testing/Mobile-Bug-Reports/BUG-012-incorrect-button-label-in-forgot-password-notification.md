# BUG-012: Incorrect Button Label in the Forgot Password Notification

## Summary

The button used to close the notification displayed after selecting **"Forgot password"** contains an incorrect label.

The expected button text is **"Aceptar"**, but the application displays **"OK"** instead.

## Preconditions

* The Urban Scooter application is installed on the Android emulator.
* The login screen is accessible.

## Steps to Reproduce

1. Open the Urban Scooter application on the Android emulator.
2. Tap the question mark icon in the bottom-right corner.
3. Enter the application URL.
4. Tap the **"Forgot password"** option.
5. Review the button displayed in the notification.

## Expected Result

The notification should contain a button labeled:

```text
Aceptar
```

The button should allow the user to close the notification.

## Actual Result

The notification contains a button labeled:

```text
OK
```

instead of the expected **"Aceptar"** label.

## Impact

The button label does not match the expected text defined for the application.

This creates an inconsistency in the user interface and may indicate an issue with the expected localization or UI requirements.

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
