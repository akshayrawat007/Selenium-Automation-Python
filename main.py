# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
# driver = webdriver.Chrome(
#     service=Service(ChromeDriverManager().install())
# )
#
# driver.maximize_window()
#
# name = ["akshay","vansh","abhay","pracheen"]
# for identity in name:
#     print(identity)
# print([name[0]])
# dict1 = {
#     "Name": "Akshay",
#     "Age": 2,
#     "Blood Group": "AB+"
# }
# print(dict1["Age"])
#
# for i in range(7):
#     print(i)
#
# age = 72
# if age < 60:
#     print("Employee")
# elif age >=60:
#     print("Senior Citizen")
# else: print("Unemployed")
#
# count = 0
#
# while count < 10:
#     print(count)
#     count+=1
#
# for i in range(20):
#     if i == 7:
#         continue
#     print(i)
#
#
# driver.get("https://www.google.com")
#
# print(driver.title)
#
#
# browsers = ["chrome", "firefox", "safari"]
# for index, browser in enumerate(browsers):
#     print(index, browser)
# driver.quit()