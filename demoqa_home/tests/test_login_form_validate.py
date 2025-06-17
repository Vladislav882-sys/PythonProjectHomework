from selenium.webdriver.common.by import By
from pages.practice_form_page import PracticeFormPage

def test_placeholder_validation(browser):

    practice_form_page = PracticeFormPage(browser)
    practice_form_page.visit()

    assert practice_form_page.get_placeholder(By.ID, 'firstName') == 'FirstName'
    assert practice_form_page.get_placeholder(By.ID, 'lastName') == 'LastName'
    assert practice_form_page.get_placeholder(By.ID, 'userEmail') == 'name@example.com'
    assert practice_form_page.get_attribute(By.ID, 'userEmail', 'pattern') == '^[\\w-\\.]+@([\\w-]+\\.)+[\\w-]{2,4}$'

    practice_form_page.submit_form()
    assert 'was-validated' in practice_form_page.get_form_class()
    
from pages.practice_form_page import PracticeFormPage

def test_state_and_city(browser):
    practice_form_page = PracticeFormPage(browser)
    practice_form_page.visit()

    practice_form_page.fill_state_and_city()
