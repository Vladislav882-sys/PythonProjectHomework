from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ModalDialogsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://demoqa.com/modal-dialogs'
        self.submenu_buttons = (By.CSS_SELECTOR, '.btn.btn-light')
        self.home_icon = (By.CSS_SELECTOR, 'img[src="/images/Toolsqa.jpg"]')

    def visit(self):
        self.driver.get(self.url)

    def count_submenu_buttons(self):
        return len(self.driver.find_elements(*self.submenu_buttons))

    def click_home_icon(self):
        self.driver.find_element(*self.home_icon).click()
