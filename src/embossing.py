import os, sys, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys as Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def _embossing(url, info):
    driver = webdriver.PhantomJS(service_log_path=os.path.devnull)

    driver.get(url)

    # get element input company id
    input_company = driver.find_element_by_id('client_id')
    # get element input email
    input_email = driver.find_element_by_id('email')
    # get element input password
    input_password = driver.find_element_by_id('password')

    # send infomation
    input_company.send_keys(info[0])
    input_email.send_keys(info[1])
    input_password.send_keys(info[2])
    
    # push button
    input_password.send_keys(Keys.ENTER)

    WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'aditBtn'))
    )
    button = driver.find_element_by_class_name('aditBtn')
    button.click()

    time.sleep(2)
    
    driver.close()
    return True


def applyEmbossing(info):
    url = 'https://ssl.jobcan.jp/login/pc-employee/'
    return _embossing(url, info)
