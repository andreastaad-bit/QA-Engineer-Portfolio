# BUG-004: Accepted Order Is Displayed Twice in the "My Orders" Tab

## Summary

After accepting an order, the same order is displayed twice in the courier's **"My Orders"** tab.

Although the order is successfully displayed in the correct section, the duplicate entry creates confusion and makes it unclear whether there are multiple orders or whether the same order has been duplicated.

## Preconditions

* The Urban Scooter application is available on the Android emulator.
* A courier account has been created through the API.
* The courier credentials are available for login.

## Steps to Reproduce

1. Open the Urban Scooter application on the Android emulator.
2. Enter the application URL using the icon in the bottom-right corner.
3. Log in as a courier using the credentials previously created through Postman.
4. Create a new order through the application.
5. Accept the order.
6. Navigate to the **"My Orders"** tab.

## Expected Result

The accepted order should be displayed once in the **"My Orders"** tab with a **"Complete"** button.

## Actual Result

The accepted order is displayed twice in the **"My Orders"** tab.

## Impact

Displaying the same order multiple times may confuse the courier and make it unclear whether the entries represent different orders or a duplicated order.

This may also lead to incorrect actions or difficulties when managing and completing orders.

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
