# EBV-BUG-001: Last Name Field Accepts More Characters Than Specified

## Summary

The **Last Name** field on the **"Place an Order"** page allows the user to enter more characters than the maximum limit specified in the requirements.

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
Velasquez Guiterrez Mendoza
```

5. Attempt to continue to the next step of the order form.

## Expected Result

The **Last Name** field should be marked as invalid and highlighted in red when the maximum character limit specified in the requirements is exceeded.

The user should not be allowed to continue to the next step of the form.

## Actual Result

The application allows the user to enter a value that exceeds the maximum character limit specified in the requirements and allows the user to continue with the order form.

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
