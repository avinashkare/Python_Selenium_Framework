import json
import pytest
from page_objects.dashboard_page_objects import DashboardPage

test_data_path = "../test_data/test_form_validation.json"

with open(test_data_path) as json_file:
    data = json.load(json_file)
    data_list = data["data"]

@pytest.mark.parametrize("data_items", data_list)
def test_form_validation(browser_invoke, data_items):
    driver = browser_invoke
    driver.get("https://testing.qaautomationlabs.com/")
    dashboard_page_obj = DashboardPage(driver)
    # form_submission_status = dashboard_page_obj.navigate_to_form().fill_form_and_submit(data).get_form_submission_message()
    form_page_obj = dashboard_page_obj.navigate_to_form_page()
    form_page_obj.fill_form_and_submit(data_items)
    form_submission_status = form_page_obj.get_form_submission_message()
    assert 'Form submitted successfully' == form_submission_status
    driver.close()