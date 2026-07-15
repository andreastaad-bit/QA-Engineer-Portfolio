# OP-BUG-003: Rental Date Field Accepts Dates from Previous Years

## Summary

The rental form allows the user to schedule a scooter rental for dates from previous years, including dates that are no longer available.

## Preconditions

* The Urban Scooter web application is accessible.
* The user can access the order form.
* The rental form is available.

## Steps to Reproduce

1. Open the Urban Scooter web application.
2. Click **ORDER**.
3. Complete the order form with valid information.
4. Click **NEXT**.
5. Select a rental date from a previous year.

For example, select a date from **2024**.

6. Continue with the rental process.

## Expected Result

The application should not allow the user to schedule a scooter rental for dates from previous years.

The date selection should restrict the user to valid and available rental dates, and dates from previous years should be rejected.

## Actual Result

The application allows the user to select rental dates from previous years.

Dates from **2024** can be selected, and no restriction or validation error is displayed.

## Impact

The application allows users to schedule scooter rentals for dates that have already passed.

This may result in invalid rental reservations and creates an inconsistency between the expected date restrictions and the implemented functionality.

## Testing Technique

* Checklist Testing
* Input Validation
* Date Validation
* Boundary Value Analysis

## Testing Environment

* **Device:** Hacer Laptop
* **Operating System:** Windows 11
* **Browser:** Google Chrome

## Defect Tracking

The original defect was identified and documented during the Order Placement Checklist testing process.
