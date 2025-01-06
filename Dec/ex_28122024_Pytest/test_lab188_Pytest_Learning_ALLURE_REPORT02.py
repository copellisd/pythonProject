import allure
def method1():
    print("this is not pytest method")

#pytest method
@allure.title("create booking with valid data is working")
@allure.description("this test case is checking for positive create booking  ")
def test_create_booking_positive():
    print("testcase1")
    assert 1-1==2
@allure.title("create booking with inpytest valid data is working")
@allure.description("this test case is checking for negative create booking  ")
def test_create_booking_negative_1():
    print("test case2")
    assert 1+1 ==2
@allure.title("create booking with invalid data is working")
@allure.description("this test case is checking for negative create booking  ")
def test_create_booking_negative_2():
    print("test case2")
    assert 1+1 ==2