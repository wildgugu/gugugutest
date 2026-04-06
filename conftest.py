from typing import Iterator
import pytest
from mysql.connector.cursor import MySQLCursor
from mysql.connector.pooling import MySQLConnectionPool
from playwright.sync_api import sync_playwright, Playwright, Browser, BrowserContext, Page, expect
import mydomain
from mysql.connector import pooling, Error, MySQLConnection


class LoginPage:
    def __init__(self,page:Page):
        self.page=page
        self.username=page.get_by_placeholder("账号")
        self.password=page.get_by_placeholder("密码")
        self.input_yzm=page.get_by_placeholder("验证码")
        self.click_yzm=page.locator('//img[@class="login-code-img"]')
        self.remember=page.get_by_text("记住密码")
        self.login_button=page.get_by_role("button",name="登 录")
        self.alert=page.get_by_role("alert")

    def login(self,username:str=None,password:str=None,remember=False):
        if username is not None:
            self.username.fill(username)
        if password is not None:
            self.password.fill(password)
        if remember:
            self.remember.check()
        else:
            self.remember.uncheck()
    def login_click(self):
        self.login_button.click()
        return self.page
    def get_simple_assert(self,dy:str):
        message=self.page.get_by_text(dy)
        expect(message).to_be_visible()
    def foward(self):
        self.page.go_forward()
    def back(self):
        self.page.go_back()
    def shua_xin(self):
        self.page.reload()

