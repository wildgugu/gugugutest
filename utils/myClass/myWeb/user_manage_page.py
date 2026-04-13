import allure
from playwright.sync_api import  Page, expect
class UserManager:
    def __init__(self,page:Page):
        self.page:Page=page
        self.add_user=page.locator('.mb8.el-row').get_by_role("button",name="新增")
        self.edit_user=page.locator('.mb8.el-row').get_by_role("button",name="修改")
        self.delete_user=page.locator('.mb8.el-row').get_by_role("button",name="删除")
        self.top_right_ry=page.get_by_role("button", name="若依")
    class AddUser:
        def __init__(self,page:Page):
            self.page:Page=page
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
            self.byno=self.dialog.get_by_role("radio",name="停用")
            self.confirm=self.dialog.get_by_role("button",name="确 定")
            self.cancel=self.dialog.get_by_role("button",name="取 消")
        @allure.step("填写用户昵称")
        def add_user_nickname(self,username:str=None):
            if username is not None:
                self.user_nickname.fill(username)
        @allure.step("填写手机号")
        def add_phone(self,phone:str=None):
            if phone is not None:
                self.phone.fill(phone)
        @allure.step("填写邮箱")
        def add_email(self,email:str):
            if email is not None:
                self.email.fill(email)
        @allure.step("填写密码")
        def add_password(self,password:str=None):
            if password is not None:
                self.password.fill(password)
        @allure.step("填写用户名")
        def add_username(self,username:str=None):
            if username is not None:
                self.username.fill(username)
        @allure.step("填写部门")
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
        @allure.step("填写性别")
        def add_gender(self,gender:str=None):
            if gender is not None:
                self.gender.click()
                self.page.get_by_text(gender).click()
        @allure.step("填写岗位")
        def add_post(self,post:str=None):
            if post is not None:
                self.post.click()
                self.page.get_by_text(post).click()
                self.page.locator(".el-select__caret.el-input__icon.el-icon-arrow-up.is-reverse").click()
        @allure.step("填写备注")
        def add_note(self,note:str=None):
            if note is not None:
                self.note.fill(note)
        @allure.step("填写角色")
        def add_career(self,career:str=None):
            if career is not None:
                self.career.click()
                self.page.get_by_text(career).click()
                self.page.locator(".el-select__caret.el-input__icon.el-icon-arrow-up.is-reverse").click()
        @allure.step("选择状态")
        def stop(self,status=False):
            if status:
                self.byno.check()
            else:
                self.normal.check()
        @allure.step("点击确定")
        def confirm_click(self):
            self.confirm.click()
        @allure.step("点击取消")
        def cancel_click(self):
            self.cancel.click()
        @allure.step("填写必填项")
        def fill_base_info(self, nickname: str=None, username: str=None, password: str=None):
            if nickname is not None:
               self.user_nickname.fill(nickname)
            if username is not None:
                self.username.fill(username)
            if password is not None:
                self.password.fill(password)

    class EditUser:
        def __init__(self,page:Page):
            self.page:Page = page
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
            self.byno = self.dialog.get_by_role("radio", name="停用")
            self.confirm = self.dialog.get_by_role("button", name="确 定")
            self.cancel = self.dialog.get_by_role("button", name="取 消")
        @allure.step("填写用户昵称")
        def add_user_nickname(self,username:str=None):
            if username is not None:
                self.user_nickname.fill(username)
        @allure.step("填写手机号")
        def add_phone(self,phone:str=None):
            if phone is not None:
                self.phone.fill(phone)
        @allure.step("填写邮箱")
        def add_email(self,email:str):
            if email is not None:
                self.email.fill(email)
        @allure.step("填写部门")
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
        @allure.step("填写性别")
        def add_gender(self,gender:str=None):
            if gender is not None:
                self.gender.click()
                self.page.get_by_text(gender).click()
        @allure.step("填写岗位")
        def add_post(self,post:str=None):
            if post is not None:
                self.post.click()
                self.page.get_by_text(post).click()
                self.page.locator(".el-select__caret.el-input__icon.el-icon-arrow-up.is-reverse").click()
        @allure.step("填写备注")
        def add_note(self,note:str=None):
            if note is not None:
                self.note.fill(note)
        @allure.step("填写角色")
        def add_career(self,career:str=None):
            if career is not None:
                self.career.click()
                self.page.get_by_text(career).click()
                self.page.locator(".el-select__caret.el-input__icon.el-icon-arrow-up.is-reverse").click()
        @allure.step("选择状态")
        def stop(self,status=True):
            if status:
                self.byno.check()
            else:
                self.normal.check()
        @allure.step("点击确定")
        def confirm_click(self):
            self.confirm.click()
        @allure.step("点击取消")
        def cancel_click(self):
            self.cancel.click()
    class DeleteUser:
        def __init__(self,page:Page):
            self.page:Page = page
            self.my_dialog=self.page.get_by_role("dialog", name="系统提示")
            self.info=self.my_dialog.locator('.el-message-box__message')
            self.confirm=self.my_dialog.get_by_role("button", name="确定")
            self.cancel=self.my_dialog.get_by_role("button", name="取消")
        @allure.step("点击确定")
        def confirm_click(self):
            self.confirm.click()
        @allure.step("点击取消")
        def cancel_click(self):
            self.cancel.click()
        @allure.step("获取提示信息")
        def info_message(self):
            return self.info.inner_text()


    @allure.step("点击新增用户")
    def click_adduser(self)->AddUser:
        self.add_user.click()
        return self.AddUser(self.page)
    @allure.step("选择用户{username}")
    def select_user(self,username:str=None):
        if username is not None:
            username_cell = self.page.get_by_text(username, exact=True)
            user_row = username_cell.locator("xpath=ancestor::tr[contains(@class, 'el-table__row')]")
            checkbox_span = user_row.locator(".el-table-column--selection .el-checkbox__inner")
            checkbox_span.click()
    @allure.step("点击编辑用户")
    def click_edit_user(self)->EditUser:
        self.edit_user.click()
        return self.EditUser(self.page)
    @allure.step("悬浮若依菜单")
    def hover_ry(self):
        self.top_right_ry.hover()
    @allure.step("点击退出登录")
    def exit_ry(self):
        self.top_right_ry.hover()
        self.page.locator('.el-dropdown-menu__item.el-dropdown-menu__item--divided').click()
        self.page.get_by_role("button",name="确定").click()
    @allure.step("简单断言")
    def get_simple_assert(self,dy:str):
        message=self.page.get_by_text(dy)
        expect(message).to_be_visible()
    @allure.step("点击删除用户")
    def click_delete_user(self)->DeleteUser:
        self.delete_user.click()
        return self.DeleteUser(self.page)
    @allure.step("刷新")
    def shua_xin(self):
        self.page.reload()