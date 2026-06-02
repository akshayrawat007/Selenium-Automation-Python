from time import sleep

from selenium.webdriver.common.by import By


def test_order_history_title(setup_teardown ):
    driver = setup_teardown
    order_history = driver.find_element(By.XPATH,"//a[text()=' Order History']")
    order_history.click()
    assert driver.title == 'Order History'
    sleep(5)
    print("Test 1 is complete")


def test_password_title(setup_teardown):
    driver = setup_teardown
    password = driver.find_element(By.PARTIAL_LINK_TEXT,'Password')
    password.click()
    assert driver.title == 'Change Password'
    sleep(5)
    print("Test 2 is complete")





