import allure
import requests
from requests import Session


class MyRequestsSession:
    def __init__(self,session:Session):
     self.sess=session
    @allure.step("send_all_request")
    def send_all_request(self,**kwargs):
         res=self.sess.request(**kwargs)
         return res
    @allure.step("receive_json")
    def receive_json(self,res):
         return res.json()
    @allure.step("receive_status_code")
    def receive_status_code(self,res):
         return res.status_code
    @allure.step("receive_headers")
    def receive_headers(self,res):
         return res.headers
    @allure.step("receive_text")
    def receive_text(self,res):
         return res.text



class MyRequestsNoSession:
    @staticmethod
    @allure.step("send_all_request")
    def send_all_request(**kwargs):
         res=requests.request(**kwargs)
         return res
    @staticmethod
    @allure.step("receive_json")
    def receive_json(res):
         return res.json()

    @staticmethod
    @allure.step("receive_status_code")
    def receive_status_code(res):
        return res.status_code

    @staticmethod
    @allure.step("receive_headers")
    def receive_headers(res):
        return res.headers

    @staticmethod
    @allure.step("receive_text")
    def receive_text(res):
        return res.text
