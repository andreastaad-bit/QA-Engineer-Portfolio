# BUG-003: Two-Hour Delivery Limit Notification Is Not Displayed

## Summary

The notification informing the courier about the two-hour time limit to accept and deliver an order is not displayed on the courier platform.

## Preconditions

* The Urban Scooter application is available on the Android emulator.
* A courier account has been created through the API.
* The courier credentials are available for login.

## Steps to Reproduce

1. Open the Android emulator.
2. Open the Urban Scooter application.
3. Enter the application URL using the icon in the bottom-right corner.
4. Log in as a courier using the credentials previously created through Postman.
5. Change the emulator time to 10:00 PM.
6. Check the courier platform for the two-hour delivery limit notification.

## Expected Result

A notification should be displayed informing the courier about the two-hour time limit available to accept and deliver the order.

## Actual Result

No notification is displayed on the courier platform.

## Testing Environment

* **Device:** Pixel 5
* **Operating System:** Android
* **API Level:** 37
* **Environment:** Android Emulator

## Impact

The courier does not receive the expected information about the two-hour time limit for accepting and delivering the order. This may affect the courier's ability to understand the time constraints associated with the order.

## Testing Tools

* Android Emulator
* Pixel 5 virtual device
* Postman

## Defect Tracking

The original defect was identified and documented in Jira during the mobile testing process.
