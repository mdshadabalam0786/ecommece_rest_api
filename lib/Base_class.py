from requests import Session
session=Session()
class Base:
    def __post_requests_(self,url,headers=None,payload=None):
        return session.post(url,headers=headers,json=payload)
    def __get_requests_(self,url,headers,token=None):
        session.headers.update(token)
        return session.get(url,headers=headers)

    def get_response(self,request_type,url,headers=None,payload=None):
        if request_type=="post":
            return self.__post_requests_(url,headers,payload)
        elif request_type=="get":
            return self.__get_requests_(url,headers[0],headers[1])