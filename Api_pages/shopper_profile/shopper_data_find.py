from lib.Base_class import Base
class Shopper_Data:
    def get_shopper_details(self,shopperId,tokenNo):
        url="https://www.shoppersstack.com/shopping"
        end_points=f'/shoppers/{shopperId}'
        uri=url+end_points
        headers={"content-type":"application/json"}
        token={"Authorization": f"Bearer {tokenNo}"}
        # "Authorization": f"Bearer {getKeyShopperId[0]}"}
        p1=Base()
        response=p1.get_response("get",uri,(headers,token))
        return response

