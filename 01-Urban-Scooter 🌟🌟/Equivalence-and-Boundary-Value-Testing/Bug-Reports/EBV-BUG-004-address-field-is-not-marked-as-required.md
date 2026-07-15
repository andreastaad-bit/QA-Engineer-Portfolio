# EBV-BUG-004: Address Field Is Not Marked as Required

## Summary

The **Address** field on the **"Place an Order"** page is described as a required field in the requirements. However, the application allows the user to continue through the order form without entering an address.

## Preconditions

* The Urban Scooter web application is accessible.
* The user is on the **"Place an Order"** page.

## Steps to Reproduce

1. Open the Urban Scooter web application.
2. Navigate to the **"Place an Order"** section.
3. Enter the following value in the **First Name** field:

```text
Andrea
```

4. Enter the following value in the **Last Name** field:

```text
Guerra
```

5. Select a metro station.
6. Enter a valid phone number.
7. Leave the **Address** field empty.
8. Attempt to continue to the next step of the order form.

## Expected Result

The application should prevent the user from continuing to the next step.

The **Address** field should be identified as required and highlighted in red to indicate that the field must be completed.

## Actual Result

The application allows the user to continue through the order form without entering an address.

No validation error is displayed.

## Impact

Users can continue the order process without providing information that is defined as mandatory in the requirements.

This may result in incomplete order data and could cause problems during the delivery process.

## Testing Technique

* Equivalence Partitioning
* Input Validation
* Required Field Validation

## Testing Environment

* **Device:** Hacer Laptop
* **Operating System:** Windows 11
* **Processor:** Intel Core i5
* **Browser:** Opera
* **Browser Version:** 14.7.0.7727.56

## Defect Tracking

The original defect was identified and documented during the Equivalence Partitioning and Boundary Value Analysis testing process.
