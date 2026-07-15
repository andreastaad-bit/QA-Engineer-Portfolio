# EBV-BUG-003: Phone Number Field Does Not Clearly Define the Allowed Position of the Plus Symbol

## Summary

The requirements indicate that the `+` symbol can be used in the **Phone Number** field, but they do not specify that it can only be placed at the beginning of the number.

When the user attempts to enter the `+` symbol in the middle of the phone number, the application does not allow the character to be entered.

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

5. Enter the following value in the **Phone Number** field:

```text
4758+958789
```

6. Observe the behavior of the Phone Number field.

## Expected Result

The requirements should clearly specify the allowed position of the `+` symbol in the Phone Number field.

If the `+` symbol is only allowed at the beginning of the phone number, this restriction should be clearly defined in the requirements or communicated through appropriate field validation.

## Actual Result

The application does not allow the user to enter the `+` symbol in the middle of the phone number.

However, the requirements only indicate that the `+` symbol can be used and do not specify that it is restricted to the beginning of the number.

## Impact

The lack of clarity in the requirements may lead to ambiguity regarding the valid format of phone numbers.

Users and testers may interpret the requirement differently because the allowed position of the `+` symbol is not explicitly defined.

## Testing Technique

* Boundary Value Analysis
* Input Validation
* Requirements Validation

## Testing Environment

* **Device:** Hacer Laptop
* **Operating System:** Windows 11
* **Processor:** Intel Core i5
* **Browser:** Opera
* **Browser Version:** 14.7.0.7727.56

## Defect Tracking

The original defect was identified and documented during the Equivalence Partitioning and Boundary Value Analysis testing process.
