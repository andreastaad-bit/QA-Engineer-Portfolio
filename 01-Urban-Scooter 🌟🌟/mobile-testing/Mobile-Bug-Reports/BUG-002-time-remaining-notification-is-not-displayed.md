# BUG-002: Time-Remaining Notification Is Not Displayed

## Summary

The notification informing the courier about the remaining time to complete an order is not displayed at the expected time.

## Preconditions

* The Urban Scooter application is installed on the Android emulator.
* A courier account is available.
* An order scheduled for the same day exists.

## Steps to Reproduce

1. Open the Urban Scooter application.
2. Log in as a courier.
3. Accept an order scheduled for the same day.
4. Change the emulator time to 9:59 PM.
5. Check whether the time-remaining notification is displayed.

## Expected Result

The following notification should be displayed:

> "2 hours until the end of the order. The order `State St 1214` must be completed. If you cannot arrive on time, contact support: 0101."

## Actual Result

The expected notification is not displayed.

## Testing Environment

* **Device:** Pixel 5
* **Operating System:** Android
* **API Level:** 37
* **Environment:** Android Emulator

## Impact

The courier does not receive the expected notification about the remaining time to complete the order. This may prevent the courier from being informed about the order deadline and the available support option.

## Testing Tools

* Android Emulator
* Pixel 5 virtual device

## Defect Tracking

The original defect was identified and documented in Jira during the mobile testing process.
