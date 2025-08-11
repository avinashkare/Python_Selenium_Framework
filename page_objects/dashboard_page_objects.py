from selenium.webdriver.common.by import By

from page_objects.form_page_objects import FormPage
from page_objects.shadow_dom_page_objects import ShadowDomPage
from utils.common_browser_utils import CommonBrowserUtils


class DashboardPage(CommonBrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.form_button = (By.XPATH, "//a[text()='Form']")
        self.shadow_dom_button = (By.XPATH, "//a[text()='Shadow Dom']")

    def navigate_to_form_page(self):
        self.driver.find_element(*self.form_button).click()
        return FormPage(self.driver)


    def navigate_to_shadow_dom_page(self):
        self.driver.find_element(*self.shadow_dom_button).click()
        return ShadowDomPage(self.driver)