from pathlib import Path
import inspect
from datetime import datetime


class BaseActions:
    def __init__(self, page):
        self.page = page

    def navigate_to(self, url):
        self.page.goto(url)

    def click_element(self, element):
        element.click()

    def fill_textfield(self, element, text):
        element.fill(text)

    def select_option(self, element, text):
        element.select_option(text)

    def get_text(self, element):
        return element.text_content()

    def assert_element(self, element):
        return element.is_visible()

    def take_screenshot(self, addedString="screenshot", full_page=True):
        screenshots_dir = Path("reports/screenshots")
        screenshots_dir.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"{addedString}_{timestamp}_result.png"

        screenshot_path = screenshots_dir / filename
        self.page.screenshot(path=str(screenshot_path), full_page=full_page)



