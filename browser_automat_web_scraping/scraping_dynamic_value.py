#
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://automated.pythonanywhere.com"

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


def clean_text(text):
    """extract only the temperature from text"""
    output = float(text.split(": ")[1])
    return output


def main():
    driver =  driver_init()
    time.sleep(2)
    element = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/h1[2]/div[1]")
    return clean_text(element.text)


print(main())