class UserManager:
    def __init__(self,page:Page):
        self.page=page
        self.add_user=page.locator('.mb8.el-row').get_by_role("button",name="新增")
        self.edit_user=page.locator('.mb8.el-row').get_by_role("button",name="修改")
        self.delete_user=page.locator('.mb8.el-row').get_by_role("button",name="删除")
        self.top_right_ry=page.get_by_role("button", name="若依")
    class AddUser:
        def __init__(self,page:Page):
            self.page=page
            self.page.get_by_role("dialog", name="添加用户").wait_for()
            self.dialog=self.page.get_by_role("dialog",name="添加用户")
            self.user_nickname=self.dialog.get_by_placeholder("用户昵称")
            self.phone=self.dialog.get_by_placeholder("手机号")
            self.email=self.dialog.get_by_placeholder("邮箱")
            self.password=self.dialog.get_by_placeholder("密码")
            self.username=self.dialog.get_by_placeholder("名称")
            self.dept=self.dialog.locator(".vue-treeselect__input-container")
            self.gender=self.dialog.get_by_placeholder("性别")
            self.post=self.dialog.get_by_placeholder("岗位")
            self.note=self.dialog.get_by_placeholder("输入内容")
            self.career=self.dialog.get_by_placeholder("角色")
            self.normal=self.dialog.get_by_role("radio",name="正常")
            self.stop=self.dialog.get_by_role("radio",name="停用")
            self.confirm=self.dialog.get_by_role("button",name="确 定")
            self.cancel=self.dialog.get_by_role("button",name="取 消")
        def add_user_nickname(self,username:str=None):
            if username is not None:
                self.user_nickname.fill(username)
        def add_phone(self,phone:str=None):
            if phone is not None:
                self.phone.fill(phone)
        def add_email(self,email:str):
            if email is not None:
                self.email.fill(email)
        def add_password(self,password:str=None):
            if password is not None:
                self.password.fill(password)
        def add_username(self,username:str=None):
            if username is not None:
                self.username.fill(username)
        def add_dept(self,dep_list:str=None):
            if dep_list is not None:
                self.dept.click()
                dep_lists=dep_list.split(",")
                for index, dep_name in enumerate(dep_lists):
                    if index != len(dep_lists) - 1:
                        (self.page.locator('.vue-treeselect__label-container')
                         .filter(has_text=f'{dep_name}')#如果不是最里层就展开
                         .locator('xpath=/../*[1]').click())#从名字开始往上找父节点，找到再往下找子节点，子节点1为展开，子节点2为名字
                    if index == len(dep_lists) - 1:
                        (self.page.locator('.vue-treeselect__label-container').filter(has_text=f'{dep_name}')
                         .locator('xpath=/../*[2]').#如果是最里层点名字
                         click())

        def add_gender(self,gender:str=None):
            if gender is not None:
                self.gender.click()
                self.page.get_by_text(gender).click()
        def add_post(self,post:str=None):
            if post is not None:
                self.post.click()
                self.page.get_by_text(post).click()
                self.page.locator(".el-select__caret.el-input__icon.el-icon-arrow-up.is-reverse").click()

        def add_note(self,note:str=None):
            if note is not None:
                self.note.fill(note)
        def add_career(self,career:str=None):
            if career is not None:
                self.career.click()
                self.page.get_by_text(career).click()
                self.page.locator(".el-select__caret.el-input__icon.el-icon-arrow-up.is-reverse").click()
        def stauts(self,status=True):
            if status:
                self.normal.check()
            else:
                self.stop.check()
        def confirm_click(self):
            self.confirm.click()
        def cancel_click(self):
            self.cancel.click()
        def fill_base_info(self, nickname: str=None, username: str=None, password: str=None):
            if nickname is not None:
               self.user_nickname.fill(nickname)
            if username is not None:
                self.username.fill(username)
            if password is not None:
                self.password.fill(password)

    class EditUser:
        def __init__(self,page:Page):
            self.page = page
            self.page.get_by_role("dialog", name="修改用户").wait_for()
            self.dialog = self.page.get_by_role("dialog", name="修改用户")
            self.user_nickname = self.dialog.get_by_placeholder("用户昵称")
            self.phone = self.dialog.get_by_placeholder("手机号")
            self.email = self.dialog.get_by_placeholder("邮箱")
            self.dept = self.dialog.locator(".vue-treeselect__input-container")
            self.gender = self.dialog.get_by_placeholder("性别")
            self.post = self.dialog.get_by_placeholder("岗位")
            self.note = self.dialog.get_by_placeholder("输入内容")
            self.career = self.dialog.get_by_placeholder("角色")
            self.normal = self.dialog.get_by_role("radio", name="正常")
            self.stop = self.dialog.get_by_role("radio", name="停用")
            self.confirm = self.dialog.get_by_role("button", name="确 定")
            self.cancel = self.dialog.get_by_role("button", name="取 消")
        def add_user_nickname(self,username:str=None):
            if username is not None:
                self.user_nickname.fill(username)
        def add_phone(self,phone:str=None):
            if phone is not None:
                self.phone.fill(phone)
        def add_email(self,email:str):
            if email is not None:
                self.email.fill(email)
        def add_dept(self,dep_list:str=None):
            if dep_list is not None:
                self.dept.click()
                dep_lists=dep_list.split(",")
                for index, dep_name in enumerate(dep_lists):
                    if index != len(dep_lists) - 1:
                        (self.page.locator('.vue-treeselect__label-container')
                         .filter(has_text=f'{dep_name}')#如果不是最里层就展开
                         .locator('xpath=/../*[1]').click())#从名字开始往上找父节点，找到再往下找子节点，子节点1为展开，子节点2为名字
                    if index == len(dep_lists) - 1:
                        (self.page.locator('.vue-treeselect__label-container').filter(has_text=f'{dep_name}')
                         .locator('xpath=/../*[2]').#如果是最里层点名字
                         click())

        def add_gender(self,gender:str=None):
            if gender is not None:
                self.gender.click()
                self.page.get_by_text(gender).click()
        def add_post(self,post:str=None):
            if post is not None:
                self.post.click()
                self.page.get_by_text(post).click()
                self.page.locator(".el-select__caret.el-input__icon.el-icon-arrow-up.is-reverse").click()

        def add_note(self,note:str=None):
            if note is not None:
                self.note.fill(note)
        def add_career(self,career:str=None):
            if career is not None:
                self.career.click()
                self.page.get_by_text(career).click()
                self.page.locator(".el-select__caret.el-input__icon.el-icon-arrow-up.is-reverse").click()
        def stauts(self,status=True):
            if status:
                self.normal.check()
            else:
                self.stop.check()
        def confirm_click(self):
            self.confirm.click()
        def cancel_click(self):
            self.cancel.click()
    class DeleteUser:
        def __init__(self,page:Page):
            self.page = page
            self.my_dialog=login_page.get_by_role("dialog", name="系统提示")
            self.info=self.my_dialog.locator('.el-message-box__message')
            self.confirm=self.my_dialog.get_by_role("button", name="确定")
            self.cancel=self.my_dialog.get_by_role("button", name="取消")
        def confirm_click(self):
            self.confirm.click()
        def cancel_click(self):
            self.cancel.click()
        def info_message(self):
            return self.info.inner_text()



    def click_adduser(self):
        self.add_user.click()
        return self.AddUser(self.page)
    def select_user(self,username:str=None):
        if username is not None:
            username_cell = login_page.get_by_text(username, exact=True)
            user_row = username_cell.locator("xpath=ancestor::tr[contains(@class, 'el-table__row')]")
            checkbox_span = user_row.locator(".el-table-column--selection .el-checkbox__inner")
            checkbox_span.click()
    def click_edit_user(self):
        self.edit_user.click()
        return self.EditUser(self.page)
    def hover_ry(self):
        self.top_right_ry.hover()
    def exit_ry(self):
        self.top_right_ry.hover()
        self.page.locator('.el-dropdown-menu__item.el-dropdown-menu__item--divided').click()
        self.page.get_by_role("button",name="确定").click()

    def click_delete_user(self):
        self.delete_user.click()
        return self.DeleteUser(self.page)

