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

    def new_tab(self):
        context = self.page.context
        new_page = context.new_page()
        return new_page

    def get_attribute_value(self, element, attribute):
        href_value = element.get_attribute(attribute)
        return href_value

    def open_href_in_new_tab(self, element):
        href = element.get_attribute("href")
        if href:
            new_page = self.new_tab()
            new_page.goto(href)
            return new_page
        return None

    def focus_specific_tab(self, indexOfTab):
        pages = self.page.context.pages
        if len(pages) > 1:
            selected_page_tab = pages[indexOfTab]
            selected_page_tab.bring_to_front()
            return selected_page_tab
        else:
            print("Tab not found!")
            return None

    def take_screenshot(self, addedString="screenshot", full_page=True):
        screenshots_dir = Path("reports/screenshots")
        screenshots_dir.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"{addedString}_{timestamp}_result.png"

        screenshot_path = screenshots_dir / filename
        self.page.screenshot(path=str(screenshot_path), full_page=full_page)







