# OP-BUG-009: Order Can Be Cancelled After the Courier Accepts It

## Summary

The user can cancel an order even after the courier has already accepted it.

## Preconditions

* The Urban Scooter web application is accessible.
* The Urban Scooter mobile application is available.
* A courier account has been created.
* A valid order has been created.
* The order is available for the courier to accept.

## Steps to Reproduce

1. Open the Urban Scooter web application.
2. Place an order.
3. Open the Urban Scooter mobile application using the **Pixie 5 emulator with API 37**.
4. Download the application package using the icon in the bottom-left corner.
5. Enter the following URL:

```text
https://cnt-939c2499-4142-4899-9ac8-21764fcbc871.containerhub.tripleten-services.com
```

6. Open the mobile application using the courier information previously created through **Postman**.
7. Accept the order as the courier.
8. Return to the user application.
9. Attempt to cancel the order.

## Expected Result

The user should not be able to cancel the order after the courier has accepted it.

The **Cancel Order** button should be disabled or unavailable once the order has been accepted by the courier.

## Actual Result

The user can cancel the order even after the courier has already accepted it.

## Impact

The application allows the user to cancel an order after the courier has accepted it, which may cause inconsistencies in the order lifecycle and courier workflow.

This may result in a courier accepting an order that can still be cancelled by the user without any restriction.

## Testing Technique

* Checklist Testing
* Functional Testing
* State Transition Testing
* Mobile Testing
* Cross-Platform Testing

## Testing Environment

* **Mobile Device:** Pixie 5 Emulator
* **API Level:** 37
* **Web Browser:** Google Chrome
* **API Tool:** Postman

## Defect Tracking

The original defect was identified and documented during the Order Placement Checklist and Mobile Testing process.
