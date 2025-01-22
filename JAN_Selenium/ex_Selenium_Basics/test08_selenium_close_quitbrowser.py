import pytest
import allure
from selenium import webdriver
import time

def test_katalon_firefox():
    driver=webdriver.Firefox()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/"
    time.sleep(10)
    #driver.close() #close means close the current window
    driver.quit() #close the current window n associated windows.danitho patu unnavi kuda close avtuyi
