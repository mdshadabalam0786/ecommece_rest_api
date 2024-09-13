from json import loads

import pytest

from lib.read_excel_data import read_excel

from Api_pages.shopper_profile.shopper_login_api import Shopper_login
@pytest.mark.skip
def test_shopper_login_api():
    p1=Shopper_login()
    """getting response from server"""
    data={
                "email": "alamsahdab786@gmail.com",
                "password": "Nagma@123",
                "role": "SHOPPER"
            }
    loads_response=p1.shopper_login(**data)
    """de-serialization"""
    d1=loads(loads_response.text)
    # print(d1)
    assert loads_response.status_code==200
    assert d1['data']['email']=='alamsahdab786@gmail.com'


def test_shopper_login_api_multiple_credentials_from_excel():
    p1=Shopper_login()
    """reading data from read_excel function"""
    read_excel_data=read_excel()
    email_li=[i for i in read_excel_data['Email']]
    password_li=[i for i in read_excel_data['Password']]
    for email,password in zip(email_li,password_li):
        data = {
            "email": email,
            "password": password,
            "role": "SHOPPER"
             }
        """getting response from server"""
        loads_response=p1.shopper_login(**data)

        """de-serialization"""
        d1=loads(loads_response.text)
        print(d1)
        assert loads_response.status_code==200
        assert d1['data']['email']==email


user="email,password"
data=[("alamsahdab786@gmail.com","Nagma@123"),("sandeepsandy580023@gmail.com","Password@123"),
      ("syedmaheen687@gmail.com","1Cd19ec14$"),("sumanbss21@gmail.com","Saibaba@1528"),
      ("richashrivastava401@gmail.com","Richa@401")]
@pytest.mark.parametrize(user,data)
def test_shopper_login_api_multiple_credentials_from_parameter(email,password):
    p1=Shopper_login()
    data = {
        "email": email,
        "password": password,
        "role": "SHOPPER"
         }
    """getting response from server"""
    loads_response=p1.shopper_login(**data)

    """de-serialization"""
    d1=loads(loads_response.text)
    print(d1)
    assert loads_response.status_code==200
    assert d1['data']['email']==email

