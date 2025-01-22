import time
from selenium import webdriver
import pytest
import allure

@allure.title("open the app vwo.com")
@pytest.mark.regression
def test_vwo_login():
    driver=webdriver.Chrome()
    #1.this code is translated into API request.
    #2.POST request -to browser driver.
    #3.where it will create a session or fresh copy of browser.
    #4.session id -16 digits
    driver.get("https://app.vwo.com")
    print(driver.session_id)
    #5.GET API  Request to navigate to particular page.
    #6.browser will navigate to the URL
    time.sleep(15)


    #source code(client)->w3c protocol->browser driver(server)->browser
