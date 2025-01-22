
import time
import pytest
import allure
from selenium import webdriver
@allure.title("verift that title of the vwo app")
def test_vwo_sample():
    driver=webdriver.Edge()
    driver.get("https://app.vwo.com")
    print(driver.title)
    assert driver.title=="Login - VWO"
