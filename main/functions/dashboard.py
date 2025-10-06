from main.pages.dashboard_page import dashboardPage
from main.fixtures.baseActions import BaseActions


class dashboardFunctions:
    def __init__(self, page, logger):
        self.page = page
        self.logger = logger
        self.__dashboardLocators = dashboardPage(page)
        self.actions = BaseActions(page)

    def verify_dashboard(self):
        self.logger.info("Verifying dashboard")
        self.actions.assert_element(self.__dashboardLocators.home_banner_heading)

    def fill_form(self, name, email, contactnum, company, jobtitle, service, textareamsg):
        self.logger.info("Start filling up form")
        # self.page.pause()
        self.actions.fill_textfield(self.__dashboardLocators.name_textfield, name)
        self.actions.fill_textfield(self.__dashboardLocators.email_address_textfield, email)
        self.actions.fill_textfield(self.__dashboardLocators.contact_num_textfield, contactnum)
        self.actions.fill_textfield(self.__dashboardLocators.company_textfield, company)
        self.actions.fill_textfield(self.__dashboardLocators.job_title_textfield, jobtitle)
        self.actions.select_option(self.__dashboardLocators.service_select, service)
        self.actions.fill_textfield(self.__dashboardLocators.message_textfield, textareamsg)
        self.actions.click_element(self.__dashboardLocators.privacy_checkbox)
        self.actions.take_screenshot(addedString="formfille")

    def click_button_get_in_touch(self):
        self.actions.click_element(self.__dashboardLocators.get_in_touch_button)

    def privacy_policy_link(self):
        # self.page.pause()
        self.logger.info("Getting url")
        self.actions.open_href_in_new_tab(self.__dashboardLocators.privacy_policy_link)
        self.logger.info("Set focus on new tab")
        self.actions.focus_specific_tab(1)
        self.logger.info("Set focus on main tab")
        self.actions.focus_specific_tab(0)
