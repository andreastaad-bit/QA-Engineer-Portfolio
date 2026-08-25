# uTest Cross-Browser Compatibility Testing

## Overview

While using uTest as one of the freelance platforms I work with, I identified UI inconsistencies when accessing the platform through different browsers.

I initially identified the issue while using Opera and decided to perform additional exploratory testing across Chrome and Opera to evaluate cross-browser consistency, usability, and basic functionality.

The main objective was to determine whether the issue was isolated to a specific page or affected multiple areas of the platform.

## Areas Tested

| Area              | Chrome | Opera | Result      |
| ----------------- | :----: | :---: | ----------- |
| Landing Page      |   ✔️   |   ❌   | **BUG**     |
| Sign In           |   ✔️   |   ✔️  | **PASS**    |
| Profile           |   ✔️   |   ❌   | **BUG**     |
| Navigation        |   ✔️   |   ❌   | **BUG**     |
| Scrolling         |   ✔️   |   ❌   | **BUG**     |
| Links             |   ✔️   |   ✔️   | **PASS** |
| Responsive Layout |   ✔️   |   ✖️   | **BUG** |

> **Note:** Chrome was used as the baseline/reference browser for comparison. The results do not imply that Chrome is the only officially supported browser by uTest.
> 
## Browsers Tested

* **Google Chrome** — Baseline / reference browser
* **Opera** — Browser where the issue was identified

## Testing Performed

The exploratory testing focused on:

* UI layout and rendering
* Navigation
* Sign-in functionality
* Profile page
* Page scrolling
* Text readability
* Basic usability
* Cross-browser comparison

## Initial Finding

During exploratory testing, a significant UI rendering issue was identified in Opera.

Several elements on the landing page and profile page were incorrectly positioned or displayed. This resulted in poor readability and significantly affected navigation and usability.

The profile page was particularly affected because the page could not be properly scrolled, making it difficult or impossible to use the profile normally.

## Expected Result

The uTest interface should maintain a consistent and usable layout across supported browsers, with page elements properly positioned and navigation and scrolling functionality working as expected.

## Actual Result

When accessing uTest through Opera, several UI elements were incorrectly rendered or positioned. The affected pages became difficult to read and navigate, with the profile page presenting a significant scrolling issue.

**Test Date:** August 25th 2026

## Bug Report

A bug report was submitted to uTest Support with screenshots, environment information, reproduction details, and the expected vs. actual results.

**Status:** Escalated to the appropriate support/product team for investigation.
