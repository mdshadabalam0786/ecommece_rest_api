from lib.Base_class import Base


class Shopper_login:
    def shopper_login(self,**data):
        url = "https://www.shoppersstack.com/shopping"
        end_point = "/users/login"
        uri = url + end_point
        """headers"""
        headers={"content-type":"application/json"}
        """body"""
        payload=data
        test_shopper=Base()
        response=test_shopper.get_response("post",uri,headers,payload)
        return response

