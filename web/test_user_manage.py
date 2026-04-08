import csv,pytest,json,allure
from operator import contains
from typing import Dict
from playwright.sync_api import expect

import mydomain
from conftest import LoginPage, UserManager, select_a_man


def select_user_nick(cursor,zh,nickname):
    cursor.execute("select user_id,user_name,nick_name from sys_user where user_name=%s And nick_name=%s",(zh, nickname))
def select_id_nick(cursor,uid,nickname):
    cursor.execute("select user_id,user_name,nick_name from sys_user where user_id=%s And nick_name=%s",(uid, nickname))
def read_autocsv01(filepath,*num,left=None,right=None):
    with open(filepath,'r',encoding='utf8') as f:
        reader = csv.DictReader(f)
        for index,include in enumerate(reader):
            if left  is not None and right is not None:
                if left<=index<=right:
                    name=include['用例编号']+include['测试标题']
                    yield pytest.param(include['测试输入'],include['预期结果'],id=name)
            else:
                if index in num:
                    name = include['用例编号'] + include['测试标题']
                    yield pytest.param(include['测试输入'], include['预期结果'], id=name)

def read_autocsv02(filepath,*num,left=None,right=None):
    with open(filepath,'r',encoding='utf8') as f:
        reader = csv.DictReader(f)
        for index,include in enumerate(reader):
            if left is not None and right is not None:
                if left <= index <= right:
                    name = include['用例编号'] + include['测试标题']
                    yield pytest.param(include['测试输入'], id=name)
            else:
                if index in num:
                    name = include['用例编号'] + include['测试标题']
                    yield pytest.param(include['测试输入'], id=name)



@pytest.mark.web
@allure.epic("搭建的网站")
@allure.feature("登录模块")
@allure.story("登录功能")
@allure.title("{id}")
@pytest.mark.parametrize('my_input,my_expect',read_autocsv01('自动化测试用例.csv',left=0,right=7))
def test_login01(my_traces,login_page,my_input,my_expect):
    dict_input:Dict[str]=json.loads(my_input)
    my_login_page=LoginPage(login_page)
    my_login_page.login(dict_input.get("zh"),dict_input.get("pwd"),dict_input.get("flag"))
    my_login_page.login_click()
    my_login_page.get_simple_assert(my_expect)

@pytest.mark.web
@allure.epic("搭建的网站")
@allure.feature("登录模块")
@allure.story("登录功能")
@allure.title("{id}")
@pytest.mark.parametrize("my_input",read_autocsv02('自动化测试用例.csv',8))
def test_login02(my_traces,login_page,my_input):
    dict_input: Dict[str] = json.loads(my_input)
    my_login_page = LoginPage(login_page)
    my_login_page.login(dict_input.get("zh"), dict_input.get("pwd"), dict_input.get("flag"))
    expect(my_login_page.password).to_have_attribute("type","password")

@pytest.mark.web
@allure.epic("搭建的网站")
@allure.feature("登录模块")
@allure.story("登录功能")
@allure.title("{id}")
@pytest.mark.parametrize("no",[None],ids=['login-027页面显示正常'])
def test_login03(my_traces,login_page,no):
    my_login_page = LoginPage(login_page)
    expect(my_login_page.username).to_be_visible()
    expect(my_login_page.password).to_be_visible()
    expect(my_login_page.login_button).to_be_visible()
    expect(my_login_page.username).to_be_editable()
    expect(my_login_page.password).to_be_editable()
    expect(my_login_page.login_button).to_be_enabled()


@pytest.mark.web
@allure.epic("搭建的网站")
@allure.feature("登录模块")
@allure.story("登录功能")
@allure.title("{id}")
@pytest.mark.parametrize("my_input",read_autocsv02('自动化测试用例.csv',10))
def test_login04(my_traces,login_page,my_input):
    dict_input: Dict[str] = json.loads(my_input)
    my_login_page = LoginPage(login_page)
    my_login_page.login(dict_input.get("zh"), dict_input.get("pwd"), dict_input.get("flag"))
    my_login_page.login_click()
    UserManager(my_login_page.page).exit_ry()
    my_login_page.login(dict_input.get("zh"), dict_input.get("pwd"), dict_input.get("flag"))
    my_login_page.login_click()
    UserManager(login_page).get_simple_assert("若依后台管理框架")

