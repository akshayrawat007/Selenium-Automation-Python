import pytest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def setup_teardown():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    driver.get('https://ecommerce-playground.lambdatest.io/index.php?route=account/login')
    driver.find_element(By.ID,'input-email').send_keys("rawatakshay.0706@gmail.com")
    driver.find_element(By.ID,'input-password').send_keys("pytest1234")
    login_button = driver.find_element(By.XPATH,"//input[@value='Login']")
    login_button.click()
    sleep(5)
    print("Login")
    yield driver
    driver.find_element(By.PARTIAL_LINK_TEXT,'Logout').click()
    print("Logout")
    driver.quit()
