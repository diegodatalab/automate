#
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


def main():
    driver =  driver_init()
    element = driver.find_element(By.XPATH, "//h1[@class='animated fadeIn mb-4']")
    return element.text


print(main())

