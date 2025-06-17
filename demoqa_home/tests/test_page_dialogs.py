import time
from pages.modal_dialogs import ModalDialogsPage

def test_modal_elements(browser):
    modal_dialogs_page = ModalDialogsPage(browser)
    modal_dialogs_page.visit()

    assert modal_dialogs_page.count_submenu_buttons() == 5

def test_navigation_modal(browser):
    modal_dialogs_page = ModalDialogsPage(browser)
    modal_dialogs_page.visit()

    browser.refresh()
    modal_dialogs_page.click_home_icon()
    browser.back()

    browser.set_window_size(900, 400)
    browser.forward()
  
    assert browser.current_url == 'https://demoqa.com/'
    assert 'ToolsQA' in browser.title

    browser.set_window_size(1000, 1000)
