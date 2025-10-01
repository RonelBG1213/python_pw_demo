import pytest


@pytest.mark.practice
def test_verify_dashboard(pageManager):
    pageManager.dashboard.verify_dashboard()
    pageManager.dashboard.fill_form("Jane Doe", "janedoe@gmail.com", "09187777776", "doers.org", "quality assurance", "Data", "ultra long message")
    pageManager.dashboard.click_button_get_in_touch


@pytest.mark.practice
def test_verify_dashboard_s(pageManager,mcp_server):
    pageManager.dashboard.verify_dashboard()
    pageManager.dashboard.fill_form("Jane Doe", "janedoe@gmail.com", "09187777776", "doers.org", "quality assurance", "Data", "ultra long message")
    pageManager.dashboard.click_button_get_in_touch
