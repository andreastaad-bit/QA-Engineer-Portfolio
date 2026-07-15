# OP-BUG-010: Order Status Screen Does Not Display a Countdown Timer

## Summary

The order status screen does not display a countdown timer showing the remaining time for the scooter rental after the order has been accepted.

## Preconditions

* The Urban Scooter web application is accessible.
* The Urban Scooter mobile application is available.
* A valid order has been created.
* A courier account is available.
* The order can be accepted by the courier.

## Steps to Reproduce

1. Open the Urban Scooter application.
2. Place a scooter rental order.
3. Accept the order as a courier using the **Pixie 5 emulator with API 37**.
4. Open the order status screen as the user.
5. Verify the information displayed on the order status screen.

## Expected Result

After the order is accepted, the order status screen should display a countdown timer showing the remaining time of the scooter rental.

The user should be able to see the remaining rental time in real time.

## Actual Result

The order status screen does not display any countdown timer.

No information is provided to the user regarding the remaining time of the rental.

## Impact

The user cannot easily determine how much time remains in the scooter rental.

This may negatively affect the user experience and prevents the user from monitoring the remaining rental time through the order status screen.

## Testing Technique

* Checklist Testing
* Functional Testing
* Mobile Testing
* UI Testing

## Testing Environment

* **Mobile Device:** Pixie 5 Emulator
* **API Level:** 37

## Defect Tracking

The original defect was identified and documented during the Order Placement Checklist and Mobile Testing process.
