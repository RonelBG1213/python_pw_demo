import pytest
from playwright.sync_api import sync_playwright
# from playwright_mcp import MCPServer  # Remove or comment out this line
from main.fixtures.pageManager import PageManager
import json
from datetime import datetime
import base64
import os
import logging

# --- Add a mock MCPServer class ---
class MCPServer:
    def __init__(self, page, port=8123):
        self.page = page
        self.port = port
        self.running = False

    def start(self):
        self.running = True
        print(f"Mock MCPServer started on port {self.port}")

    def stop(self):
        self.running = False
        print("Mock MCPServer stopped")

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright

@pytest.fixture(scope="session")
def browser(playwright_instance, browser_name):
    browser = getattr(playwright_instance, browser_name).launch(headless=False)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def mcp_server(page):
    server = MCPServer(page, port=8123)
    server.start()
    try:
        yield server
    finally:
        server.stop()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context(viewport=None)
    page = context.new_page()
    with open("main/envi/urls.json", "r") as f:
        urls = json.load(f)
    page.goto(urls["baseURL"], timeout=60000)
    page.set_default_timeout(60000)

    yield page
    context.close()

@pytest.fixture(scope="function")
def pageManager(page):
    return PageManager(page)

@pytest.fixture(scope="function")
def logger():
    """Provide a configured logger for tests."""
    logger = logging.getLogger('test_logger')
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s [%(levelname)8s] %(name)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if call.when == "call":
        setattr(item, "rep_call", report)

    if pytest_html and hasattr(report, 'longrepr'):
        if hasattr(report, 'caplog') and report.caplog:
            log_content = report.caplog
            if log_content:
                extra.append(pytest_html.extras.text(log_content, "Captured Log Output"))

        if hasattr(report, 'capstdout') and report.capstdout:
            extra.append(pytest_html.extras.text(report.capstdout, "Captured stdout"))

        if hasattr(report, 'capstderr') and report.capstderr:
            extra.append(pytest_html.extras.text(report.capstderr, "Captured stderr"))

    if report.when == 'call':
        xfail = hasattr(report, 'wasxfail')

        test_status = "Unknown"
        if report.skipped:
            test_status = "Skipped"
            extra.append("Test was skipped")
        elif report.failed:
            test_status = "Failed"
        elif report.passed:
            test_status = "Passed"

        my_test_name = item.originalname
        parts = my_test_name.split('_')
        test_name = '_'.join(parts[:2])

        project_root = os.path.abspath(os.path.dirname(__file__))
        screenshot_folder = os.path.join(project_root, 'reports', 'screenshots', test_name)

        if not os.path.exists(screenshot_folder):
            os.makedirs(screenshot_folder)

        page_fixture = item.funcargs.get("page")
        pagemanager_fixture = item.funcargs.get("pageManager")

        if page_fixture:
            current_page = page_fixture

            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            screenshot_filename = f"{my_test_name}_{timestamp}_{test_status.lower()}.png"
            screenshot_path = os.path.join(screenshot_folder, screenshot_filename)

            try:
                current_page.screenshot(path=screenshot_path, full_page=True)

                with open(screenshot_path, "rb") as image_file:
                    image_data = base64.b64encode(image_file.read()).decode('utf-8')

                screenshot_label = f"Test {test_status} Screenshot"
                if report.failed:
                    screenshot_label = f"🔴 FAILED Test Screenshot - {my_test_name}"
                elif report.passed:
                    screenshot_label = f"✅ PASSED Test Screenshot - {my_test_name}"
                elif report.skipped:
                    screenshot_label = f"⚠️ SKIPPED Test Screenshot - {my_test_name}"

                if pytest_html:
                    extra.append(pytest_html.extras.image(image_data, screenshot_label))
            except Exception as e:
                print(f"Failed to capture screenshot: {e}")

        elif pagemanager_fixture and hasattr(pagemanager_fixture, 'page'):
            current_page = pagemanager_fixture.page

            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            screenshot_filename = f"{my_test_name}_{timestamp}_{test_status.lower()}.png"
            screenshot_path = os.path.join(screenshot_folder, screenshot_filename)

            try:
                current_page.screenshot(path=screenshot_path, full_page=True)

                with open(screenshot_path, "rb") as image_file:
                    image_data = base64.b64encode(image_file.read()).decode('utf-8')

                screenshot_label = f"Test {test_status} Screenshot"
                if report.failed:
                    screenshot_label = f"🔴 FAILED Test Screenshot - {my_test_name}"
                elif report.passed:
                    screenshot_label = f"✅ PASSED Test Screenshot - {my_test_name}"
                elif report.skipped:
                    screenshot_label = f"⚠️ SKIPPED Test Screenshot - {my_test_name}"

                if pytest_html:
                    extra.append(pytest_html.extras.image(image_data, screenshot_label))
            except Exception as e:
                print(f"Failed to capture screenshot: {e}")

        try:
            screenshot_prefix = f"{test_name}_"
            excluded_suffixes = ("_failed.png", "_passed.png", "_skipped.png", "_result.png", "_result.html")

            if os.path.exists(screenshot_folder):
                for filename in os.listdir(screenshot_folder):
                    if filename.startswith(screenshot_prefix) and not filename.endswith(excluded_suffixes):
                        screenshot_path = os.path.join(screenshot_folder, filename)

                        try:
                            with open(screenshot_path, "rb") as image_file:
                                image_data = base64.b64encode(image_file.read()).decode('utf-8')

                            if pytest_html:
                                extra.append(pytest_html.extras.image(image_data, f"📸 Additional Screenshot - {filename}"))
                        except Exception as e:
                            print(f"Failed to process additional screenshot {filename}: {e}")
        except Exception as e:
            print(f"Failed to process additional screenshots: {e}")

        if call.when == 'call' and pytest_html:
            log_content = ""

            if 'caplog' in item.funcargs:
                caplog = item.funcargs['caplog']
                if caplog.records:
                    for record in caplog.records:
                        if record.name.startswith('main.') or record.name.startswith('test_'):
                            timestamp = datetime.fromtimestamp(record.created).strftime('%Y-%m-%d %H:%M:%S')
                            log_content += f"{timestamp} [{record.levelname}] {record.name}: {record.getMessage()}\n"

            try:
                logging_plugin = item.config.pluginmanager.get_plugin("logging-plugin")
                if logging_plugin and hasattr(logging_plugin, 'item_collected_logs'):
                    collected_logs = getattr(logging_plugin, 'item_collected_logs', {})
                    if item.nodeid in collected_logs:
                        for record in collected_logs[item.nodeid]:
                            if record.name.startswith('main.'):
                                timestamp = datetime.fromtimestamp(record.created).strftime('%Y-%m-%d %H:%M:%S')
                                log_content += f"{timestamp} [{record.levelname}] {record.name}: {record.getMessage()}\n"
            except:
                pass

            if log_content.strip():
                extra.append(pytest_html.extras.text(log_content, "📋 Test Execution Logs"))

        report.extras = extra

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    reports_dir = os.path.join(os.path.dirname(__file__), 'reports')
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)

@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    pass