@pytest.mark.web
@allure.epic("搭建的网站")
@allure.feature("登录模块")
@allure.story("登录功能")
@allure.title("{id}")
@pytest.mark.parametrize("my_input",read_autocsv02('自动化测试用例.csv',11))
def test_login05(new_chrome,chrome_context,login_page,my_input):
    dict_input: Dict[str] = json.loads(my_input)
    my_login_page = LoginPage(login_page)
    my_login_page.login(dict_input.get("zh"), dict_input.get("pwd"), dict_input.get("flag"))
    my_login_page.login_click()
    login_page.wait_for_load_state('networkidle')
    UserManager(login_page).get_simple_assert("若依后台管理框架")
    chrome_context.storage_state(path='web/cache/auth.json')
    chrome_context.close()
    my_context=new_chrome.new_context(storage_state='web/cache/auth.json')
    again_page=my_context.new_page()
    again_page.goto(f"http://{mydomain.domain}")
    UserManager(again_page).get_simple_assert("若依后台管理框架")

@pytest.mark.web
@allure.epic("搭建的网站")
@allure.feature("登录模块")
@allure.story("登录功能")
@allure.title("{id}")
@pytest.mark.parametrize('my_input,my_expect',read_autocsv01('自动化测试用例.csv',12))
def test_login06(my_traces,login_page,my_input,my_expect):
    dict_input:Dict[str]=json.loads(my_input)
    my_login_page=LoginPage(login_page)
    my_login_page.shua_xin()
    my_login_page.login(dict_input.get("zh"),dict_input.get("pwd"),dict_input.get("flag"))
    my_login_page.login_click()
    my_login_page.get_simple_assert(my_expect)

@pytest.mark.web
@allure.epic("搭建的网站")
@allure.feature("登录模块")
@allure.story("登录功能")
@allure.title("{id}")
@pytest.mark.parametrize('my_input',read_autocsv02('自动化测试用例.csv',13))
def test_login07(my_traces,login_page,my_input):
    dict_input:Dict[str]=json.loads(my_input)
    my_login_page=LoginPage(login_page)
    my_login_page.login(dict_input.get("zh"),dict_input.get("pwd"),dict_input.get("flag"))
    my_login_page.login_click()
    my_login_page.shua_xin()
    expect(my_login_page.password).to_have_value("")
    expect(my_login_page.username).to_have_value("")
    expect(my_login_page.remember).not_to_be_checked()

@pytest.mark.web
@allure.epic("搭建的网站")
@allure.feature("登录模块")
@allure.story("登录功能")
@allure.title("{id}")
@pytest.mark.parametrize('my_input',read_autocsv02('自动化测试用例.csv',14))
def test_login08(my_traces,login_page,my_input):
    dict_input:Dict[str]=json.loads(my_input)
    my_login_page=LoginPage(login_page)
    my_login_page.login(dict_input.get("zh"),dict_input.get("pwd"),dict_input.get("flag"))
    my_login_page.login_click()
    my_login_page.back()
    UserManager(login_page).get_simple_assert("若依后台管理框架")

@pytest.mark.web
@allure.epic("搭建的网站")
@allure.feature("登录模块")
@allure.story("登录功能")
@allure.title("{id}")
@pytest.mark.parametrize("my_input",read_autocsv02('自动化测试用例.csv',15,16))
def test_login09(my_traces,login_page,my_input):
    dict_input: Dict[str] = json.loads(my_input)
    my_login_page = LoginPage(login_page)
    my_login_page.back()
    my_login_page.foward()
    my_login_page.login(dict_input.get("zh"), dict_input.get("pwd"), dict_input.get("flag"))
    my_login_page.login_click()
    if dict_input.get("zh")=="admin":
        UserManager(login_page).get_simple_assert("若依后台管理框架")
    if dict_input.get("zh")=="ad min":
        my_login_page.get_simple_assert("用户不存在/密码错误")

