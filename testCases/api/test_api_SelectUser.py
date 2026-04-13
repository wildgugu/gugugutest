import allure
import pytest
from utils.myClass.myApi.api_selectuser import SelectUser
from utils.myYaml.yaml_util import read_paratre


class TestSelectId:
    @pytest.mark.api
    @allure.epic("搭建的网站")
    @allure.feature("用户管理模块")
    @allure.story("查询用户ID接口")
    @allure.title("{aid}")
    @pytest.mark.parametrize('all_dict,aid',read_paratre('docs/Yaml/test_select.yaml'))
    def test_select_userid(self,create_session,have_token,all_dict,aid):
        select=SelectUser(create_session)
        select.sess.headers=all_dict["request"]["headers"]
        if all_dict["request"]["headers"].get("Authorization") is not None:
            select.set_token(have_token)
        res = select.send_all_request(method=all_dict["request"]["method"], url=all_dict["request"]["url"],headers=select.sess.headers, json=all_dict["request"].get("data"),data=all_dict["request"].get("raw"))
        with allure.step("断言"):
            assert select.receive_status_code(res) == all_dict["assert"]["status_code"]
            if select.receive_msg(res) is not None:
                assert select.receive_msg(res) == all_dict["assert"]["msg"]
            if select.receive_code(res) is not None:
                assert select.receive_code(res) == all_dict["assert"]["code"]
            if select.receive_code(res) == 200:
                assert select.receive_roleIds(res) is not None
            else:
                assert select.receive_roleIds(res) is None