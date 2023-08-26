#
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


url = "http://automated.pythonanywhere.com/login/"


def driver_init():
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars')
    options.add_argument('start-maximized')
    options.add_argument('disable-dev-shm-usage') # special for linux
    options.add_argument('no-sandbox')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument('disable-blink-features=AutomationControlled')
    
    driver = webdriver.Chrome(options=options)
    
    driver.get(url)

    return driver


def main():
    driver =  driver_init()
    driver.find_element(By.ID, "id_username").send_keys('automated')
    time.sleep(2)
    driver.find_element(By.ID, "id_password").send_keys('automatedautomated' + Keys.RETURN)
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/nav/div/a").click()
    print(driver.current_url)
    


print(main())

