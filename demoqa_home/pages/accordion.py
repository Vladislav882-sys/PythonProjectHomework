from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class Accordion(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://demoqa.com/accordion'

        self.section1_content = (By.CSS_SELECTOR, '#section1Content > p')
        self.section1_heading = (By.CSS_SELECTOR, '#section1Heading')
        self.section2_content_p1 = (By.CSS_SELECTOR, '#section2Content > p:nth-child(1)')
        self.section2_content_p2 = (By.CSS_SELECTOR, '#section2Content > p:nth-child(2)')
        self.section3_content_p = (By.CSS_SELECTOR, '#section3Content > p')

    def visit(self):
        self.driver.get(self.url)

    def is_section1_content_visible(self):
        return self.find_element(self.section1_content).is_displayed()

    def click_section1_heading(self):
        self.find_element(self.section1_heading).click()

    def is_section2_content_p1_visible(self):
        return self.find_element(self.section2_content_p1).is_displayed()

    def is_section2_content_p2_visible(self):
        return self.find_element(self.section2_content_p2).is_displayed()

    def is_section3_content_p_visible(self):
        return self.find_element(self.section3_content_p).is_displayed()
