import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_alert(browser):
    browser.get("https://demoqa.com/alerts")

    timer_alert_button = browser.find_element(By.ID, "timerAlertButton")
    timer_alert_button.click()

    time.sleep(5)
    alert = WebDriverWait(browser, 10).until(EC.alert_is_present())

    assert alert.text == "This alert appeared after 5 seconds"
    alert.accept()
