from selenium.webdriver.common.by import By

from utils.common_browser_utils import CommonBrowserUtils


class FormPage(CommonBrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.first_name_input = (By.CSS_SELECTOR, "#firstname")
        self.middle_name_input = (By.CSS_SELECTOR, "#middlename")
        self.last_name_input = (By.CSS_SELECTOR, "#lastname")
        self.email_input = (By.CSS_SELECTOR, "#email")
        self.password_input = (By.CSS_SELECTOR, "#password")
        self.address_input = (By.CSS_SELECTOR, "#address")
        self.city_input = (By.CSS_SELECTOR, "#city")
        self.state_input = (By.CSS_SELECTOR, "#states")
        self.pincode_input = (By.CSS_SELECTOR, "#pincode")
        self.submit_button = (By.CSS_SELECTOR, "button[type='submit']")
        self.message = (By.CSS_SELECTOR, "#message")


    def enter_firstname(self, firstname):
        self.driver.find_element(*self.first_name_input).clear()
        self.driver.find_element(*self.first_name_input).send_keys(firstname)

    def enter_middle_name(self, middle_name):
        self.driver.find_element(*self.middle_name_input).clear()
        self.driver.find_element(*self.middle_name_input).send_keys(middle_name)

    def enter_last_name(self, lastname):
        self.driver.find_element(*self.last_name_input).clear()
        self.driver.find_element(*self.last_name_input).send_keys(lastname)

    def enter_email(self, email):
        self.driver.find_element(*self.email_input).clear()
        self.driver.find_element(*self.email_input).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).clear()
        self.driver.find_element(*self.password_input).send_keys(password)

    def enter_address(self, address):
        self.driver.find_element(*self.address_input).clear()
        self.driver.find_element(*self.address_input).send_keys(address)

    def enter_city(self, city):
        self.driver.find_element(*self.city_input).clear()
        self.driver.find_element(*self.city_input).send_keys(city)

    def enter_state(self, state):
        self.driver.find_element(*self.state_input).clear()
        self.driver.find_element(*self.state_input).send_keys(state)

    def enter_pincode(self, pincode):
        self.driver.find_element(*self.pincode_input).clear()
        self.driver.find_element(*self.pincode_input).send_keys(pincode)

    def click_submit_button(self):
        self.driver.find_element(*self.submit_button).click()

    def fill_form_and_submit(self, data):
        self.enter_firstname(data['firstname'])
        self.enter_middle_name(data['middle_name'])
        self.enter_last_name(data['lastname'])
        self.enter_email(data['email'])
        self.enter_password(data['password'])
        self.enter_address(data['address'])
        self.enter_city(data['city'])
        self.enter_state(data['state'])
        self.enter_pincode(data['pincode'])
        self.click_submit_button()
        return FormPage(self.driver)

    def get_form_submission_message(self):
        return self.driver.find_element(*self.message).text
