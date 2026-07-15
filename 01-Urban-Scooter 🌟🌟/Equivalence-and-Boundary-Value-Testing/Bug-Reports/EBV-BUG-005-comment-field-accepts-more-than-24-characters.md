# EBV-BUG-005: Comment Field Accepts More Than 24 Characters

## Summary

The **Comment** field in the rental form allows the user to enter more than the maximum limit of 24 characters without displaying a validation error.

## Preconditions

* The Urban Scooter web application is accessible.
* The initial order form has been completed.
* The rental form is available.

## Steps to Reproduce

1. Complete the initial order form.
2. Complete the rental form.
3. Select a rental date.
4. Select a rental period.
5. Select a scooter color.
6. Enter a comment containing more than 24 characters.
7. Observe the behavior of the **Comment** field.

## Expected Result

The application should identify the input as invalid when the comment exceeds the maximum allowed limit of 24 characters.

The field should display a validation error and prevent the user from continuing until the input meets the specified character limit.

## Actual Result

The application allows the user to enter more than 24 characters in the **Comment** field without displaying a validation error.

## Impact

The application accepts input that exceeds the character limit defined in the requirements.

This may result in data exceeding the expected field length and creates an inconsistency between the specified requirements and the implemented validation.

## Testing Technique

* Boundary Value Analysis
* Input Validation

## Testing Environment

* **Device:** Hacer Laptop
* **Operating System:** Windows 11
* **Processor:** Intel Core i5
* **Browser:** Opera
* **Browser Version:** 14.7.0.7727.56

## Defect Tracking

The original defect was identified and documented during the Equivalence Partitioning and Boundary Value Analysis testing process.
