from selenium.webdriver.common.by import By

def test_window_tab(browser):
    browser.get("https://demoqa.com/links")

    home_link = browser.find_element(By.LINK_TEXT, "Home")

    assert home_link.text == "Home"
    assert home_link.get_attribute("href") == "https://demoqa.com"

    home_link.click()
    browser.switch_to.window(browser.window_handles[1])

    assert browser.current_url == "https://demoqa.com"

  