@pytest.mark.web
@allure.epic("搭建的网站")
@allure.feature("登录模块")
@allure.story("登录功能")
@allure.title("{id}")
@pytest.mark.parametrize("my_input",read_autocsv02('自动化测试用例.csv',17))
def test_login10(chrome_context,my_traces,login_page,my_input):
    dict_input: Dict[str] = json.loads(my_input)
    my_login_page = LoginPage(login_page)
    my_login_page.login(dict_input.get("zh"), dict_input.get("pwd"), dict_input.get("flag"))
    my_login_page.login_click()
    my_login_page.page.wait_for_load_state('networkidle')
    np=chrome_context.new_page()
    np.goto(f"http://{mydomain.domain}/login")
    UserManager(np).exit_ry()
    LoginPage(np).shua_xin()
    my_login_page.shua_xin()
    LoginPage(np).get_simple_assert("登 录")
    my_login_page.get_simple_assert("登 录")

@pytest.mark.web
@allure.epic("搭建的网站")
@allure.feature("用户管理模块")
@allure.story("新增功能")
@allure.title("{id}")
@pytest.mark.parametrize("my_input",read_autocsv02('自动化测试用例.csv',18,19,25))
def test_manage01(my_traces,user_manage_page,select_a_man,my_input):
    my_cursor=select_a_man
    dict_input: Dict[str] = json.loads(my_input)
    my_manage_page = UserManager(user_manage_page)
    my_add=my_manage_page.click_adduser()
    my_add.fill_base_info(dict_input.get("nickname"),dict_input.get("zh"),dict_input.get("pwd"))
    my_add.add_dept(dict_input.get("department"))
    my_add.add_note(dict_input.get("remark"))
    my_add.add_post(dict_input.get("post"))
    my_add.add_password(dict_input.get("pwd"))
    my_add.add_career(dict_input.get("role"))
    my_add.add_email(dict_input.get("email"))
    my_add.add_phone(dict_input.get("phone"))
    my_add.add_gender(dict_input.get("gender"))
    my_add.confirm_click()
    if dict_input.get("gender") is not None:
        my_manage_page.get_simple_assert(dict_input.get("phone"))
        select_user_nick(my_cursor, dict_input.get("zh"), dict_input.get("nickname"))
        alist = my_cursor.fetchall()
        assert len(alist)>0
    else:
        my_manage_page.get_simple_assert(dict_input.get("zh"))
        select_user_nick(my_cursor, dict_input.get("zh"), dict_input.get("nickname"))
        alist = my_cursor.fetchall()
        assert len(alist) > 0

@pytest.mark.web
@allure.epic("搭建的网站")
@allure.feature("用户管理模块")
@allure.story("新增功能")
@allure.title("{id}")
@pytest.mark.parametrize("my_input",read_autocsv02('自动化测试用例.csv',20))
def test_manage02(my_traces,user_manage_page,select_a_man,my_input):
    my_cursor = select_a_man
    dict_input: Dict[str] = json.loads(my_input)
    my_manage_page = UserManager(user_manage_page)
    my_add = my_manage_page.click_adduser()
    my_add.fill_base_info(dict_input.get("nickname"), dict_input.get("zh"), dict_input.get("pwd"))
    my_add.stop("stop")
    my_add.confirm_click()
    my_manage_page.get_simple_assert(dict_input.get("zh"))
    expect(my_manage_page.page.locator("//tbody/*[2]/*[contains(@class,'column_7')]").get_by_role("checkbox")).not_to_be_checked()
    select_user_nick(my_cursor, dict_input.get("zh"), dict_input.get("nickname"))
    alist = my_cursor.fetchall()
    assert len(alist) > 0

