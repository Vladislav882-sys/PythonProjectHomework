import time
from pages.accordion import Accordion

def test_visible_accordion(browser):
    accordion_page = Accordion(browser)
    accordion_page.visit()

    assert accordion_page.is_section1_content_visible()
    accordion_page.click_section1_heading()
    time.sleep(2)

    assert not accordion_page.is_section1_content_visible()

def test_visible_accordion_default(browser):
    accordion_page = Accordion(browser)
    accordion_page.visit()

    assert not accordion_page.is_section2_content_p1_visible()
    assert not accordion_page.is_section2_content_p2_visible()
    assert not accordion_page.is_section3_content_p_visible()
