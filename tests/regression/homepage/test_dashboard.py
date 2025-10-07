import pytest


@pytest.mark.practice
def test_verify_dashboard(pageManager):
    pageManager.dashboard.verify_dashboard()
    pageManager.dashboard.fill_form("Jane Doe", "janedoe@gmail.com", "09187777776", "doers.org", "quality assurance", "Data", "ultra long message")
    pageManager.dashboard.click_button_get_in_touch

@pytest.mark.practice
def test_verify_dashboard_s(pageManager):
    pageManager.dashboard.verify_dashboard()
    pageManager.dashboard.fill_form("Jane Doe", "janedoe@gmail.com", "09187777776", "doers.org", "quality assurance", "Data", "ultra long message")
    pageManager.dashboard.click_button_get_in_touch

@pytest.mark.practice
@pytest.mark.parametrize(
    "name,email,phone,org,role,department,message",
    [
        ("Jane Doe", "janedoe@gmail.com", "09187777776", "doers.org", "quality assurance", "Data", "ultra long message"),
        ("John Smith", "johnsmith@example.com", "09998887766", "testers.com", "developer", "Cloud", "short message")
    ]
)
def test_verify_dashboard_parameterize(pageManager, name, email, phone, org, role, department, message):
    pageManager.dashboard.verify_dashboard()
    pageManager.dashboard.fill_form(name, email, phone, org, role, department, message)
    pageManager.dashboard.click_button_get_in_touch()


@pytest.mark.parametrize(
    "form_data",
    [
        {
            "name": "Jane Doe",
            "email": "janedoe@gmail.com",
            "phone": "09187777776",
            "org": "doers.org",
            "role": "quality assurance",
            "department": "Data",
            "message": "ultra long message"
        },
        {
            "name": "John Smith",
            "email": "johnsmith@example.com",
            "phone": "09998887766",
            "org": "testers.com",
            "role": "developer",
            "department": "Cloud",
            "message": "short message"
        }
    ]
)
def test_verify_dashboard_parameterize_2(pageManager, form_data):
    pageManager.dashboard.verify_dashboard()
    pageManager.dashboard.fill_form(
        form_data["name"],
        form_data["email"],
        form_data["phone"],
        form_data["org"],
        form_data["role"],
        form_data["department"],
        form_data["message"]
    )
    pageManager.dashboard.click_button_get_in_touch()