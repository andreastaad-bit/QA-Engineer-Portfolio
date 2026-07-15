# OP-BUG-005: Metro Station Field Breaks the Page When an Invalid Station Is Entered

## Summary

The **Metro Station** field does not properly handle an address that does not correspond to one of the available metro stations. Entering an invalid station value causes the page to break instead of displaying a validation error.

## Preconditions

* The Urban Scooter web application is accessible.
* The user can access the order form.
* The order form is available.

## Steps to Reproduce

1. Open the Urban Scooter web application.
2. Click **ORDER**.
3. Fill in the personal information form.
4. Enter an invalid address or station name that is not included in the available metro station options.
5. Attempt to continue with the order process.

## Expected Result

The application should validate the entered information.

The **Metro Station** field should be highlighted in red and display an error message indicating that the entered station or address is invalid and must be corrected.

The page should remain functional.

## Actual Result

The page breaks after an invalid station or address is entered in the **Metro Station** field.

No proper validation message is displayed, and the user cannot continue the order process normally.

## Impact

The application does not properly handle invalid input in the **Metro Station** field.

This may interrupt the order placement process and prevent users from continuing when incorrect station information is entered.

## Testing Technique

* Checklist Testing
* Input Validation
* Negative Testing
* Error Handling Testing

## Testing Environment

* **Device:** Hacer Laptop
* **Operating System:** Windows 11
* **Browser:** Google Chrome

## Defect Tracking

The original defect was identified and documented during the Order Placement Checklist testing process.
