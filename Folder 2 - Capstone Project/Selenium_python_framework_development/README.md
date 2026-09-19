# Folder 2: Enterprise-Grade E-Commerce Automated Testing Framework

An automated end-to-end testing framework built using **Python**, **Selenium**, and **PyTest** following industry-standard software engineering design principles. This project automates core e-commerce workflows on the TutorialsNinja demo application.

---

## 📹 Project Demonstration Video

* **Watch the Walkthrough & Execution Demo:** [https://drive.google.com/file/d/1MLjJDubvikoVL5HQosFhtK2CK1G8ahbi/view?usp=sharing]

---

## 🛠️ Key Framework Features

* **Page Object Model (POM):** Strict decoupling of test scripts from page locators and business logic classes to ensure high maintainability.
* **Data-Driven Testing (DDT):** Externalized test data managed via `.csv` files for dynamic user authentication and product searches.
* **Core Action Wrappers:** Centralized Selenium commands via a base action class to enforce DRY (Don't Repeat Yourself) principles and reliable explicit waits.
* **Automated Executive Reporting:** Integrated with `pytest-html` to generate detailed, clean visual execution dashboards.
* **Failure Capture Hooks:** Automated exception handling that snaps failure screenshots on test assertion errors for fast troubleshooting.

---

## 📂 Project Directory Structure

```text
Folder 2 - Capstone Project/
│
└── Selenium_python_framework_development/
    │
    ├── configs/                  # Environment settings and base configurations
    ├── csv_data/                 # External test input data (test_inputs.csv)
    ├── failure_screenshots/      # Captured images of test failures and debugging logs
    ├── html_reports/             # Generated execution_report.html dashboards
    ├── source_pages/             # Page Object Model classes (BaseActions, LoginScreen, SearchScreen)
    ├── test_scripts/             # End-to-end test execution suites
    ├── utils/                    # Helper utilities and data parsers
    │
    ├── conftest.py               # PyTest fixtures, hooks, and configuration setup
    ├── requirements.txt          # Python package dependencies
    └── README.md                 # Framework level documentation
```
## ⚙️ Prerequisites & Setup

1. **Python Installation:** Ensure Python 3.14.7 is installed
2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
