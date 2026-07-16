# OP-BUG-012: Order Status Does Not Update Automatically After Courier Actions

## Summary

The order status displayed in the web application does not update automatically when the courier changes the order status. The user must manually refresh the page to see the updated status.

## Preconditions

* The Urban Scooter web application is accessible.
* The Urban Scooter mobile application is available.
* A scooter rental order can be created for the same day.
* A courier account can be created.
* The courier application can access the order.

## Steps to Reproduce

1. Open the Urban Scooter web application.
2. Place a scooter rental order for the same day.
3. Open the **Pixie 5 emulator with API 37**.
4. Create a courier account using **Postman**.
5. Access the order as the courier using the emulator.
6. Accept the order.
7. Return to the order status screen in the web application.
8. Observe the displayed order status.

## Expected Result

The order status displayed in the web application should update automatically after the courier accepts the order.

The user should be able to see the status change without manually refreshing the page.

## Actual Result

The order status does not update automatically.

The user must manually refresh the page to see the change in the order status.

## Impact

The application does not provide real-time synchronization between the courier's actions and the user's order status.

This may cause the user to see outdated information and requires manual page refreshes after each status change.

## Testing Technique

* Checklist Testing
* Functional Testing
* State Transition Testing
* Real-Time Data Synchronization Testing
* Cross-Platform Testing

## Testing Environment

* **Browser:** Opera
* **Mobile Device:** Pixie 5 Emulator
* **API Level:** 37
* **API Tool:** Postman

## Defect Tracking

The original defect was identified and documented during the Order Placement Checklist and Mobile Testing process.
