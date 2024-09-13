import pytest
from requests import Session
from json import loads
session=Session()
@pytest.fixture(scope='function')
def get_token_shopperid():
    print("fixture got called")
    url = "https://www.shoppersstack.com/shopping"
    end_point = "/users/login"
    uri = url + end_point
    """headers"""
    headers = {"content-type": "application/json"}
    """body"""
    payload = {
                "email": "alamsahdab786@gmail.com",
                "password": "Nagma@123",
                "role": "SHOPPER"
              }
    response = session.post(uri, headers=headers, json=payload)
    response_load_into_json=loads(response.text)
    yield response_load_into_json['data']['userId'],response_load_into_json['data']['jwtToken']
    session.close()