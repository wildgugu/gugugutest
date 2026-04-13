import allure
@allure.step("查询用户")
def select_user_nick(cursor,zh,nickname):
    cursor.execute("select user_id,user_name,nick_name from sys_user where user_name=%s And nick_name=%s",(zh, nickname))
@allure.step("查询用户")
def select_id_nick(cursor,uid,nickname):
    cursor.execute("select user_id,user_name,nick_name from sys_user where user_id=%s And nick_name=%s",(uid, nickname))
