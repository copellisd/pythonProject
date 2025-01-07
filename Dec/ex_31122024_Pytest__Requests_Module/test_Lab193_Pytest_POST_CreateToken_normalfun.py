import  pytest
import allure
import requests

def get_token():
    base_url="https://restful-booker.herokuapp.com"
    base_path="/auth"
    full_url=base_url+base_path
    headers={"Content-Type":"application/json"}
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
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    full_url = base_url + base_path
    print(full_url)
    headers = {"Content-Type": "application/json"}
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




