import pytest
import allure
import time
from selenium import webdriver
@allure.title("verify that  the current url and title of espocrm is as expected")
def test_espo_crm():
    driver=webdriver.Chrome()
    driver.get("https://demo.us.espocrm.com/")
    print(driver.title)
    assert driver.title=="EspoCRM Demo"
    time.sleep(10)
    print(driver.current_url)
    assert driver.current_url=="https://demo.us.espocrm.com/"