from time import sleep

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
# implicit wait
# driver.implicitly_wait(10)
# explicit wait
# wait = WebDriverWait(driver,30)
# fluent wait
wait = WebDriverWait(driver,timeout=30,poll_frequency=5,ignored_exceptions=[NoSuchElementException])
driver.get('https://omayo.blogspot.com/')
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
driver.find_element(By.CSS_SELECTOR,'.dropbtn').click()
flipkart_option = wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Flipkart')))
flipkart_option.click()