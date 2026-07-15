# EBV-BUG-008: Date Field Accepts Dates from the Past

## Summary

The **Date** field in the rental form allows the user to select or enter a date prior to the current date, even though the requirements specify that past dates should not be accepted.

## Preconditions

* The Urban Scooter web application is accessible.
* The user can access the order form.
* The rental form is available.

## Steps to Reproduce

1. Open the Urban Scooter web application.
2. Complete the initial order form.
3. Navigate to the rental form.
4. Enter or select a date prior to the current date in the **Date** field.
5. Attempt to continue with the rental process.

## Expected Result

The application should reject dates prior to the current date.

The **Date** field should display a validation error and prevent the user from continuing with the rental process until a valid date is entered.

## Actual Result

The application accepts a date prior to the current date without displaying a validation error.

The user is able to continue with the rental process.

## Impact

The application allows users to select a rental date that has already passed.

This may result in invalid rental data and creates an inconsistency between the requirements and the implemented date validation.

## Testing Technique

* Boundary Value Analysis
* Input Validation
* Date Validation

## Testing Environment

* **Device:** Hacer Laptop
* **Operating System:** Windows 11
* **Processor:** Intel Core i5
* **Browser:** Opera
* **Browser Version:** 14.7.0.7727.56

## Defect Tracking

The original defect was identified and documented during the Equivalence Partitioning and Boundary Value Analysis testing process.
