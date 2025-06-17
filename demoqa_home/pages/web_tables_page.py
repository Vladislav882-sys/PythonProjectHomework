from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class WebTablesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://demoqa.com/webtables'
        self.add_button = (By.ID, 'addNewRecordButton')
        self.submit_button = (By.ID, 'submit')
        self.dialog = (By.CSS_SELECTOR, '.modal-content')
        self.first_name_field = (By.ID, 'firstName')
        self.last_name_field = (By.ID, 'lastName')
        self.user_email_field = (By.ID, 'userEmail')
        self.age_field = (By.ID, 'age')
        self.salary_field = (By.ID, 'salary')
        self.department_field = (By.ID, 'department')
        self.edit_button = (By.CSS_SELECTOR, 'span[title="Edit"]')
        self.delete_button = (By.CSS_SELECTOR, 'span[title="Delete"]')
        self.rows = (By.CSS_SELECTOR, '.rt-tr-group')
        self.next_button = (By.CSS_SELECTOR, 'button[title="Next"]')
        self.previous_button = (By.CSS_SELECTOR, 'button[title="Previous"]')
        self.page_info = (By.CSS_SELECTOR, '.rt-center .-pageInfo')

    def visit(self):
        self.driver.get(self.url)

    def click_add_button(self):
        self.driver.find_element(*self.add_button).click()

    def is_dialog_open(self):
        return self.driver.find_element(*self.dialog).is_displayed()

    def fill_form(self, first_name, last_name, user_email, age, salary, department):
        self.driver.find_element(*self.first_name_field).send_keys(first_name)
        self.driver.find_element(*self.last_name_field).send_keys(last_name)
        self.driver.find_element(*self.user_email_field).send_keys(user_email)
        self.driver.find_element(*self.age_field).send_keys(age)
        self.driver.find_element(*self.salary_field).send_keys(salary)
        self.driver.find_element(*self.department_field).send_keys(department)

    def click_submit_button(self):
        self.driver.find_element(*self.submit_button).click()

    def get_row_count(self):
        return len(self.driver.find_elements(*self.rows))

    def click_edit_button(self, row_index):
        edit_buttons = self.driver.find_elements(*self.edit_button)
        edit_buttons[row_index].click()

    def click_delete_button(self, row_index):
        delete_buttons = self.driver.find_elements(*self.delete_button)
        delete_buttons[row_index].click()

    def is_next_button_disabled(self):
        return 'disabled' in self.driver.find_element(*self.next_button).get_attribute('class')

    def is_previous_button_disabled(self):
        return 'disabled' in self.driver.find_element(*self.previous_button).get_attribute('class')

    def click_next_button(self):
        self.driver.find_element(*self.next_button).click()

    def click_previous_button(self):
        self.driver.find_element(*self.previous_button).click()

    def get_page_info(self):
        return self.driver.find_element(*self.page_info).text