@pytest.mark.web
@allure.epic("搭建的网站")
@allure.feature("用户管理模块")
@allure.story("新增功能")
@allure.title("{id}")
@pytest.mark.parametrize("my_input",read_autocsv02('自动化测试用例.csv',21))
def test_manage03(my_traces,user_manage_page,select_a_man,my_input):
    my_cursor = select_a_man
    dict_input: Dict[str] = json.loads(my_input)
    my_manage_page = UserManager(user_manage_page)
    my_add = my_manage_page.click_adduser()
    my_add.fill_base_info(dict_input.get("nickname"), dict_input.get("zh"), dict_input.get("pwd"))
    my_add.cancel_click()
    expect(my_manage_page.page.get_by_text(dict_input.get("zh"))).not_to_be_visible()
    select_user_nick(my_cursor, dict_input.get("zh"), dict_input.get("nickname"))
    alist = my_cursor.fetchall()
    assert len(alist) == 0


@pytest.mark.web
@allure.epic("搭建的网站")
@allure.feature("用户管理模块")
@allure.story("新增功能")
@allure.title("{id}")
@pytest.mark.parametrize("my_input",read_autocsv02('自动化测试用例.csv',22))
def test_manage04(my_traces,user_manage_page,my_input):
    dict_input: Dict[str] = json.loads(my_input)
    my_manage_page = UserManager(user_manage_page)
    my_add = my_manage_page.click_adduser()
    my_add.add_user_nickname(dict_input.get("nickname"))
    my_manage_page.shua_xin()
    expect(my_manage_page.page.get_by_text(dict_input.get("nickname"))).not_to_be_visible()

@pytest.mark.web
@allure.epic("搭建的网站")
@allure.feature("用户管理模块")
@allure.story("新增功能")
@allure.title("{id}")
@pytest.mark.parametrize("my_input,msg",read_autocsv01('自动化测试用例.csv',23,24))
def test_manage05(my_traces,user_manage_page,select_a_man,my_input,msg):
    dict_input: Dict[str] = json.loads(my_input)
    my_manage_page = UserManager(user_manage_page)
    my_add = my_manage_page.click_adduser()
    my_add.fill_base_info(dict_input.get("nickname"), dict_input.get("zh"), dict_input.get("pwd"))
    my_add.stop(dict_input.get("status"))
    my_add.confirm_click()
    my_manage_page.exit_ry()
    LoginPage(user_manage_page).login(dict_input.get("zh"),dict_input.get("pwd"))
    LoginPage(user_manage_page).login_click()
    if dict_input.get("status"):
        LoginPage(user_manage_page).get_simple_assert(msg)
    else:
        my_manage_page.get_simple_assert("您的密码")

@pytest.mark.test
@allure.epic("搭建的网站")
@allure.feature("用户管理模块")
@allure.story("新增功能")
@allure.title("{id}")
@pytest.mark.parametrize("my_input",read_autocsv02('自动化测试用例.csv',26))
def test_manage06(my_traces,user_manage_page,select_a_man,my_input):
    my_cursor = select_a_man
    dict_input: Dict[str] = json.loads(my_input)
    my_manage_page = UserManager(user_manage_page)
    my_add = my_manage_page.click_adduser()
    my_add.fill_base_info(dict_input.get("nickname"), dict_input.get("zh"), dict_input.get("pwd"))
    my_add.confirm.dblclick()
    my_manage_page.get_simple_assert("数据正在处理")
    my_manage_page.get_simple_assert("请勿重复提交")
    expect(user_manage_page.get_by_text(dict_input.get("zh"))).to_have_count(1)
    select_user_nick(my_cursor, dict_input.get("zh"), dict_input.get("nickname"))
    alist = my_cursor.fetchall()
    assert len(alist) == 1

@pytest.mark.test
@allure.epic("搭建的网站")
@allure.feature("用户管理模块")
@allure.story("新增功能")
@allure.title("{id}")
@pytest.mark.parametrize("my_input",read_autocsv02('自动化测试用例.csv',27))
def test_manage07(my_traces,user_manage_page,my_input,select_a_man):
    dict_input: Dict[str] = json.loads(my_input)
    my_manage_page = UserManager(user_manage_page)
    my_add = my_manage_page.click_adduser()
    my_add.fill_base_info(dict_input.get("nickname"), dict_input.get("zh"), dict_input.get("pwd"))
    my_add.confirm_click()
    my_manage_page.click_adduser()
    for i in my_add.dialog.get_by_role("textbox").all():
        expect(i).to_have_value("")

