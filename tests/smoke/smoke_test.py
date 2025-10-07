import pytest

@pytest.mark.practice
def test_smoke1(pageManager):
    pageManager.dashboard.verify_dashboard()
    pageManager.dashboard.fill_form("John Doe", "johndoe@gmail.com", "09187777776", "doers.org", "quality assurance", "Cloud", "ultra long message")
    pageManager.dashboard.click_button_get_in_touch

@pytest.mark.practice
def test_smoke2(pageManager):
    pageManager.dashboard.verify_dashboard()
    pageManager.dashboard.fill_form("Jane Doe", "janedoe@gmail.com", "09187777776", "doers.org", "quality assurance", "Data", "ultra long message")
    pageManager.dashboard.click_button_get_in_touch

def test_smoke3(pageManager):
    # pageManager.page.pause()
    pageManager.navigation.navigate_to_other_page("About")
    pageManager.navigation.navigate_to_other_page("Contact")

def test_smoke4(pageManager):
    pageManager.dashboard.verify_dashboard()
    pageManager.dashboard.privacy_policy_link()
    pageManager.dashboard.fill_form("Jane Doe", "janedoe@gmail.com", "09187777776", "doers.org", "quality assurance", "Data", "ultra long message")
    pageManager.dashboard.click_button_get_in_touch


