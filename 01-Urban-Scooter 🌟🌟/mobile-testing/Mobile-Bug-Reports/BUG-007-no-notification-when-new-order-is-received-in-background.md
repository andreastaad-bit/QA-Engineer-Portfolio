# BUG-007: No Notification Is Displayed When a New Order Is Received While the App Is in the Background

## Summary

When the courier is logged into the Urban Scooter application but is using another application, no notification is displayed when a new order is assigned.

## Preconditions

* The Urban Scooter application is installed on the Android emulator.
* A courier account has been created through the API.
* The courier is logged in to the application.
* The application is running in the background.

## Steps to Reproduce

1. Open the Urban Scooter application on the Pixel 5 emulator.
2. Enter the application URL using the question mark icon in the bottom-right corner.
3. Log in using the courier credentials previously created through Postman.
4. Leave the Urban Scooter application and open another application.
5. Create or assign a new order using Postman or the web application.
6. Check the device for a notification about the new order.

## Expected Result

The courier should receive a notification informing them that a new order has been received while the Urban Scooter application is running in the background.

## Actual Result

No notification is displayed when the new order is received.

## Impact

The courier may not be aware that a new order has been assigned while using another application.

This may delay the courier's response to the order and negatively affect the order acceptance process.

## Testing Environment

* **Device:** Pixel 5
* **Operating System:** Android
* **API Level:** 37
* **Environment:** Android Emulator

## Testing Tools

* Android Emulator
* Pixel 5 virtual device
* Postman
* Urban Scooter web application

## Defect Tracking

The original defect was identified and documented in Jira during the mobile testing process.
