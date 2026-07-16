
# 🛴 Urban Scooter — End-to-End QA Testing Project

> 🧪 A comprehensive QA project covering **Web, Mobile, and API Testing** for the Urban Scooter transportation platform.

This project documents the end-to-end quality assurance testing performed across the Urban Scooter application ecosystem.

The testing focused on validating customer and courier workflows, identifying defects, and documenting test execution results and evidence.

---

## 🎯 Testing Scope

The project covers:

🌐 **Web Application Testing**
📱 **Mobile Application Testing**
🔌 **API Testing**
🔄 **End-to-End Testing**
✅ **Functional Testing**
📋 **Checklist Testing**
🔍 **Exploratory Testing**
🧮 **Boundary Value Analysis**
🧩 **Equivalence Partitioning**
🔀 **State Transition Testing**
🔗 **Cross-Platform Testing**

---

## 📂 Project Structure

```text
01-Urban-Scooter/
│
├── 📋 order-placement-checklist/
│   ├── README.md
│   ├── 📊 Test Cases & Execution Results
│   └── 🐞 bugs/
│       ├── OP-BUG-001-...
│       ├── OP-BUG-002-...
│       └── OP-BUG-012-...
│
├── 🧮 equivalence-and-boundary-value-testing/
│   ├── README.md
│   ├── 📊 Test Cases
│   └── 🐞 Bug Reports
│
├── 📱 mobile-testing/
│   ├── README.md
│   └── 📄 Mobile Test Documentation
│
└── 🔌 API Testing & Supporting Documentation
```

---

## 🌐 Web Testing

The web application was tested across different functional areas, including:

📝 Order placement
✅ Form validation
📌 Required field validation
📅 Rental date validation
🚫 Invalid input handling
💾 Data persistence
🎫 Order confirmation
🔎 Order status verification
🔄 Order lifecycle testing

The testing identified defects related to incomplete validation, invalid rental dates, order creation, order status management, and synchronization between application states.

---

## 📱 Mobile Testing

The mobile application was tested using an Android emulator to validate courier-related workflows and interactions with customer orders.

Testing included:

🚴 Courier access
📦 Order acceptance
❌ Order cancellation
🔄 Order status changes
🏁 Rental completion
🔀 Order lifecycle transitions

The mobile testing was combined with web testing to validate the interaction between the customer and courier sides of the platform.

---

## 🔌 API Testing

API testing was used to support the end-to-end testing process and prepare the data required for specific test scenarios.

🛠️ **Postman** was used to create courier information and support testing between the web application and the mobile courier application.

---

## 📚 Test Documentation

The project contains:

📊 Test cases
📋 Test execution results
✅ Checklists
🐞 Bug reports
📸 Testing evidence
📄 Supporting QA documentation

Test cases and execution results are maintained in Excel files, while individual defects are documented in Markdown files.

Each bug report includes:

* 📌 Summary
* ⚙️ Preconditions
* 🔢 Steps to reproduce
* ✅ Expected result
* ❌ Actual result
* 💥 Impact
* 🧪 Testing technique
* 💻 Testing environment
* 🗂️ Defect tracking information

---

## 🖥️ Testing Environment

### 🌐 Web Application

| Component           | Details      |
| ------------------- | ------------ |
| 🌍 Browser          | Opera        |
| 💻 Operating System | Windows 11   |
| 🖥️ Device          | Hacer Laptop |

### 📱 Mobile Application

| Component    | Details |
| ------------ | ------- |
| 📱 Emulator  | Pixie 5 |
| ⚙️ API Level | 37      |

### 🔌 API Testing

| Tool        |
| ----------- |
| 🛠️ Postman |

---

## 🔄 Order Lifecycle Tested

The main workflow tested was:

```text
👤 Customer
      ↓
📝 Order Placement
      ↓
🛴 Rental Configuration
      ↓
✅ Order Confirmation
      ↓
🚴 Courier Acceptance
      ↓
🔄 Order Status Updates
      ↓
🏁 Rental Completion
```

Testing the complete flow made it possible to identify not only isolated defects, but also issues related to communication and state synchronization between different parts of the application.

---

## 🧠 QA Skills Demonstrated

### 🧪 Testing

* Manual QA Testing
* Web Testing
* Mobile Testing
* API Testing
* Functional Testing
* End-to-End Testing
* Checklist Testing
* Exploratory Testing

### 🔍 Test Design Techniques

* Boundary Value Analysis
* Equivalence Partitioning
* Input Validation
* State Transition Testing

### 🛠️ Tools

* Postman
* Android Emulator
* Microsoft Excel
* Git
* GitHub

### 📄 Documentation

* Test Case Design
* Test Execution
* Bug Reporting
* Test Evidence
* QA Documentation

---

> 💡 This project demonstrates a structured approach to QA testing across multiple platforms, combining test design techniques, functional validation, API support, mobile testing, and detailed defect documentation.
