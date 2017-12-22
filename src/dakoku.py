import os, sys, time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys as Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def scraping(url):
    driver = webdriver.PhantomJS(service_log_path=os.path.devnull)

    driver.get(url)

    # get element input company id
    input_company = driver.find_element_by_id('client_id')
    # get element input email
    input_email = driver.find_element_by_id('email')
    # get element input password
    input_password = driver.find_element_by_id('password')

    #send infomation
    input_company.send_keys('Nagisa')
    input_email.send_keys('miyazawa@nagisa-inc.jp')
    input_password.send_keys('J1DvhNxt')
    
    # push button
    input_password.send_keys(Keys.ENTER)

    WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'aditBtn'))
    )
    driver.save_screenshot('entrance.png')
    button = driver.find_element_by_class_name('aditBtn')
    button.click()

    time.sleep(2)
    driver.save_screenshot('result.png')
    
    driver.close()
    print('end')
    sys.exit(0)


if __name__ == '__main__':
    url = 'https://ssl.jobcan.jp/login/pc-employee/'
    scraping(url)