@pytest.fixture(scope="session")
def new_play_driver():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def new_chrome(new_play_driver:Playwright):
    my_chrome=new_play_driver.chromium.launch(headless=False)
    yield my_chrome
    my_chrome.close()

@pytest.fixture
def chrome_context(new_chrome:Browser)->Iterator[BrowserContext]:
    my_context=new_chrome.new_context()
    yield my_context
    my_context.close()

@pytest.fixture
def login_page(chrome_context:BrowserContext)->Iterator[Page]:
    login_page=chrome_context.new_page()
    login_page.goto(f"http://{mydomain.domain}/login")
    yield login_page
    login_page.close()
@pytest.fixture
def user_manage_page(chrome_context:BrowserContext)->Iterator[Page]:
    user_manage_page=chrome_context.new_page()
    user_manage_page.goto(f"http://{mydomain.domain}/system/user")
    my_login=LoginPage(user_manage_page)
    my_login.login("admin","admin123")
    my_login.loginclick()
    yield user_manage_page
    user_manage_page.close()

@pytest.fixture(scope="session")
def db_pool():
    pool = pooling.MySQLConnectionPool(
        pool_name="test_pool",
        pool_size=10,
        pool_reset_session=True,
        host=f"{mydomain.domain}",  # 数据库主机地址
        user=f"{mydomain.mysql_user}",  # 数据库用户名
        passwd=f"{mydomain.mysql_passwd}",  # 数据库密码
        database=f"{mydomain.mysql_database}",
        charset='utf8mb4',
        autocommit=False
    )
    yield pool
    #自动关闭连接池

@pytest.fixture(scope="function")
def db_cursor(db_pool:MySQLConnectionPool)->Iterator[tuple[MySQLCursor, MySQLConnection]]:
    conn:MySQLConnection|None = None
    cursor:MySQLCursor|None = None
    try:
        conn = db_pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        yield cursor,conn
        conn.rollback()  # 自动回滚
    except Error as e:
        if conn:
            conn.rollback()
        raise RuntimeError(f"数据库测试失败: {e}") from e
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

@pytest.fixture(scope="function")
def make_a_man(db_cursor)-> Iterator[list]:
    my_cursor,my_conn=db_cursor
    data=["ptr123","普通人123"]
    my_cursor.execute("insert into sys_user(user_id,user_name,nick_name) values (DEFAULT,%s,%s)",data)
    my_conn.commit()
    new_data = data.copy()
    new_data.append(my_cursor.lastrowid)
    yield new_data
    my_cursor.execute("select user_id,user_name,nick_name from sys_user where user_name=%s And nick_name=%s",data)
    list=my_cursor.fetchall()
    if len(list)>0:
        my_cursor.execute("delete from sys_user where user_name=%s And nick_name=%s",data)
        my_conn.commit()
