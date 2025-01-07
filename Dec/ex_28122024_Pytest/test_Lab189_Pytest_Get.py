import pytest
import allure
import requests

@allure.title("verify the get request of restful booker")
@allure.description("this test case is checking the booking id and verify the response  ")
def test_get_request_positive():
    URL="https://restful-booker.herokuapp.com/booking/1"
    response_data=requests.get(url=URL)
    #print(response_data.text)
    assert response_data.status_code==200

@allure.title("verify the get request of restful booker")
@allure.description("this test case is checking the booking id  -1 and verify the response  ")
def test_get_request_negative():
    URL="https://restful-booker.herokuapp.com/booking/1"
    response_data=requests.get(url=URL)
    #print(response_data.text)
    assert response_data.status_code==404




