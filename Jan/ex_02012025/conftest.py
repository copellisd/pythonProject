from http.client import responses

import pytest
import requests
from dotenv import load_dotenv
import os

@pytest.fixture()
def create_token():
    load_dotenv()
    username=os.getenv("USERNAME")
    password=os.getenv("PASSWORD")
    print(username,password)
    print("....creating a token.....")
    url="https://restful-booker.herokuapp.com/auth"
    headers={"Content-Type":"application/json"}
    json_payload={
        "username": "admin",
        "password": "password123"

    }
    response=requests.post(url=url,headers=headers,json=json_payload)
    token=response.json()["token"]
    print(token)


@pytest.fixture()
def create_booking_id():
    print(".....create booking id......")
    url="https://restful-booker.herokuapp.com/booking"
    headers={"Content-Type":"application/json"}
    json_payload={

    "firstname": "Susan",
    "lastname": "Brown",
    "totalprice": 856,
    "depositpaid": False,
    "bookingdates": {
        "checkin": "2015-07-05",
        "checkout": "2021-07-06"
    },
    "additionalneeds": "Breakfast"
    }
    response=requests.post(url=url,headers=headers,json=json_payload)
    print(type(url))
    print(type(headers))
    print(type(json_payload))
    data=response.json()
    booking_id=data["bookingid"]
    return booking_id



@pytest.fixture()
def read_csv_file_data():
    pass
def read_mysql_file_database():
    pass
@pytest.fixture()
def read_url_testdata_excel():
    pass