import pytest

from page_objects.dashboard_page_objects import DashboardPage


@pytest.mark.smoke
def test_shadow_dom_validation(browser_invoke):
    driver = browser_invoke
    driver.get("https://testing.qaautomationlabs.com/")
    dashboard_page_obj = DashboardPage(driver)
    shadow_dom_page_obj = dashboard_page_obj.navigate_to_shadow_dom_page()
    outside_shadow_label = shadow_dom_page_obj.get_shadow_dom_label_text()
    assert outside_shadow_label == "This is outside Shadow DOM"
    inside_shadow_label = shadow_dom_page_obj.get_shadow_element_text()
    assert inside_shadow_label == "Hello from Shadow DOM!"