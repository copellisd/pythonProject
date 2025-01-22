import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_katalon_firefox():
    driver=webdriver.Firefox()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    #<a id="btn-make-appointment"
    # href="./profile.php#login"
    # class="btn btn-dark btn-lg">
    # Make Appointment
    # </a>

    #find element by ID

    make_appointment_element=driver.find_element(By.ID,value="btn-make-appointment")

    #click on it

    make_appointment_element.click()

    # verify that URL change

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    time.sleep(10)
    driver.quit()