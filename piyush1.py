from selenium import webdriver

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Users\Cliffex-Lead\Downloads\chromedriver_win32 (3)\chromedriver.exe")

driver.get("https://www.facebook.com/login/")

print(driver.title)

driver.close()
