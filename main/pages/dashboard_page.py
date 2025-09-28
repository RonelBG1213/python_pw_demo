class dashboardPage:
    def __init__(self, page):
        self.home_banner_heading = page.get_by_role("heading", name="Fast forward to the future")
        self.our_services_heading = page.get_by_role("heading", name="OUR SERVICES")
        self.why_stratpoint_heading = page.get_by_role("heading", name="WHY STRATPOINT?")
        self.lets_connect_heading = page.get_by_role("heading", name="Let's connect")
        self.name_textfield = page.get_by_role("textbox", name="Name", exact=True)
        self.email_address_textfield = page.get_by_role("textbox", name="Email Address")
        self.contact_num_textfield = page.get_by_role("textbox", name="Contact Number")
        self.company_textfield = page.get_by_role("textbox", name="Company Name")
        self.job_title_textfield = page.get_by_role("textbox", name="Job Title")
        self.service_select = page.get_by_role("combobox", name="service")
        self.message_textfield = page.locator("[placeholder='Message']")
        self.privacy_checkbox = page.get_by_role("checkbox", name="We value your privacy and we'")
        self.get_in_touch_button = page.get_by_role("checkbox", name="GET IN TOUCH")





