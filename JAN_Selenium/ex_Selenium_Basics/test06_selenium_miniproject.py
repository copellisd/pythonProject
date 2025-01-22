#checking the content is exist in the particular site
import pytest
import allure
from selenium import webdriver
import time
def test_vwo_sample():
    driver=webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    if "CURA Healthcare Service" in driver.page_source:
        print("text found! test case passed")
    else:
        print("test not found on the page")
        pytest.fail("testcase failed")