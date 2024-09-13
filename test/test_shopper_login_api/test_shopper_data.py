from json import loads
from Api_pages.shopper_profile.shopper_data_find import Shopper_Data
def test_shopper_data(get_token_shopperid):
    p1=Shopper_Data()
    response=p1.get_shopper_details(get_token_shopperid[0],get_token_shopperid[1])
    """de serialization"""
    li=loads(response.text)
    print(li)