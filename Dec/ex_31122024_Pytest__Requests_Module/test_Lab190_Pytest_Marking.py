import  pytest
import allure
import requests

@allure.title("tc#1 verify that 2-2=0")
@allure.description("this testcase is to check basic math")
@pytest.mark.smoke
def test_basicmath():
    assert 2-2==0

@allure.title(" #verify that 3-3=0")
@allure.description("this smoke testcase is to check basic math")
@pytest.mark.regression
def test_sub1():
    assert 2-2==0

@allure.title("verify that 1-1=0")
@allure.description("this regression testcase is to check basic math")
@pytest.mark.smoke
def test_sub2():
    assert 2-2==0

@pytest.mark.skip(reason="not working ,skip it")
def test_sub3():
    assert 0-0!=0

