import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service


url = "http://automated.pythonanywhere.com/login/"

def driver_init():
    service = Service()
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars')
    options.add_argument('start-maximized')
    options.add_argument('disable-dev-shm-usage') # special for linux
    options.add_argument('no-sandbox')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument('disable-blink-features=AutomationControlled')
    
    
    driver = webdriver.Chrome(service=service, options=options)
    
    driver.get(url)

    return driver


def snippet(patch):
    output = patch.split(':')[1]
    return output


def main():
    driver =  driver_init()
    driver.find_element(By.ID, "id_username").send_keys('automated')
    time.sleep(2)
    driver.find_element(By.ID, "id_password").send_keys('automatedautomated' + Keys.RETURN)
    time.sleep(2)
    element = driver.find_element(By.XPATH, "//div[@class='text-success']")
    return snippet(element.text)
        

print(main())
