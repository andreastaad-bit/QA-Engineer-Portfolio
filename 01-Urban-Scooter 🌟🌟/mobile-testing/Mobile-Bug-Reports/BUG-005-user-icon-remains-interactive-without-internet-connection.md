# BUG-005: User Icon Remains Interactive Without an Internet Connection

## Summary

When the device loses its internet connection, the application displays an appropriate connection error message. However, after dismissing the error message, the user icon remains interactive and allows the user to access the logout option.

## Preconditions

* The Urban Scooter application is installed on the Android emulator.
* A courier account has been created through the API.
* The courier is logged in to the application.

## Steps to Reproduce

1. Open the Urban Scooter application on the Pixel 5 emulator.
2. Enter the application URL using the question mark icon in the bottom-right corner.
3. Log in using the courier credentials previously created through Postman.
4. Navigate to the orders page.
5. Disable the internet connection.
6. Wait for the connection error message to appear.
7. Dismiss the error message by tapping **OK**.
8. Tap another active element on the page, such as the user icon in the top-right corner.

## Expected Result

The application should display the following error message:

> "No Internet Connection"

The application should prevent further actions that require an active internet connection.

## Actual Result

After dismissing the connection error message, the user icon remains interactive.

When the user taps the icon, the application responds normally and displays the logout confirmation option.

## Impact

The application allows the user to interact with functionality that requires an internet connection even though the device is offline.

This may lead to inconsistent application behavior and may cause users to believe that actions have been successfully completed when the application cannot communicate with the backend.

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
