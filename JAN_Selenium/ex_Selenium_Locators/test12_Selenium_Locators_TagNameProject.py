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

   #i want to find the all links in  the page

    all_links_page=driver.find_elements(By.TAG_NAME,value="a")
    print(len(all_links_page))

    for i in all_links_page:
        print(i.text)
        if "Start a free trail" in i.text:
            i.click()

    time.sleep(20)
    driver.quit()