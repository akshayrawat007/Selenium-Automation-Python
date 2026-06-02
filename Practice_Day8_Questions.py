from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('https://vinothqaacademy.com/drop-down/')
driver.maximize_window()
title = driver.title
assert title == "Demo Site – DropDown – Vinoth Tech Solutions"
city_drop_down = driver.find_element(By.ID,'simpleDropdown')
select_city = Select(city_drop_down)
select_city.select_by_visible_text('London')
account_drop_down = driver.find_element(By.ID,'FromAccount')
select_account = Select(account_drop_down)
select_account.select_by_value('Salary')
#multiple selection
choose_programming_lang_drop_down = driver.find_element(By.NAME,'programming')
select_language = Select(choose_programming_lang_drop_down)
required_languages = ["JAVA","PYTHON","PHP"]
all_options = select_language.options
#going to select 3 languages dynamically
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
for option in all_options:
    option_value = option.get_attribute('value')
    if option_value in required_languages:
        select_language.select_by_value(option_value)
sleep(5)
#Navigating to HomePage
driver.execute_script("window.scrollTo(0, 0)")
home_bar = driver.find_element(By.LINK_TEXT,'Home')
home_bar.click()
title = driver.title
assert title == "Vinoth Tech Solutions – Empowering Tech Careers"
#countinng all links on homepage
all_links = driver.find_elements(By.TAG_NAME,'a')
print("Total links", len(all_links))



