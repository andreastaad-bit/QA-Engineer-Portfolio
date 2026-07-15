# EBV-BUG-009: Date Field Accepts Dates from Previous Years

## Summary

The **Date** field in the **"Rental"** screen allows users to enter dates from previous years, even though the requirements specify that dates from previous years should not be allowed.

## Preconditions

* The Urban Scooter web application is accessible.
* The user can access the order form.
* The rental form is available.

## Steps to Reproduce

1. Open the Urban Scooter web application.
2. Complete the initial order form.
3. Complete the rental form.
4. Enter a date from a previous year in the **Date** field.

For example:

```text
11.09.25
```

5. Observe the field validation.
6. Attempt to continue with the rental process.

## Expected Result

The **Date** field should be highlighted in red and display a validation error because dates from previous years are not allowed according to the requirements.

The user should not be allowed to continue with the rental process.

## Actual Result

The application allows the user to enter dates from previous years without displaying a validation error.

The user can continue with the rental process.

## Impact

The application accepts dates that do not comply with the date restrictions defined in the requirements.

This may result in invalid rental information and creates an inconsistency between the specified requirements and the implemented date validation.

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
