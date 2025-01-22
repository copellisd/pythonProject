import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@allure.title("verify the login of vwo app")
@allure.description("TC1-vwo login with credintials")
def test_vwo_app_login():
    chrome_options=Options()
    chrome_options.add_argument("-----incognito")
    driver=webdriver.Chrome(chrome_options)
    driver.get("https://app.vwo.com/#/login")
    #i need to click that link in vwo app ie  start a free trial
    #<a href="https://vwo.com/free-trial/?utm_medium=website&amp;utm_source=login-page&amp;utm_campaign=mof_eg_loginpage"
    # class="text-link"
    # data-qa="bericafeqo">Start a free trial
    # </a>

    #by linktext-complete n exact match link and partial text -any word match  in that text

    anchor_link_web_element=driver.find_element(By.LINK_TEXT,value="Start a free trial")
    anchor_link_web_element.click()


    assert driver.current_url=="https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"

    time.sleep(20)
    driver.quit()