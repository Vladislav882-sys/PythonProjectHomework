from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class PracticeFormPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://demoqa.com/automation-practice-form'

    def visit(self):
        self.driver.get(self.url)

    def get_placeholder(self, locator_by, locator_value):
        return self.driver.find_element(locator_by, locator_value).get_attribute('placeholder')

    def get_attribute(self, locator_by, locator_value, attribute):
        return self.driver.find_element(locator_by, locator_value).get_attribute(attribute)

    def submit_form(self):
        submit_button = self.driver.find_element(By.ID, 'submit')
        submit_button.click()

    def get_form_class(self):
        return self.driver.find_element(By.ID, 'userForm').get_attribute('class')
