# Test Scenarios — uTest Cross-Browser Compatibility

## Objective

Verify the consistency, usability, and basic functionality of the uTest platform across Google Chrome and Opera, with particular focus on UI rendering, navigation, scrolling, and profile usability.

**Reference Browser:** Google Chrome
**Affected Browser:** Opera

---

## TS-01 — Landing Page UI Rendering

**Objective:** Verify that the landing page is correctly rendered across browsers.

**Preconditions:**

* User has access to the uTest website.
* Chrome and Opera are installed.

**Steps:**

1. Open the uTest landing page in Chrome.
2. Observe the page layout, text, buttons, and navigation elements.
3. Open the same page in Opera.
4. Compare the layout and visual elements between browsers.

**Expected Result:**
The landing page should maintain a consistent and properly organized layout across both browsers.

---

## TS-02 — Landing Page Text Readability

**Objective:** Verify that all relevant text is readable and properly positioned.

**Steps:**

1. Open the landing page in Chrome.
2. Review headings, labels, buttons, and other visible text.
3. Repeat the same steps in Opera.
4. Compare text positioning, size, spacing, and readability.

**Expected Result:**
Text should be clearly visible, properly positioned, and readable without overlapping or unexpected formatting.

---

## TS-03 — Sign-In Page UI Consistency

**Objective:** Verify that the Sign-In page maintains a consistent UI across browsers.

**Steps:**

1. Open the uTest Sign-In page in Chrome.
2. Review the layout and form elements.
3. Open the same page in Opera.
4. Compare the layout and visual elements.

**Expected Result:**
The Sign-In page should have a consistent layout and correctly positioned elements in both browsers.

---

## TS-04 — Sign-In Functionality

**Objective:** Verify that users can access the platform successfully from both browsers.

**Steps:**

1. Open uTest in Chrome.
2. Navigate to Sign In.
3. Enter valid credentials.
4. Sign in.
5. Repeat the process in Opera.

**Expected Result:**
The user should be able to successfully sign in and access the platform in both browsers.

---

## TS-05 — Profile Page UI Rendering

**Objective:** Verify that the user profile is correctly rendered after authentication.

**Steps:**

1. Sign in using Chrome.
2. Navigate to the user profile.
3. Observe the layout and positioning of profile elements.
4. Repeat the same steps in Opera.
5. Compare both versions.

**Expected Result:**
The profile page should display all elements correctly and maintain a usable layout across browsers.

---

## TS-06 — Profile Page Scrolling

**Objective:** Verify that users can scroll through the complete profile page.

**Steps:**

1. Sign in to uTest.
2. Navigate to the profile page.
3. Scroll from the top to the bottom of the page.
4. Repeat the test in Chrome and Opera.

**Expected Result:**
The user should be able to scroll through the entire profile page without the page becoming unresponsive or preventing access to content.

---

## TS-07 — Main Navigation

**Objective:** Verify that the main navigation remains usable across browsers.

**Steps:**

1. Sign in to uTest.
2. Navigate through the available main navigation options in Chrome.
3. Repeat the same actions in Opera.
4. Observe the position and usability of navigation elements.

**Expected Result:**
Navigation elements should be correctly positioned and users should be able to access the available sections without UI-related issues.

---

## TS-08 — Page Layout During Navigation

**Objective:** Verify that the UI remains stable when navigating between different sections.

**Steps:**

1. Sign in to uTest.
2. Navigate from the main page to the profile.
3. Navigate to another available section.
4. Return to the profile.
5. Repeat the process in Chrome and Opera.

**Expected Result:**
The layout should remain stable and correctly rendered after navigating between sections.

---

## TS-09 — Browser Window / Viewport Behavior

**Objective:** Verify that the UI remains usable when the browser window size changes.

**Steps:**

1. Open uTest in Chrome.
2. Resize the browser window.
3. Observe the behavior of the page layout.
4. Repeat the test in Opera.
5. Compare the behavior between browsers.

**Expected Result:**
Page elements should adapt to the available viewport without overlapping, becoming inaccessible, or significantly affecting usability.

---

## TS-10 — Cross-Browser Usability Comparison

**Objective:** Evaluate the overall usability of the platform after completing the previous scenarios.

**Steps:**

1. Perform the same basic workflow in Chrome and Opera:

   * Open the landing page.
   * Navigate to Sign In.
   * Authenticate.
   * Access the profile.
   * Navigate between available sections.
   * Scroll through the pages.
2. Compare the overall experience between browsers.

**Expected Result:**
The core user journey should remain functional and usable across both browsers. Significant differences affecting navigation, readability, or functionality should be documented as defects.

---

## Test Execution Status

| ID    | Scenario                           | Chrome | Opera | Status |
| ----- | ---------------------------------- | :----: | :---: | ------ |
| TS-01 | Landing Page UI Rendering          |  PASS  |  FAIL | 🔴     |
| TS-02 | Landing Page Text Readability      |  PASS  |  FAIL | 🔴     |
| TS-03 | Sign-In Page UI Consistency        |  PASS  |  FAIL | 🔴     |
| TS-04 | Sign-In Functionality              |  PASS  |  PASS | 🟢     |
| TS-05 | Profile Page UI Rendering          |  PASS  |  FAIL | 🔴     |
| TS-06 | Profile Page Scrolling             |  PASS  |  FAIL | 🔴     |
| TS-07 | Main Navigation                    |  PASS  |  FAIL | 🔴     |
| TS-08 | Page Layout During Navigation      |  PASS  |  FAIL | 🔴     |
| TS-09 | Browser Window / Viewport Behavior |  PASS  |  FAIL | 🔴     |
| TS-10 | Cross-Browser Usability Comparison |  PASS  |  FAIL | 🔴     |

### Status Legend

* 🟢 **PASS** — Expected behavior observed.
* 🔴 **FAIL** — Behavior does not meet the expected result.
* 🟡 **TBD** — Test not executed yet.
