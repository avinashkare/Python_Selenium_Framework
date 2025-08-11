# Python Selenium Framework

## Overview
This is a **Python Selenium Automation Framework** built using the **Page Object Model (POM)** design pattern with data-driven testing from JSON files.  
The framework is designed to be modular, maintainable, and scalable for UI test automation.

## Features
- **Page Object Model (POM)**: Separates test logic from page elements for better maintainability.
- **Data-Driven Testing**: Test data is stored in `.json` files under the `test_data` directory and dynamically loaded during test execution.
- **Pytest Support**: Simple and powerful test execution using pytest.
- **Cross-Browser Testing**: Supports Chrome, Firefox, and Edge browsers.
- **Parallel Execution**: Tests can be run in parallel using `pytest-xdist`.
- **HTML Reports**: Generates detailed HTML reports using `pytest-html`.
- **Shadow DOM Handling**: Supports accessing elements inside Shadow DOM.
- **Jenkins Integration**: Configured to run tests via Jenkins with browser choice as a parameter.

## Project Structure
```
Python_Selenium_Framework/
│
├── page_objects/               # Contains Page Object classes
│   ├── dashboard_page_objects.py
│   ├── shadow_dom_page_objects.py
│   └── ...
│
├── tests/                      # Contains all test scripts
│   ├── test_form_validation.py
│   ├── test_shadow_dom_validations.py
│   └── reports/                # HTML test reports
│
├── test_data/                  # JSON test data files
│   ├── test_form_validation.json
│   └── ...
│
├── conftest.py                  # Pytest fixtures and hooks (e.g., browser setup, screenshots)
├── pytest.ini                   # Pytest configuration
└── requirements.txt             # Project dependencies
```

## Data-Driven Testing
Test data is stored in JSON files under the `test_data` directory.

Example: `test_form_validation.json`
```json
{
    "form_data": {
        "username": "testuser",
        "password": "password123",
        "email": "test@example.com"
    }
}
```

Usage in test script:
```python
import json
import os

test_data_path = os.path.join(os.path.dirname(__file__), "../test_data/test_form_validation.json")
with open(test_data_path) as json_file:
    data = json.load(json_file)

username = data["form_data"]["username"]
```

## Running Tests
Run all tests:
```bash
pytest -s -v
```

Run tests with specific browser:
```bash
pytest -s -v --browser_type chrome
```

Run tests in parallel:
```bash
pytest -s -n 3 --browser_type firefox
```

Generate HTML report:
```bash
pytest -s --html=reports/report.html
```

## Jenkins Integration
- Create a Jenkins Freestyle Project
- Pull code from GitHub repository
- Add an "Execute Windows batch command" build step:
```bash
cd tests
py -m pytest -s -n 3 --html=reports/report.html --browser_type chrome
```
- Configure "Choice Parameter" for selecting browser:
  - Parameter name: `browser`
  - Choices: `chrome`, `firefox`, `edge`

## Screenshot on Failure
The `pytest_runtest_makereport` hook in `conftest.py` captures screenshots on failure and attaches them to the HTML report.

---
**Author:** Avinash Kare
**GitHub:** [Python_Selenium_Framework](https://github.com/avinashkare/Python_Selenium_Framework)
