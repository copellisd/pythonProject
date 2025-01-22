import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@allure.title("Demo ESPO_CRM positive Testcase")
@allure.description("TC1 - Positive TC - Verify the Title and current URL.")
@pytest.mark.Positive
def test_verify_title_chrome():

    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://demo.us.espocrm.com/")
    #print(driver.title)
    time.sleep(10)
    assert driver.title=="EspoCRM Demo"
    assert driver.current_url=="https://demo.us.espocrm.com/"

    driver.quit()


@allure.title("Demo ESPO_CRM positive Testcase")
@allure.description("TC2 - Positive TC - Click on login and verify the current page Url")
@pytest.mark.Positive

def test_verify_login_espo_crm():

    chrome_options=Options()
    chrome_options.add_argument("----incognito")
    driver=webdriver.Chrome(chrome_options)
    driver.get("https://demo.us.espocrm.com/")

    #login button
    #<button type="submit"
    # class="btn btn-primary btn-s-wide"
    # id="btn-login">Login
    # </button>

    login_web_element=driver.find_element(By.XPATH,"//button[@id='btn-login']")
    login_web_element.click()
    time.sleep(5)
   # print("Current URL:", driver.current_url)

    assert driver.current_url=="https://demo.us.espocrm.com/?l=en_US"

    driver.quit()

@allure.title("Demo ESPO_CRM Positive Testcase")
@allure.description("TC3 - Positive TC - Click on Advance pack link ")
@pytest.mark.adv_pack
def test_click_adv_pack_chrome():
    driver=webdriver.Chrome()
    driver.get("https://demo.us.espocrm.com/")
    time.sleep(5)

    link_adv_pack=driver.find_element(By.XPATH,"//a[@href='https://www.espocrm.com/extensions/advanced-pack/']")
    link_adv_pack.click()
    time.sleep(5)
    assert driver.current_url=="https://demo.us.espocrm.com/"

    driver.quit()
@allure.title("Demo ESPO_CRM Positive Testcase")
@allure.description("TC4 - Positive TC - Click on Sales pack link ")
@pytest.mark.Positive
def test_click_sales_pack_chrome():
    driver=webdriver.Chrome()
    driver.get("https://demo.us.espocrm.com/")

    link_sales_pack=driver.find_element(By.XPATH,"//a[@href='https://www.espocrm.com/extensions/sales-pack/']")
    link_sales_pack.click()
    time.sleep(5)
    assert driver.current_url=="https://demo.us.espocrm.com/"

    driver.quit()

@allure.title("Demo ESPO_CRM Positive Testcase")
@allure.description("TC5 - Positive TC - Click on personal demo ")
@pytest.mark.demo_espo_crm
def test_click_personal_demo_chrome():

    driver=webdriver.Chrome()
    driver.get("https://demo.us.espocrm.com/")

    link_personal_demo=driver.find_element(By.XPATH,"//a[@href='https://www.espocrm.com/cloud-registration/?plan=demo']")
    link_personal_demo.click()
    time.sleep(5)

    assert driver.current_url=="https://www.espocrm.com/cloud-registration/?plan=demo"
    driver.quit()