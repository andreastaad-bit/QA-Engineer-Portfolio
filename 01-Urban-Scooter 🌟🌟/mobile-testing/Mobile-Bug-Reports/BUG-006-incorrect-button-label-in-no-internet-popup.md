# BUG-006: Incorrect Button Label in the No-Internet Connection Popup

## Summary

The button used to close the no-internet connection error popup displays an incorrect label.

The expected button text is **"Aceptar"**, but the application displays **"OK"** instead.

## Preconditions

* The Urban Scooter application is available on the Android emulator.
* A courier account is available for login.
* The device has an active internet connection before starting the test.

## Steps to Reproduce

1. Open the Urban Scooter application on the Android emulator.
2. Tap the question mark icon in the bottom-right corner.
3. Enter the application URL.
4. Log in as a courier using the available courier credentials.
5. Disable the internet connection.
6. Wait for the connection error popup to appear.
7. Review the label of the button used to close the popup.

## Expected Result

The popup should contain a button labeled:

```text
Aceptar
```

The button should allow the user to close the error message.

## Actual Result

The popup contains a button labeled:

```text
OK
```

instead of the expected **"Aceptar"** label.

## Impact

The button label does not match the expected text defined for the application.

This may create an inconsistency in the user interface and may indicate that the expected localization or UI requirements were not implemented correctly.

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
