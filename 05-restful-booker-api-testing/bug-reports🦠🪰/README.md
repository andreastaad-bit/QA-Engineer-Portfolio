# Restful Booker API — Bug Findings

## Overview

During the API testing of the Restful Booker API, several issues were identified across authentication, booking creation, update, and deletion workflows.

The test cases were executed using Postman, and failed test cases are directly linked to their corresponding Jira bug reports.

This document provides a consolidated summary of the defects identified during testing.

---

## Bug Findings

| Test Case | Bug Report |
|---|---|
| **RBT-004 — PUT request to update an existing booking** | **RBB-01 — PUT request intermittently returns 400 or 403 when updating an existing booking** |
| **RBT-006 — POST request with empty body** | **RBB-02 — POST method request with empty body** |
| **RBT-005 — Authentication with invalid credentials** | **RBB-03 — Unexpected response with the use of invalid credentials on the body** |
| **RBT-002 — Create booking with valid information** | **RBB-04 — Error on HTTP code when creating a booking** |
| **RBT-003 — Delete an existing booking** | **RBB-05 — Wrong HTTP code when deleting a booking** |

---

## Findings Summary

### RBB-01 — PUT request intermittently returns 400 or 403

**Area:** Booking Update  
**Method:** `PUT`  
**Severity:** [HIGH]  
**Status:** [HIGH]

The update request intermittently returns an unexpected `400` or `403` HTTP status code when attempting to update an existing booking with valid information.

---

### RBB-02 — POST request with empty body

**Area:** Booking Creation  
**Method:** `POST`  
**Severity:** [MEDIUM]  
**Status:** [MEDIUM]

The API accepts a `POST` request with an empty request body and returns an unexpected response instead of properly handling the missing request data.

---

### RBB-03 — Unexpected response with invalid credentials

**Area:** Authentication  
**Method:** `POST`  
**Severity:** [LOW]  
**Status:** [MEDIUM]

When invalid authentication information is submitted, the API returns an unexpected response that does not match the expected behavior for invalid credentials.

---

### RBB-04 — Incorrect HTTP status when creating a booking

**Area:** Booking Creation  
**Method:** `POST`  
**Severity:** [LOW]  
**Status:** [LOW]

When creating a booking with valid information, the API returns an unexpected HTTP status code instead of the expected successful response.

---

### RBB-05 — Incorrect HTTP status when deleting a booking

**Area:** Booking Deletion  
**Method:** `DELETE`  
**Severity:** [MEDIUM]  
**Status:** [MEDIUM]

When deleting an existing booking, the API returns an unexpected HTTP status code instead of the expected successful response.

---

## Testing Summary

| Metric | Result |
|---|---:|
| Test cases executed | 10 |
| Passed | 5 |
| Failed | 5 |
| Bugs identified | 5 |
| API tool | Postman |
| API | Restful Booker |

---

## Defect Tracking

All identified defects were documented and tracked in Jira.

The corresponding Jira issues are linked directly from the failed test cases in the test case documentation.
