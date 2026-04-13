import allure

from utils.myClass.myApi.base_api import MyRequestsSession

class SelectUser(MyRequestsSession):
    @allure.step('传递token')
    def set_token(self,token):
        self.sess.headers['Authorization']=token
    @allure.step('receive_code')
    def receive_code(self,res):
         login_json=res.json()
         return login_json.get('code')
    @allure.step('receive_msg')
    def receive_msg(self,res):
        login_json = res.json()
        return login_json.get('msg')
    @allure.step('receive_roleIds')
    def receive_roleIds(self,res):
        login_json = res.json()
        return login_json.get('roleIds')