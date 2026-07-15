# OP-BUG-002: Order Form Data Is Lost After Returning to the Home Page

## Summary

The information entered in the order form is cleared when the user returns to the home page and opens the order form again.

## Preconditions

* The Urban Scooter web application is accessible.
* The user can access the order form.
* The order form is available.

## Steps to Reproduce

1. Open the Urban Scooter web application.
2. Click **ORDER**.
3. Enter valid information in the order form.
4. Return to the home page by clicking the application logo.
5. Click **ORDER** again.

## Expected Result

The information previously entered in the order form should be preserved when navigating between pages.

The user should be able to return to the order form and continue with the previously entered information.

## Actual Result

All previously entered information is cleared after the user returns to the home page.

When the user opens the order form again, the fields are empty.

## Impact

The application loses user-entered order information when navigating between pages.

This may cause data loss, inconvenience for the user, and requires the user to re-enter all previously provided information.

## Testing Technique

* Checklist Testing
* Data Persistence Testing
* Navigation Testing

## Testing Environment

* **Device:** Hacer Laptop
* **Operating System:** Windows 11
* **Browser:** Google Chrome

## Defect Tracking

The original defect was identified and documented during the Order Placement Checklist testing process.
