from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

PATH = "C:/Program Files (x86)/chromedriver.exe"

driver = webdriver.Chrome(PATH, chrome_options=chrome_options)

driver.get("https://www.indiatimes.com/")
# For maximizing window
driver.maximize_window()

driver.implicitly_wait(5)

search = None

lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);"
                                  "var lenOfPage=document.body.scrollHeight;"
                                  "return lenOfPage;")
match = False

while match is False:
    lastCount = lenOfPage
    # time.sleep(3)
    search = driver.find_element(by=By.LINK_TEXT, value="Terms & Conditions")
    search.send_keys(Keys.PAGE_DOWN)
    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);"
                                      "var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match = True

print(search.text)

search.click()

driver.p