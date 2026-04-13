import allure
import pytest
import requests

from utils.myClass.myApi.api_Login import LoginRequests
from utils.myYaml.yaml_util import read_paratre


class TestLogin:
    @pytest.mark.api
    @allure.epic("搭建的网站")
    @allure.feature("登录模块")
    @allure.story("登录接口")
    @allure.title("{aid}")
    @pytest.mark.parametrize('all_dict,aid',read_paratre('docs/Yaml/test_login.yaml'))
    def test_login(self,create_session,all_dict,aid):
        login = LoginRequests(create_session)
        res=login.send_all_request(method=all_dict["request"]["method"],url=all_dict["request"]["url"],headers=all_dict["request"]["headers"],json=all_dict["request"].get("data"),data=all_dict["request"].get("raw"))
        with allure.step("断言"):
            assert login.receive_status_code(res)==all_dict["assert"]["status_code"]
            if login.receive_msg(res) is not None:
                assert login.receive_msg(res)==all_dict["assert"]["msg"]
            if login.receive_code(res) is not None:
                assert login.receive_code(res)==all_dict["assert"]["code"]
            if login.receive_code(res) ==200:
                assert login.receive_token(res) is not None
            else:
                assert login.receive_token(res) is None
