# OP-BUG-008: Rental Date Allows a Date Before the Current Date

## Summary

The rental form allows the user to select a date before the current date and complete the rental process, even though rentals should only be available for the current date or the following day.

## Preconditions

* The Urban Scooter web application is accessible.
* The user can access the order form.
* The rental form is available.

## Steps to Reproduce

1. Open the Urban Scooter web application.
2. Click **ORDER**.
3. Complete the personal information form.
4. Complete the rental form.
5. Select a rental date before the current date.
6. Continue with the rental process.
7. Confirm the rental order.

## Expected Result

The application should not allow the user to schedule a scooter rental for a date before the current date.

The application should either:

* Display a validation error indicating that the selected date is invalid; or
* Prevent the user from continuing with the rental process.

Only the current date or the following day should be available for rental according to the expected behavior.

## Actual Result

The application allows the user to complete the rental process with a date before the current date.

After the rental is created, the application only marks **Status 1** in red and displays a message indicating that the courier is late and the scooter cannot be delivered.

## Impact

The application allows invalid rental dates to be submitted and creates a rental that cannot be fulfilled.

This results in an invalid order and indicates that date validation is performed after the rental has already been created instead of preventing the invalid input beforehand.

## Testing Technique

* Checklist Testing
* Input Validation
* Date Validation
* Negative Testing
* Boundary Value Analysis

## Testing Environment

* **Device:** Hacer Laptop
* **Operating System:** Windows 11
* **Browser:** Google Chrome

## Defect Tracking

The original defect was identified and documented during the Order Placement Checklist testing process.
