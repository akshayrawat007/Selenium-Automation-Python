import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_uploading_file(driver):
    file_name = 'Jason_Duval_01.webp'
    file_path = os.path.abspath(f"sample_files/{file_name}")
    driver.get("https://practice.expandtesting.com/upload")
    wait = WebDriverWait(driver,10)
    file_input = wait.until(EC.presence_of_element_located((By.ID, "fileInput")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", file_input )
    file_input.send_keys(file_path)
    driver.find_element(By.ID, "fileSubmit").click()
    # Upload succeeded check
    success_message = wait.until(EC.visibility_of_element_located((By.XPATH,f"//p[contains(text(),'{file_name}')]")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", success_message)
    assert "Jason_Duval_01.webp" in success_message.text
    print(f"Uploaded: {success_message.text}")

    # Playing around types of locator & closing the ads
    home_page_locator = driver.find_element(By.LINK_TEXT,'Home')
    home_page_locator.click()
    parent_frame = driver.find_element(By.ID,'aswift_4')
    driver.switch_to.frame(parent_frame)
    all_ads = driver.find_elements(By.CLASS_NAME,'continue-prompt-text')
    first_ad = all_ads[0]
    first_ad.click()
    driver.switch_to.default_content()
    driver.find_element(By.PARTIAL_LINK_TEXT,'API').is_displayed()
    all_h2_locators = driver.find_elements(By.TAG_NAME,'h2')
    print(len(all_h2_locators))
    driver.find_element(By.CSS_SELECTOR,'.btn.btn-expand.btn-sm').is_enabled()








