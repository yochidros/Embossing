from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary

chrome_path = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'
def testChromeHeadless():
    options = Options()
    options.binary_location = chrome_path
    options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=options)

    driver.get("https://www.google.co.jp")
    html = driver.page_source

    print(html)

    driver.quit()


if __name__ == '__main__':
    testChromeHeadless()