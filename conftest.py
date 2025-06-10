import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Chrome(executable_path="./driver/chromedriver")  # укажите свой путь
    yield driver
    driver.quit()
