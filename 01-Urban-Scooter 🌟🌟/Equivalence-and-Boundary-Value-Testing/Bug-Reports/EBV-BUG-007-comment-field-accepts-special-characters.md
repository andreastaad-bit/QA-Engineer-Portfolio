# EBV-BUG-007: Comment Field Accepts Special Characters

## Summary

The **Comment** field in the rental form accepts special characters, even though the requirements specify that these characters are not allowed.

The application does not display a validation error and allows the user to continue with the rental process.

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
no me gu$stan tus empanadas
```

5. Observe the behavior of the field.
6. Attempt to continue with the scooter rental process.

## Expected Result

The **Comment** field should be marked as invalid and highlighted in red because special characters are not allowed according to the requirements.

The user should not be allowed to continue with the rental process while the invalid input remains.

## Actual Result

The application accepts the special character `$` in the **Comment** field without displaying a validation error.

The user can continue with the scooter rental process.

## Impact

The application accepts input that does not comply with the character restrictions defined in the requirements.

This may result in invalid data being submitted and creates an inconsistency between the specified validation rules and the actual application behavior.

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
