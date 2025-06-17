from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TextBoxPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://demoqa.com/text-box'
        self.full_name_field = (By.ID, 'userName')
        self.current_address_field = (By.ID, 'currentAddress')
        self.submit_button = (By.ID, 'submit')
        self.output_full_name = (By.ID, 'name')
        self.output_current_address = (By.CSS_SELECTOR, '#output #currentAddress')

    def visit(self):
        self.driver.get(self.url)

    def fill_full_name(self, text):
        self.driver.find_element(*self.full_name_field).send_keys(text)

    def fill_current_address(self, text):
        self.driver.find_element(*self.current_address_field).send_keys(text)

    def submit(self):
        self.driver.find_element(*self.submit_button).click()

    def get_output_full_name(self):
        return self.driver.find_element(*self.output_full_name).text.split(':')[1].strip()

    def get_output_current_address(self):
        return self.driver.find_element(*self.output_current_address).text.split(':')[1].strip()