@pytest.mark.web
@allure.epic("搭建的网站")
@allure.feature("用户管理模块")
@allure.story("新增功能")
@allure.title("{id}")
@pytest.mark.parametrize("my_input",read_autocsv02('自动化测试用例.csv',28))
def test_manage08(my_traces,user_manage_page,my_input,select_a_man):
    my_cursor = select_a_man
    dict_input: Dict[str] = json.loads(my_input)
    my_manage_page = UserManager(user_manage_page)
    my_add = my_manage_page.click_adduser()
    my_add.fill_base_info(dict_input.get("nickname"), dict_input.get("zh"), dict_input.get("pwd"))
    my_add.confirm_click()
    my_manage_page.click_adduser()
    my_add.fill_base_info(dict_input.get("nickname"), dict_input.get("zh"), dict_input.get("pwd"))
    my_add.confirm_click()
    my_manage_page.get_simple_assert("已存在")
    select_user_nick(my_cursor, dict_input.get("zh"), dict_input.get("nickname"))
    alist = my_cursor.fetchall()
    assert len(alist) == 1

@pytest.mark.web
@allure.epic("搭建的网站")
@allure.feature("用户管理模块")
@allure.story("修改功能")
@allure.title("{id}")
@pytest.mark.parametrize("my_input",read_autocsv02('自动化测试用例.csv',29))
def test_alter01(my_traces,user_manage_page,my_input,make_a_man):
    my_cursor ,uid= make_a_man
    my_manage_page = UserManager(user_manage_page)
    my_manage_page.select_user(f"{uid}")
    my_edit = my_manage_page.click_edit_user()
    my_edit.add_user_nickname("普通人")
    my_edit.confirm_click()
    my_manage_page.get_simple_assert("修改成功")
    select_id_nick(my_cursor, uid, "普通人")
    alist = my_cursor.fetchall()
    assert len(alist) == 1

@pytest.mark.web
@allure.epic("搭建的网站")
@allure.feature("用户管理模块")
@allure.story("修改功能")
@allure.title("{id}")
@pytest.mark.parametrize("my_input",read_autocsv02('自动化测试用例.csv',30))
def test_alter02(my_traces,user_manage_page,my_input,make_a_man):
    my_cursor ,uid= make_a_man
    dict_input: Dict[str] = json.loads(my_input)
    my_manage_page = UserManager(user_manage_page)
    my_manage_page.select_user(f"{uid}")
    my_edit = my_manage_page.click_edit_user()
    my_edit.cancel_click()
    my_manage_page.get_simple_assert(dict_input.get("nickname"))




@pytest.mark.web
@allure.epic("搭建的网站")
@allure.feature("用户管理模块")
@allure.story("修改功能")
@allure.title("{id}")
@pytest.mark.parametrize("my_input",read_autocsv02('自动化测试用例.csv',31))
def test_alter03(my_traces,user_manage_page,my_input,select_a_man):
    dict_input: Dict[str] = json.loads(my_input)
    my_manage_page = UserManager(user_manage_page)
    my_add = my_manage_page.click_adduser()
    my_add.fill_base_info(dict_input.get("nickname"), dict_input.get("zh"), dict_input.get("pwd"))
    my_add.stop(dict_input.get("status"))
    my_add.confirm_click()
    my_manage_page.select_user(dict_input.get("zh"))
    my_edit = my_manage_page.click_edit_user()
    my_edit.stop(False)
    my_edit.confirm_click()
    my_manage_page.exit_ry()
    LoginPage(user_manage_page).login(dict_input.get("zh"), dict_input.get("pwd"))
    LoginPage(user_manage_page).login_click()
    my_manage_page.get_simple_assert(dict_input.get("nickname"))

