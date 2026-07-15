# OP-BUG-007: Unnecessary Second Text Line in the Order Form

## Summary

The order form contains a second line of text that is unnecessary because the input fields limit the number of characters that can be entered.

## Preconditions

* The Urban Scooter web application is accessible.
* The user can access the order form.
* The order form is available.

## Steps to Reproduce

1. Open the Urban Scooter web application.
2. Click **ORDER**.
3. Fill in the personal information form.
4. Enter a long name or other long text in one of the input fields.
5. Continue with the scooter rental order process.

## Expected Result

The form layout should be designed according to the maximum number of characters allowed in each input field.

A second line of text should not be necessary because the character limit prevents the user from entering text that would require additional space.

## Actual Result

The order form includes a second line of text even though the input fields limit the number of characters that can be entered.

As a result, the second line is unnecessary and does not provide additional value to the user.

## Impact

The unnecessary second line creates redundant space in the form layout and may affect the visual design and usability of the order form.

This creates an inconsistency between the available input length and the visual space allocated for the entered information.

## Testing Technique

* Checklist Testing
* UI Testing
* Usability Testing
* Boundary Value Analysis

## Testing Environment

* **Device:** Hacer Laptop
* **Operating System:** Windows 11
* **Browser:** Google Chrome

## Defect Tracking

The original defect was identified and documented during the Order Placement Checklist testing process.
