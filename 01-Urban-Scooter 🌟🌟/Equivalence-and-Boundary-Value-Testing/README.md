
# Equivalence Partitioning and Boundary Value Analysis

## Overview

This section of my QA portfolio presents the test cases performed using two fundamental test design techniques:

* **Equivalence Partitioning**
* **Boundary Value Analysis**

The testing was performed on the **Urban Scooter web application**, focusing primarily on the order placement and scooter rental flows.

The objective was to identify valid and invalid input classes, verify the behavior of field validations, and test how the application responds when users enter values at or beyond the specified limits.

## Testing Scope

The following areas were tested:

* Order placement form
* Customer information fields
* Phone number validation
* Address field validation
* Rental form
* Date validation
* Comment field validation
* Character restrictions
* Maximum character limits
* Required fields

## Testing Techniques

### Equivalence Partitioning

Equivalence Partitioning was used to divide input data into groups that are expected to behave similarly.

Examples of tested input classes included:

* Valid text input
* Empty fields
* Invalid characters
* Non-Latin characters
* Special characters
* Valid and invalid dates
* Values that comply with the specified requirements
* Values that do not comply with the specified requirements

### Boundary Value Analysis

Boundary Value Analysis was used to test values at and around the limits defined in the requirements.

Examples included:

* Maximum allowed number of characters
* Maximum allowed number of digits
* Dates from the past
* Dates from previous years
* Values exceeding the specified limits

The purpose was to verify whether the application correctly validates values at the boundaries and rejects values outside the allowed range.

## Test Environment

* **Device:** Hacer Laptop
* **Operating System:** Windows 11
* **Processor:** Intel Core i5
* **Browser:** Opera
* **Browser Version:** 14.7.0.7727.56

## Test Documentation

The complete test cases and results are available in the following Excel file:

📊 **[Equivalence and Boundary Value Testing Checklist](./equivalence-and-boundary-value-tests.xlsx)**

The spreadsheet contains the test cases performed during the testing process, including the tested input, expected results, actual results, and test status.

## Defect Reports

During the testing process, 9 defects were identified and documented.

The detailed bug reports can be found in the following folder:

🐞 **[View Bug Reports](./Bug-Reports/)**

The identified defects included issues related to:

* Maximum character limits
* Maximum phone number length
* Ambiguous input requirements
* Required field validation
* Invalid character validation
* Special character validation
* Date validation
* Acceptance of dates from previous years

## Key Findings

The testing process identified several inconsistencies between the requirements and the application's actual behavior.

The main findings were related to:

* Input limits not being properly enforced.
* Invalid characters being accepted.
* Required fields allowing empty values.
* Dates outside the allowed range being accepted.
* Ambiguity in the requirements regarding the allowed position of the `+` symbol in phone numbers.

These findings demonstrate the importance of testing not only typical valid inputs, but also invalid data and values located at or beyond defined boundaries.

## Conclusion

Applying Equivalence Partitioning and Boundary Value Analysis helped identify validation issues that may not be detected through standard positive testing alone.

These techniques provided a structured approach to testing input fields and verifying whether the application behavior matched the defined requirements.

This testing process also reinforced the importance of:

* Testing both valid and invalid input classes.
* Testing values at the boundaries of allowed ranges.
* Comparing implemented behavior against documented requirements.
* Identifying ambiguities or gaps in the requirements.
* Documenting defects with clear steps to reproduce and expected versus actual results.
