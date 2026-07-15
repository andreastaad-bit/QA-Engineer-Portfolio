# EBV-BUG-002: Phone Number Field Accepts More Than 13 Digits

## Summary

The **Phone Number** field allows users to enter more than 13 digits without displaying a validation error.

According to the requirements, values exceeding the maximum allowed length should be rejected.

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

5. Enter 13 or more digits in the **Phone Number** field.
6. Attempt to continue with the order form.

## Expected Result

The **Phone Number** field should be marked as invalid and highlighted in red when the maximum allowed number of digits is exceeded.

The user should not be allowed to continue with the form.

## Actual Result

The application allows the user to enter more than 13 digits in the **Phone Number** field without displaying a validation error.

The user is also able to continue with the order form.

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
