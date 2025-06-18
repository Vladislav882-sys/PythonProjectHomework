from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_sort(browser):
    browser.get("https://demoqa.com/webtables")
    headers = browser.find_elements(By.CSS_SELECTOR, ".rt-th .rt-resizable-header-content")

    for header in headers:
        header.click()
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".rt-th.-sort-asc .rt-resizable-header-content")))
        assert "-sort-asc" in header.get_attribute("class") or "-sort-desc" in header.get_attribute("class")
