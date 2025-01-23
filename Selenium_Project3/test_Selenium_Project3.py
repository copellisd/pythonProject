import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@allure.title("Opencart Registration Account Testing With Selenium_Mini_Project 3 ")
@allure.description("TC1 - Positive TC - Fill the registration form with Valid data and verify whether account created ")
@pytest.mark.Positive
def test_awesome_qa():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")
    #time.sleep(5)
    #firstname element
    ele_firstname=driver.find_element(By.XPATH,"//input[@name='firstname']")
    ele_firstname.send_keys("Preksha")
    #time.sleep(5)
    #last name
    ele_lastname=driver.find_element(By.XPATH,"//input[@name='lastname']")
    ele_lastname.send_keys("Sakhamudi")
    #time.sleep(5)
    #e-mail
    ele_email=driver.find_element(By.XPATH,"//input[@id='input-email']")
    ele_email.send_keys("sruthi.spr18@gmail.com")
    #time.sleep(5)
    #Telephone
    ele_telephone=driver.find_element(By.XPATH,"//input[@id='input-telephone']")
    ele_telephone.send_keys("6829994324")
    #time.sleep(5)
    #password
    ele_password=driver.find_element(By.XPATH,"//input[@name='password']")
    ele_password.send_keys("Sakhamudi@3001")
    #time.sleep(5)
    #confirm password
    ele_confirm_password=driver.find_element(By.XPATH, "//input[@name='confirm']")
    ele_confirm_password.send_keys("Sakhamudi@3001")
    #time.sleep(5)
    #policy checkbox
    policy_checkbox=driver.find_element(By.XPATH,"//input[@name='agree']")
    policy_checkbox.click()
    #time.sleep(5)
    #continue button
    continue_button=driver.find_element(By.XPATH,"//input[@type='submit']")
    continue_button.click()
    time.sleep(5)
    assert driver.current_url=="https://awesomeqa.com/ui/index.php?route=account/success"
    time.sleep(5)
    print("Driver Title "+ driver.title)

    #message_web_element=driver.find_element(By.XPATH,"//div[@id=content]")
    message_web_element = driver.find_element(By.XPATH,
                                             "//div[@id='content']//*[text()='Your Account Has Been Created!']")
    print(message_web_element.text)

    time.sleep(5)
    driver.quit()









