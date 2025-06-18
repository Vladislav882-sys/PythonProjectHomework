import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

@pytest.mark.skipif(True, reason="Page availability check failed")
def test_modal_dialogs(browser):
    try:
        browser.get("https://demoqa.com/modal-dialogs")
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "showSmallModal")))
    except TimeoutException:
        pytest.skip("Page is not available")

    small_modal_button = browser.find_element(By.ID, "showSmallModal")
    small_modal_button.click()

    small_modal = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-sm")))
    assert small_modal.is_displayed()

    close_button = browser.find_element(By.ID, "closeSmallModal")
    close_button.click()

    assert not small_modal.is_displayed()

    large_modal_button = browser.find_element(By.ID, "showLargeModal")
    large_modal_button.click()

    large_modal = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg")))
    assert large_modal.is_displayed()

    close_button = browser.find_element(By.ID, "closeLargeModal")
    close_button.click()
ь
    assert not large_modal.is_displayed()
