# OP-BUG-001: Pickup Address Field Is Not Required

## Summary

The **Pickup Address** field in the order form allows the user to proceed without entering any information, even though the field is required according to the form requirements.

## Preconditions

* The Urban Scooter web application is accessible.
* The user can access the order form.
* The order form is available.

## Steps to Reproduce

1. Open the Urban Scooter web application.
2. Click **ORDER** in the top-right corner.
3. Enter valid information in the following fields:

   * First name
   * Last name
   * Metro station
   * Phone number
4. Leave the **Pickup Address** field empty.
5. Click **NEXT**.

## Expected Result

The application should prevent the user from proceeding to the next step.

The **Pickup Address** field should be highlighted in red and display a validation error indicating that the field is required.

## Actual Result

The application allows the user to click **NEXT** and proceed to the next step without completing the **Pickup Address** field.

No validation error is displayed.

## Impact

The application allows the user to continue the order placement process with incomplete required information.

This may result in orders being created without a necessary pickup address and creates an inconsistency between the expected form validation behavior and the implemented functionality.

## Testing Technique

* Checklist Testing
* Input Validation
* Required Field Validation

## Testing Environment

* **Device:** Hacer Laptop
* **Operating System:** Windows 11
* **Browser:** Google Chrome

## Defect Tracking

The original defect was identified and documented during the Order Placement Checklist testing process.
