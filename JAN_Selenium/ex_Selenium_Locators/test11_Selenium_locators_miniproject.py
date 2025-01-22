import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options



@allure.title("vwo login negative testcase")
@allure.description("TC1- VWO-LOGIN-negative testcase  with invalid data")
def test_vwo_chrome():

    chrome_options=Options()
    chrome_options.add_argument("--incognito")
    driver=webdriver.Chrome(chrome_options)
    driver.get("https://app.vwo.com/#/login")

#--------Usename Inspect----------------------------
    #<input type="email"
    # class="text-input W(100%)"
    # name="username"
    # id="login-username"
    # data-qa="hocewoqisi"
    # >
    email_web_element=driver.find_element(By.ID,value="login-username")
    email_web_element.send_keys("abc@gmail.com")

#----------------------password inspect-------------------------------

    #<input type="password"
    # class="text-input W(100%)"
    # name="password"
    # id="login-password"
    # data-qa="jobodapuxe">

    pwd_web_element=driver.find_element(By.NAME,value="password")
    pwd_web_element.send_keys("password@123")

#----------SUBMIT BUTTON INSPECT--------------------------
    #<button
    # type="submit"
    # id="js-login-btn"
    # class="btn btn--positive btn--inverted W(100%) H(48px) Fz(16px)"
    # onclick="login.login(event)"
    # data-qa="sibequkica">
    #<span class="icon loader hidden" data-qa="zuyezasugu"></span>
	#<span data-qa="ezazsuguuy">Sign in</span>
	#</button>

    submit_button_web_element=driver.find_element(By.ID,value="js-login-btn")
    submit_button_web_element.click()

    #waiting time
    time.sleep(3)

    #for the o/p of clicking submit button,we got o/p uname and  pwd does not match
    #<div class="notification-box-description"
    # id="js-notification-box-msg"
    # data-qa="rixawilomi">
    # Your email, password, IP address or location did not match
    # </div>

    error_message_web_element=driver.find_element(By.CLASS_NAME,value="notification-box-description")
    print(error_message_web_element.text)

    time.sleep(60)
    driver.quit()