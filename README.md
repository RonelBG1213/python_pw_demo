# Python Playwright Test Framework

A comprehensive test automation framework built with Python and Playwright for web application testing.

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Test Organization](#test-organization)
- [Reporting](#reporting)
- [Advanced Features](#advanced-features)
- [Utilities](#utilities)
- [Contributing](#contributing)

## ✨ Features

- **Page Object Model (POM)** architecture for maintainable test code
- **Playwright** integration for cross-browser testing (Chromium, Firefox, Safari)
- **Parallel test execution** for faster test runs
- **Comprehensive reporting** with HTML reports and screenshots
- **Test tracing** for debugging failed tests
- **PDF assertion utilities** for document validation
- **Excel file handling** capabilities
- **JSON configuration** management
- **Automatic screenshot capture** on test failures
- **Flexible test markers** for test categorization
- **Built-in retry mechanism** for flaky tests

## 📁 Project Structure

```
python_pw_demo/
├── conftest.py                 # Pytest configuration and fixtures
├── pytest.ini                 # Pytest settings and markers
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── main/                       # Core framework code
│   ├── envi/                   # Environment configurations
│   │   └── urls.json          # URL configurations for different environments
│   ├── fixtures/               # Test fixtures and base classes
│   │   ├── baseActions.py     # Base action methods
│   │   ├── navigation.py      # Navigation utilities
│   │   └── pageManager.py     # Page object manager
│   ├── functions/             # Business logic functions
│   │   └── dashboard.py       # Dashboard-specific functions
│   ├── pages/                 # Page object classes
│   │   └── dashboard_page.py  # Dashboard page elements
│   ├── resources/             # Test data and resources
│   │   └── sample_report.pdf  # Sample files for testing
│   └── utils/                 # Utility modules
│       ├── excel_handler.py   # Excel file operations
│       ├── json_handler.py    # JSON file operations
│       └── pdf_assert.py      # PDF assertion utilities
├── tests/                     # Test cases
│   ├── regression/            # Regression test suites
│   │   └── homepage/
│   │       └── test_dashboard.py
│   └── smoke/                 # Smoke test suites
│       ├── smoke_test.py
│       └── test_pdf_assertions_example.py
├── reports/                   # Test execution reports
│   ├── report.html           # HTML test report
│   ├── screenshots/          # Failure screenshots
│   └── trace/               # Playwright traces
└── test_venv/               # Virtual environment (optional)
```

## 🔧 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd python_pw_demo
   ```

2. **Create and activate virtual environment** (recommended)
   ```bash
   python -m venv test_venv
   source test_venv/bin/activate  # On Windows: test_venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers**
   ```bash
   playwright install
   ```

## ⚙️ Configuration

### Environment URLs
Edit `main/envi/urls.json` to configure your application URLs:
```json
{
    "baseURL": "https://your-app.com/",
    "dashboardURL": "https://your-app.com/dashboard",
    "loginURL": "https://your-app.com/login"
}
```

### Pytest Configuration
The framework is configured via `pytest.ini`:
- **Default browser**: Chromium
- **Parallel execution**: 2 workers
- **HTML reporting**: Enabled
- **Logging**: Configured with timestamps
- **Reruns**: Disabled by default (can be enabled)

## 🎯 Usage

### Basic Test Execution

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/smoke/smoke_test.py

# Run tests with specific markers
pytest -m smoke
pytest -m regression
pytest -m practice

# Run tests in headed mode (visible browser)
pytest --headed

# Run with trace enabled for debugging
pytest --enable-trace

# Run specific test with verbose output
pytest -v tests/regression/homepage/test_dashboard.py
```

### Advanced Test Execution

```bash
# Run tests in parallel with custom worker count
pytest -n 4

# Run with retries for flaky tests
pytest --reruns 3

# Run tests with specific browser
pytest --browser firefox
pytest --browser webkit

# Generate HTML report with custom path
pytest --html=custom_reports/my_report.html

# Run with trace enabled and headed mode
pytest tests/regression/homepage/test_dashboard.py --enable-trace --headed -v
```

## 🗂️ Test Organization

### Test Markers
The framework uses pytest markers to categorize tests:

- `@pytest.mark.smoke` - Quick smoke tests
- `@pytest.mark.regression` - Full regression tests
- `@pytest.mark.practice` - Practice/demo tests
- `@pytest.mark.pdf_verification` - PDF-related tests

### Writing Tests
Tests follow the Page Object Model pattern:

```python
import pytest

@pytest.mark.smoke
def test_dashboard_functionality(pageManager):
    # Use pageManager to access page objects
    pageManager.dashboard.verify_dashboard()
    pageManager.dashboard.fill_form(
        name="John Doe",
        email="john@example.com",
        phone="1234567890",
        company="Test Corp",
        role="QA Engineer",
        service="Testing",
        message="Test message"
    )
    pageManager.dashboard.click_button_get_in_touch()
```

## 📊 Reporting

### HTML Reports
- Generated automatically in `reports/report.html`
- Includes test results, timestamps, and failure details
- Self-contained with embedded CSS and JavaScript

### Screenshots
- Automatic screenshot capture on test failures
- Stored in `reports/screenshots/`
- Organized by test name and timestamp

### Traces
- Enable with `--enable-trace` flag
- Stored in `reports/trace/`
- Can be viewed in Playwright trace viewer:
  ```bash
  playwright show-trace reports/trace/your_trace.zip
  ```

## 🔍 Advanced Features

### Page Manager
Central manager for all page objects:
```python
def test_example(pageManager):
    pageManager.dashboard.some_action()
    pageManager.navigation.navigate_to_other_page("About")
```

### PDF Assertions
Utility class for PDF content validation:
```python
from main.utils.pdf_assert import PDFAssert

# Extract text from PDF
text = PDFAssert.extract_text("path/to/file.pdf")

# Search for specific content
assert PDFAssert.contains_text("path/to/file.pdf", "Expected Text")
```

### Excel Handling
Work with Excel files in your tests:
```python
from main.utils.excel_handler import ExcelHandler

# Read/write Excel data for data-driven tests
```

### JSON Configuration
Manage test data and configurations:
```python
from main.utils.json_handler import JSONHandler

# Load configuration data
config = JSONHandler.load_config("config_file.json")
```

## 🛠️ Utilities

### Available Utility Classes
1. **PDFAssert** - PDF content validation and text extraction
2. **ExcelHandler** - Excel file operations for data-driven testing
3. **JSONHandler** - JSON configuration management
4. **BaseActions** - Common web actions and utilities
5. **NavigationFunctions** - Page navigation helpers

### Logging
The framework includes comprehensive logging:
- Console output with timestamps
- File logging for debugging
- Different log levels (INFO, DEBUG, ERROR)

## 🤝 Contributing

1. Follow the existing code structure and patterns
2. Add appropriate test markers to new tests
3. Include proper documentation for new utilities
4. Ensure all tests pass before submitting changes
5. Update this README when adding new features

## 📝 Notes

- Screenshots and traces are automatically generated for failed tests
- The framework supports parallel execution for faster test runs
- All page objects should inherit from base classes for consistency
- Use the pageManager fixture to access all page objects in tests

## 🆘 Troubleshooting

### Common Issues

1. **Browser not found**: Run `playwright install`
2. **Import errors**: Ensure virtual environment is activated
3. **Test failures**: Check logs in `reports/` directory
4. **Trace issues**: Ensure `--enable-trace` flag is used

### Getting Help

- Check the generated HTML reports for detailed error information
- Use `--enable-trace` for detailed debugging
- Review log files for specific error messages
- Ensure all dependencies are properly installed