@pytest.mark.web
@allure.epic("搭建的网站")
@allure.feature("用户管理模块")
@allure.story("修改功能")
@allure.title("{id}")
@pytest.mark.parametrize("my_input",read_autocsv02('自动化测试用例.csv',32))
def test_alter04(my_traces,user_manage_page,my_input,make_a_man):
    my_cursor ,uid= make_a_man
    dict_input: Dict[str] = json.loads(my_input)
    my_manage_page = UserManager(user_manage_page)
    my_manage_page.select_user(f"{uid}")
    my_edit = my_manage_page.click_edit_user()
    my_edit.stop(True)
    my_edit.confirm.click()
    my_manage_page.exit_ry()
    LoginPage(user_manage_page).login(dict_input.get("zh"), dict_input.get("pwd"))
    LoginPage(user_manage_page).login_click()
    LoginPage(user_manage_page).get_simple_assert("已封禁")

@pytest.mark.web
@allure.epic("搭建的网站")
@allure.feature("用户管理模块")
@allure.story("修改功能")
@allure.title("{id}")
@pytest.mark.parametrize("my_input",read_autocsv02('自动化测试用例.csv',33))
def test_alter05(my_traces,user_manage_page,my_input,make_a_man):
    my_cursor ,uid= make_a_man
    dict_input: Dict[str] = json.loads(my_input)
    my_manage_page = UserManager(user_manage_page)
    my_manage_page.select_user(f"{uid}")
    my_edit = my_manage_page.click_edit_user()
    my_edit.add_dept(dict_input.get("department"))
    my_edit.confirm_click()
    expect(my_manage_page.page.locator(".splitpanes__pane").last.get_by_text("测试")).to_be_visible()

@pytest.mark.web
@allure.epic("搭建的网站")
@allure.feature("用户管理模块")
@allure.story("删除功能")
@allure.title("{id}")
@pytest.mark.parametrize("my_input",read_autocsv02('自动化测试用例.csv',34,36))
def test_del01(my_traces,user_manage_page,my_input,make_a_man):
    my_cursor ,uid= make_a_man
    dict_input: Dict[str] = json.loads(my_input)
    my_manage_page = UserManager(user_manage_page)
    my_manage_page.select_user(f"{uid}")
    my_delete=my_manage_page.click_delete_user()
    user_manage_page.wait_for_timeout(2000)
    my_manage_page.get_simple_assert("是否确认删除用户")
    my_delete.confirm_click()
    user_manage_page.wait_for_timeout(2000)
    my_manage_page.get_simple_assert("删除成功")
    select_id_nick(my_cursor, uid,dict_input.get("nickname"))
    alist = my_cursor.fetchall()
    assert len(alist) == 1

@pytest.mark.web
@allure.epic("搭建的网站")
@allure.feature("用户管理模块")
@allure.story("删除功能")
@allure.title("{id}")
@pytest.mark.parametrize("my_input",read_autocsv02('自动化测试用例.csv',35))
def test_del02(my_traces,user_manage_page,my_input,make_a_man):
    my_cursor ,uid= make_a_man
    dict_input: Dict[str] = json.loads(my_input)
    my_manage_page = UserManager(user_manage_page)
    my_manage_page.select_user(f"{uid}")
    my_delete=my_manage_page.click_delete_user()
    my_delete.confirm_click()
    my_manage_page.get_simple_assert("删除成功")
    my_manage_page.exit_ry()
    LoginPage(user_manage_page).login(dict_input.get("zh"), dict_input.get("pwd"))
    LoginPage(user_manage_page).login_click()
    LoginPage(user_manage_page).get_simple_assert("用户不存在")

@pytest.mark.web
@allure.epic("搭建的网站")
@allure.feature("用户管理模块")
@allure.story("删除功能")
@allure.title("{id}")
@pytest.mark.parametrize("my_input",read_autocsv02('自动化测试用例.csv',37))
def test_del03(my_traces,user_manage_page,my_input):
    my_manage_page = UserManager(user_manage_page)
    my_manage_page.select_user("1")
    my_delete=my_manage_page.click_delete_user()
    my_delete.confirm_click()
    my_manage_page.get_simple_assert("不能删除")
