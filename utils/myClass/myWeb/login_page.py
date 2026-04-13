from playwright.sync_api import  Page, expect
import allure
class LoginPage:
    def __init__(self,page:Page):
        self.page:Page=page
        self.username=page.get_by_placeholder("账号")
        self.password=page.get_by_placeholder("密码")
        self.remember=page.get_by_text("记住密码")
        self.login_button=page.get_by_role("button",name="登 录")
        self.alert=page.get_by_role("alert")
    @allure.step("登录输入")
    def login(self,username:str=None,password:str=None,remember=False):
        if username is not None:
            self.username.fill(username)
        if password is not None:
            self.password.fill(password)
        if remember:
            self.remember.check()
        else:
            self.remember.uncheck()
    @allure.step("登录点击")
    def login_click(self):
        self.login_button.click()
        return self.page
    @allure.step("简单断言")
    def get_simple_assert(self,dy:str):
        message=self.page.get_by_text(dy)
        expect(message).to_be_visible()
    @allure.step("前进")
    def foward(self):
        self.page.go_forward()
    @allure.step("后退")
    def back(self):
        self.page.go_back()
    @allure.step("刷新")
    def shua_xin(self):
        self.page.reload()