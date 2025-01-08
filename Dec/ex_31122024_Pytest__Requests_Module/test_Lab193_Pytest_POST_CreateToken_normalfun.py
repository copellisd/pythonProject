import  pytest
import allure
import requests
from six import assertNotRegex

base_url="https://restful-booker.herokuapp.com"
headers = {"Content-Type": "application/json"}


def get_token():
    #base_url="https://restful-booker.herokuapp.com"
    base_path="/auth"
    full_url=base_url+base_path
    #headers={"Content-Type":"application/json"}
    json_payload_auth ={
        "username": "admin",
        "password": "password123"
    }
    response_data=requests.post(url=full_url,headers=headers,json=json_payload_auth)
    print(response_data)
    assert response_data.status_code==200

    response_data_json=response_data.json()
    token=response_data_json["token"]
    print(token)
    assert type(token)==str
    assert len(token)>0
    return token

def get_booking_id():
   # base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    full_url = base_url + base_path
    print(full_url)
    #headers = {"Content-Type": "application/json"}
    json_payload={
        "firstname": "amit",
        "lastname": "brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"

    }
    response_data=requests.post(url=full_url,headers=headers,json=json_payload)
    response_data_json=response_data.json()
    bookingid=response_data_json["bookingid"]
    return bookingid

def test_put_request():
    token=get_token()
    bookingid=get_booking_id()
    print(token)
    print(bookingid)
    base_path="/booking"+str(bookingid)
    full_url_put=base_url+base_path
    cookie="token"+token
    headers={
       "Content-type":"application/json",
        "cookie":cookie
    }

    json_payload={
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response_data=requests.put(url=full_url_put,headers=headers,json=json_payload)
    assert response_data.status_code==200
    assert response_data.json()["firstname"]=="James"

def test_delete():
    URL="https://restful-booker.herokuapp.com/booking/"
    bookingid=get_booking_id()
    DELETE_URL=URL+str(bookingid)
    cookie="token"+get_token()
    headers={
        "Content-type": "application/json",
        "cookie": cookie
    }
    response=requests.delete(url=DELETE_URL,headers=headers)
    assert response.status_code==201





