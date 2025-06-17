from selenium.webdriver.common.by import By
from pages.text_box_page import TextBoxPage

def test_text_box(browser):

    text_box_page = TextBoxPage(browser)
    text_box_page.visit()

    full_name = "Vlad Lord"
    current_address = "123 Lenina St"
    text_box_page.fill_full_name(full_name)
    text_box_page.fill_current_address(current_address)

    text_box_page.submit()
  
    assert text_box_page.get_output_full_name() == full_name
    assert text_box_page.get_output_current_address() == current_address
