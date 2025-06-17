from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class PracticeFormPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://demoqa.com/automation-practice-form'
        self.state_dropdown = (By.ID, 'state')
        self.city_dropdown = (By.ID, 'city')

    def visit(self):
        self.driver.get(self.url)

    def fill_state_and_city(self, state="NCR", city="Delhi"):
        self.driver.find_element(*self.state_dropdown).click()

        state_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f"//div[contains(text(), '{state}')]"))
        )
        state_input.click()

        self.driver.find_element(*self.city_dropdown).click()

        city_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f"//div[contains(text(), '{city}')]"))
        )
        city_input.click()

    def get_placeholder(self, locator_by, locator_value):
        return self.driver.find_element(locator_by, locator_value).get_attribute('placeholder')

    def get_attribute(self, locator_by, locator_value, attribute):
        return self.driver.find_element(locator_by, locator_value).get_attribute(attribute)

    def submit_form(self):
        submit_button = self.driver.find_element(By.ID, 'submit')
        submit_button.click()

    def get_form_class(self):
        return self.driver.find_element(By.ID, 'userForm').get_attribute('class')
