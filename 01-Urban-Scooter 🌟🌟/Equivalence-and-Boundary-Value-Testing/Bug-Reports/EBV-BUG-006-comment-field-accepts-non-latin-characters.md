# EBV-BUG-006: Comment Field Accepts Non-Latin Characters Without Validation

## Summary

The **Comment** field allows users to enter Chinese characters, even though the requirements specify that non-Latin characters are not allowed.

The application does not display a validation error when non-Latin characters are entered.

## Preconditions

* The Urban Scooter web application is accessible.
* The user can access the order form.
* The rental form is available.

## Steps to Reproduce

1. Open the Urban Scooter web application.
2. Complete the initial order form.
3. Complete the rental form.
4. Enter the following text in the **Comment** field:

```text
伊杰伊艾马披艾勒欧
```

5. Observe the behavior of the field.

## Expected Result

The **Comment** field should be marked as invalid and highlighted in red because non-Latin characters are not allowed according to the requirements.

The user should not be allowed to continue with the form while the invalid input remains.

## Actual Result

The application allows the user to enter Chinese characters in the **Comment** field without displaying a validation error.

## Impact

The application accepts input that does not comply with the character restrictions defined in the requirements.

This may result in invalid data being submitted and creates an inconsistency between the specified input validation rules and the actual application behavior.

## Testing Technique

* Equivalence Partitioning
* Input Validation
* Character Set Validation

## Testing Environment

* **Device:** Hacer Laptop
* **Operating System:** Windows 11
* **Processor:** Intel Core i5
* **Browser:** Opera
* **Browser Version:** 14.7.0.7727.56

## Defect Tracking

The original defect was identified and documented during the Equivalence Partitioning and Boundary Value Analysis testing process.
