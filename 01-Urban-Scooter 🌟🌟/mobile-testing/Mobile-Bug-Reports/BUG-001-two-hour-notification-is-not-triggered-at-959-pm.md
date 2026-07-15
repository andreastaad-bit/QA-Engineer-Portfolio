# BUG-001: Two-Hour Notification Is Not Triggered at 9:59 PM

## Summary

The notification indicating the remaining time to complete an order is not triggered at the expected time.

When the application reaches 9:59 PM, no notification is displayed to inform the user about the remaining time to complete the order.

## Preconditions

* The Urban Scooter application is installed on the Android emulator.
* A courier account has been created.
* The user can log in to the application.
* An order has been created.
* The order is in progress.

## Steps to Reproduce

1. Open the Urban Scooter application on the Android emulator.
2. Add the application URL using the question mark icon in the bottom-right corner.
3. Log in using the courier credentials created during API testing.
4. Create an order.
5. Change the emulator time to 9:58 PM.
6. Wait until the time reaches 9:59 PM.
7. Check whether the notification is displayed.

## Expected Result

A notification should be displayed informing the user about the remaining time to complete the order.

## Actual Result

When the emulator time reaches 9:59 PM, no notification is displayed.

## Testing Environment

* **Device:** Pixel 5
* **Operating System:** Android 11
* **API Level:** 37
* **Environment:** Android Emulator

## Impact

The user does not receive the expected time-based notification, which may prevent them from being properly informed about the remaining time to complete the order.

## Testing Tools

* Android Emulator
* Pixel 5 virtual device

## Defect Tracking

The original defect was identified and documented in Jira during the mobile testing process.
