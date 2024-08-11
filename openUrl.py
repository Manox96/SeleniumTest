from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.common.by import By

options = Options()
options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'

driver = webdriver.Chrome(service=chromeService(ChromeDriverManager().install()), options=options)

driver.get("https://www.google.com")

search_bar = driver.find_element(By.ID, "APjFqb")

# if u dint find id, use xpath  
# search_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[1]")
# search_btn.click()

search_bar.send_keys("usful things for python")

# this how to press enter
search_bar.send_keys(u'\ue007')
#u'\ue007' is the enter key in selenium to check the key code use this link: https://www.w3.org/2002/09/tests/keys.html

time.sleep(100)
driver.close()
