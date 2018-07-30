import os, sys, time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys as Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import chromedriver_binary

__url = 'https://ssl.jobcan.jp/login/pc-employee/'


def __capture(driver):
    driver.get('https://ssl.jobcan.jp/employee/attendance')

    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'page-title'))
        )
    except TimeoutException as error:
        print('Error: couldn\'t load page.')
        driver.close()
        return False

    driver.save_screenshot('attendance.png')

    driver.close()
    return True


def capture_Attendance(info):
    driver = __login(__url, info)
    if driver is None:
        return False
    else:
        return __capture(driver)

_chrome_path = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'

def __login(url, info):
    # driver = webdriver.PhantomJS(service_log_path=os.path.devnull)
    options = Options()
    options.binary_location = _chrome_path
    options.add_argument('--headless')
    options.add_argument('window-size=1980,2400')
    driver = webdriver.Chrome(chrome_options=options)

    driver.get(url)
    try:
        # get element input company id
        input_company = driver.find_element_by_id('client_id')
        # get element input email
        input_email = driver.find_element_by_id('email')
        # get element input password
        input_password = driver.find_element_by_id('password')
    except NoSuchElementException as error:
        driver.close()
        print('Error: couldn\'t get page infomation')
        sys.exit(1)

    # send infomation
    input_company.send_keys(info[0].decode())
    input_email.send_keys(info[1].decode())
    input_password.send_keys(info[2].decode())

    # push button
    input_password.send_keys(Keys.ENTER)
    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'aditBtn'))
        )
    except TimeoutException as error:
        print(error)
        driver.close()
        driver = None
        return driver

    return driver


def __embossing(driver):

    button = driver.find_element_by_class_name('aditBtn')
    button.click()

    time.sleep(2)

    driver.close()
    return True


def applyEmbossing(info):
    driver = __login(__url, info)
    if driver is None:
        return False
    else:
        return __embossing(driver)
