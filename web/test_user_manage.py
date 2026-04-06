import csv
from typing import Dict
import pytest
import json
from conftest import LoginPage

def read_autocsv1(filepath):
    with open(filepath,'r',encoding='utf8') as f:
        reader = csv.DictReader(f)
        for index,include in enumerate(reader):
            if 0<=index<=7:
                yield pytest.param(include['测试输入'],include['预期结果'],id=include['测试标题'])

@pytest.mark.parametrize('input,my_expect',read_autocsv1('自动化测试用例.csv'))
def test_login(login_page,chrome_context,input,my_expect):
    dict_input:Dict[str]=json.loads(input)
    my_login_page=LoginPage(login_page)
    my_login_page.login(dict_input.get("zh"),dict_input.get("pwd"),dict_input.get("flag"))
    my_login_page.login_click()
    my_login_page.get_simple_assert(my_expect)