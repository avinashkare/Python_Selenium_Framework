import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.common_browser_utils import CommonBrowserUtils

logger = logging.getLogger(__name__)

class ShadowDomPage(CommonBrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.outside_shadow_dom_label = (By.XPATH, "//h3[contains(text(), 'Shadow')]")
        self.shadow_host = (By.CSS_SELECTOR, "#shadow-host")
        self.shadow_element = (By.CSS_SELECTOR, ".box")

    def get_shadow_dom_label_text(self):
        return self.driver.find_element(*self.outside_shadow_dom_label).text

    def get_shadow_element_text(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(self.shadow_host))
        shadow_host_element = self.driver.find_element(*self.shadow_host)
        shadow_root = self.driver.execute_script("return arguments[0].shadowRoot", shadow_host_element)
        return shadow_root.find_element(*self.shadow_element).text
