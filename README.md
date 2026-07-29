# 🛒 QA Automation E-Commerce Project

A professional **Web UI Test Automation Framework** developed using **Python, Selenium WebDriver, and Pytest**.
The project follows the **Page Object Model (POM)** design pattern and is integrated with **Jenkins CI/CD** for automated test execution and reporting.

---

## 🚀 Technologies & Tools

* 🐍 Python
* 🌐 Selenium WebDriver
* 🧪 Pytest
* 🏗️ Page Object Model (POM)
* ⚙️ Jenkins CI/CD
* 🌙 Chrome Headless Execution
* 📊 JUnit Test Reporting
* 📦 WebDriver Manager
* 💻 VS Code

---

## 📌 Project Features

✅ Automated browser testing with Selenium
✅ Page Object Model architecture
✅ Pytest test framework integration
✅ Chrome Headless browser support
✅ Jenkins automated test execution
✅ JUnit XML test report generation
✅ Clean and maintainable test structure
✅ Configuration management

---

# 📂 Project Structure

```
QA-Automation-Ecommerce
│
├── config
│   └── config.py
│
├── pages
│   └── Page Object classes
│
├── tests
│   └── Test scenarios
│
├── utils
│   └── Helper functions
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── Jenkinsfile
└── README.md
```

---

# 🧩 Test Architecture

The project uses the **Page Object Model (POM)** approach.

Benefits:

* Better code organization
* Reusable page components
* Easier maintenance
* Separation between test logic and page actions

Example flow:

```
Test Case
    |
    ↓
Page Object
    |
    ↓
Selenium WebDriver
    |
    ↓
Web Application
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to project folder:

```bash
cd QA-Automation-Ecommerce
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate environment:

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running Tests

Run tests locally:

```bash
pytest
```

---

# 📊 Test Reporting

Generate JUnit XML test report:

```bash
pytest --junitxml=test-results.xml
```

The generated report can be published through Jenkins.

---

# 🔄 Jenkins CI/CD Integration

The project is integrated with Jenkins.

Pipeline workflow:

```
Developer
    |
    ↓
GitHub Repository
    |
    ↓
Jenkins Build
    |
    ↓
Install Dependencies
    |
    ↓
Run Selenium Tests
    |
    ↓
Generate Test Reports
    |
    ↓
Publish Results
```

Jenkins executes tests automatically and provides:

* Test execution status
* Passed / Failed test counts
* Test result reports

---

# 🌐 Browser Configuration

Tests are executed using:

```
Google Chrome Headless Mode
```

Advantages:

* Faster execution
* Suitable for CI/CD environments
* No browser UI required

---

# 🧪 Example Test Scenario

Example automated flow:

```
Open Website
      ↓
Navigate Page
      ↓
Perform User Actions
      ↓
Validate Results
      ↓
Generate Test Report
```

---

# 📈 Skills Demonstrated

This project demonstrates experience with:

* Test Automation
* Selenium WebDriver
* Python Programming
* Pytest Framework
* Object-Oriented Programming
* Page Object Model
* CI/CD Concepts
* Jenkins Automation
* Test Reporting

---

# 👨‍💻 Author

**Alper Türk**

QA Automation Engineer Candidate

Skills:

* Selenium
* Pytest
* Python
* Jenkins
* Postman
* Newman
* API Testing

---
