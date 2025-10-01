from main.fixtures.baseActions import BaseActions

class navigationFunctions:
    def __init__(self, page, logger):
        self.page = page
        self.logger = logger
        self.actions = BaseActions(page)


    def navigate_to_other_page(self, sitepage):
        self.logger.info(f"Navigating to {sitepage} page")
        match(sitepage):
            case "Home":
                self.actions.click_element(self.page.locator("a:has-text('Home')"))
                self.actions.assert_element(self.page.locator("text=Welcome to Home"))  
            case "About":
                self.actions.click_element(self.page.get_by_role("link", name="About 3"))
                self.actions.assert_element(self.page.locator("text=About Us"))
            case "Services":
                self.actions.click_element(self.page.locator("a:has-text('Services')"))
                self.actions.assert_element(self.page.locator("text=Our Services"))
            case "Contact":
                self.actions.click_element(self.page.locator("nav#top-menu-nav").locator("//ul[@id='top-menu']/li").get_by_role("link", name="Contact Us"))
                self.actions.assert_element(self.page.locator("nav#top-menu-nav").locator("//ul[@id='top-menu']/li").get_by_role("link", name="Contact Us"))
            case _:
                self.logger.error(f"Unknown page: {sitepage}")
                raise ValueError(f"Unknown page: {sitepage}")
        self.actions.take_screenshot(f"navigated_to_{sitepage.lower()}")