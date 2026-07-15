
# Mobile Testing

## Overview

This section of my QA portfolio presents the mobile testing performed on the **Urban Scooter** application using an Android emulator.

The objective was to verify the application's functionality, usability, notifications, session management, offline behavior, input validation, and stability across different user scenarios.

## Testing Scope

The mobile testing included the following areas:

* Courier login and account management
* Order acceptance and order management
* Push notifications
* Notifications when the application is running in the background
* Time-based order notifications
* Offline behavior and connection error handling
* User interface validation
* Input validation
* Session management
* Switching between courier accounts
* Application stability
* Application behavior after restarting the emulator
* Long-duration application usage

## Test Environment

* **Device:** Pixel 5
* **Operating System:** Android
* **API Level:** 37
* **Environment:** Android Emulator

## Testing Tools

* Android Emulator
* Pixel 5 virtual device
* Postman
* Urban Scooter web application

## Test Documentation

The complete mobile test cases and their results are available in the following Excel file:

📱 **[Mobile Testing Checklist](./mobile-testing-checklist.xlsx)**

The spreadsheet contains the test scenarios performed during the mobile testing process, including the tested functionality, expected results, actual results, and test status.

## Defect Reports

During the testing process, 14 defects were identified and documented.

The detailed bug reports can be found in the following folder:

🐞 **[View Mobile Bug Reports](./Mobile-Bug-Reports/)**

The identified defects included issues related to:

* Missing notifications
* Incorrect notification behavior
* Duplicate order display
* Offline connection handling
* Incorrect UI text
* Application crashes
* Session management
* Application stability
* Input validation
* Non-Latin characters
* Password validation
* Error handling
* Background application behavior

## Key Findings

The testing process identified several issues affecting the application's functionality, stability, and user experience.

The main findings included:

* Notifications were not consistently displayed when expected.
* The application did not always handle offline scenarios correctly.
* Some UI elements did not match the expected text.
* Switching between courier accounts could lead to application crashes.
* In some cases, the application remained in an unusable state after restarting.
* The application accepted input that did not comply with the expected validation rules.
* Technical errors were displayed without providing a clear user-friendly explanation.

## Conclusion

The mobile testing process helped evaluate the Urban Scooter application across different functional and non-functional scenarios.

The testing focused not only on verifying the expected behavior of individual features, but also on observing how the application behaved under different conditions, including:

* Background execution
* Loss of internet connectivity
* Repeated login and logout sessions
* Switching between users
* Extended application usage
* Invalid input
* Application and emulator restarts

The identified defects were documented with clear steps to reproduce, expected results, actual results, impact, and testing environment information.

This testing process demonstrates the importance of validating mobile applications under both normal and unexpected conditions to identify issues that may affect the user experience and application stability.
