import  pytest
import allure
import requests


@allure.title("TC#1-create booking CRUD positive")
@allure.description(" verift the create booking")
@pytest.mark.crud
def test_create_booking_positive():
    base_url="https://restful-booker.herokuapp.com"
    base_path_post="/booking"
    full_url=base_url+base_path_post
    headers={
          "Content-Type":"application/json"
            }
    payload={
        "firstname": "jim",
        "lastname": "brown",
        "totalprice": 111,
        "depositpaid":True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response_data=requests.post(url=full_url,headers=headers,json=payload)
    #statuscode_veification
    assert response_data.status_code==200

    #booking_id>0,firstname==jim

    response_data_json=response_data.json()
    bookingid=response_data_json["bookingid"]
    print(bookingid)
    assert bookingid is not None
    assert bookingid>0
    assert type(bookingid)==int

    firstname=response_data_json["booking"]["firstname"]
    lastname=response_data_json["booking"]["lastname"]
    totalprice=response_data_json["booking"]["totalprice"]
    depositpaid=response_data_json["booking"]["depositpaid"]

    assert type(firstname)==str
    assert lastname=="brown"
    assert totalprice==111
    assert depositpaid==True

    checkin = response_data_json["booking"]["bookingdates"]["checkin"]
    checkout = response_data_json["booking"]["bookingdates"]["checkout"]
    assert checkin=="2018-01-01"
    assert checkout=="2019-01-01"
    time=response_data.elapsed.total_seconds()
    assert time<3

@allure.title("TC#1-create booking CRUD positive")
@allure.description(" verift the create booking")
@pytest.mark.crud
def test_create_booking_negative():
    base_url = "https://restful-booker.herokuapp.com"
    base_path_post = "/booking"
    full_url = base_url + base_path_post
    headers = {
        "Content-Type": "application/json"
    }
    json_payload={}
    response=requests.post(url=full_url,headers=headers,json=json_payload)
    assert response.status_code==500
    print(response.text)
    assert response.text=="internal server error"



