# OP-BUG-011: Order Completion Status 5 Is Missing

## Summary

The order status flow does not display a fifth status after the scooter rental has been completed.

## Preconditions

* The Urban Scooter web application is accessible.
* The Urban Scooter mobile application is available.
* The user can create an order for the same day.
* A courier account is available.
* The order can be accepted and completed by the courier.

## Steps to Reproduce

1. Open the Urban Scooter web application in Opera.
2. Place a scooter rental order for the same day.
3. Accept the order using the **Pixie 5 emulator with API 37**.
4. Complete the scooter rental.
5. Check the order status displayed in the application.

## Expected Result

After the scooter rental is completed, a **fifth status** should appear below **Status 4** at the bottom of the order status section.

The fifth status should display a message indicating that the order or rental has been completed.

## Actual Result

Only **Status 4** is displayed.

A fifth status is never added after the scooter rental is completed.

## Impact

The order status flow does not provide a final status indicating that the rental has been completed.

This may make it difficult for the user to confirm the final state of the order and creates an incomplete order status flow.

## Testing Technique

* Checklist Testing
* Functional Testing
* State Transition Testing
* Mobile Testing

## Testing Environment

* **Browser:** Opera
* **Mobile Device:** Pixie 5 Emulator
* **API Level:** 37

## Defect Tracking

The original defect was identified and documented during the Order Placement Checklist and Mobile Testing process.
