import time
from pages.web_tables_page import WebTablesPage

def test_web_tables(browser):
    web_tables_page = WebTablesPage(browser)
    web_tables_page.visit()

    web_tables_page.click_add_button()

    assert web_tables_page.is_dialog_open()

    web_tables_page.click_submit_button()
    assert web_tables_page.is_dialog_open()

    web_tables_page.fill_form("Vlad", "Lord", "test@test.com", "30", "50000", "IT")
    web_tables_page.click_submit_button()

    assert not web_tables_page.is_dialog_open()
    assert web_tables_page.get_row_count() > 0

    web_tables_page.click_edit_button(0)

    web_tables_page.fill_form("Ivan", "Lord", "test@test.com", "30", "50000", "IT")
    web_tables_page.click_submit_button()

    assert "Ivan" in browser.page_source

    web_tables_page.click_delete_button(0)
    assert web_tables_page.get_row_count() == 0

def test_web_tables_pagination(browser):
    web_tables_page = WebTablesPage(browser)
    web_tables_page.visit()

    assert web_tables_page.is_next_button_disabled()
    assert web_tables_page.is_previous_button_disabled()

    for i in range(3):
        web_tables_page.click_add_button()
        web_tables_page.fill_form(f"FirstName{i}", f"LastName{i}", f"email{i}@example.com", "25", "40000", "HR")
        web_tables_page.click_submit_button()

    assert "of 2" in web_tables_page.get_page_info()
    assert not web_tables_page.is_next_button_disabled()

    web_tables_page.click_next_button()
    assert "2" in web_tables_page.get_page_info()

    web_tables_page.click_previous_button()
    assert "1" in web_tables_page.get_page_info()
