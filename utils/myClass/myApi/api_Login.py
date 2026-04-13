from utils.myClass.myApi.base_api import MyRequestsSession
import allure

class LoginRequests(MyRequestsSession):
    @allure.step("receive_code")
    def receive_code(self,res):
         login_json=res.json()
         return login_json.get('code')
    @allure.step("receive_msg")
    def receive_msg(self,res):
        login_json = res.json()
        return login_json.get('msg')
    @allure.step("receive_token")
    def receive_token(self,res):
        login_json = res.json()
        return login_json.get('token')