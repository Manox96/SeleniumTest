

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # Add this import statement
import time
import pickle #used for save seasion on cookies
import os

driver = webdriver.Chrome(service=chromeService(ChromeDriverManager().install()), options=Options())


driver.get("https://practicetestautomation.com/practice-test-login/")
cookies_file = "cookies.pkl"
useCookies = False

if (os.path.exists(cookies_file) and useCookies):
    cookies = pickle.load(open(cookies_file,'rb'))
    for cookie in cookies:
        driver.add_cookie(cookie)
    time.sleep(5)
else:
    print("\033[91m --- No Cookies Saved--- \033[0m")
    userNameBar = driver.find_element(By.ID, "username")
    passWordBar = driver.find_element(By.ID, "password")
    submitBtn = driver.find_element(By.XPATH, '//*[@id="submit"]')

    userNameBar.send_keys("student")
    time.sleep(2)
    passWordBar.send_keys("Password123")
    time.sleep(2)
    submitBtn.click()
    time.sleep(5)

    # we will save (dumping) cookies here
    try:
        pickle.dump(driver.get_cookies(), open(cookies_file, 'wb'))
        print("\033[92m[😍] Cookies created successfully\033[0m")
    except:
        print("\033[92m[🤬] Cookies not created successfully\033[0m")

    try:
        checkErrorogin = driver.find_element(By.XPATH, '//*[@id="error"]')
    except:
        checkErrorogin = None

    if (checkErrorogin):
        print("\033[91m[X] Error Message is Displayed \033[0m")
        time.sleep(10)
    else:
        NewUrl = driver.current_url
        if NewUrl == "https://practicetestautomation.com/logged-in-successfully/":
            print("\033[92m[√] Login Passed Successfully\033[0m")
        else:
            print("\033[91m[X] Login Failed\033[0m")
        logOutBtt = driver.find_element(By.XPATH, '//*[@id="loop-container"]/div/article/div[2]/div/div/div/a')

        if (logOutBtt.is_displayed):
            print("\033[92m[√] Logout is Displayed Successfully\033[0m")
        time.sleep(5)
        logOutBtt.click()
        if driver.current_url == "https://practicetestautomation.com/practice-test-login/":
            print("\033[92m[√] Logout Passed Successfully\033[0m")
        else:
            print("\033[91m[X] Logout Failed\033[0m")
        time.sleep(30)    
driver.close()
print("\033[92m[√] Browser Closed Successfully\033[0m")
