import json

import allure
import requests
import pytest
from playwright.sync_api import sync_playwright, Playwright, Browser, BrowserContext, Page, expect
from utils.myClass.myWeb.login_page import LoginPage
from mysql.connector import pooling, Error, MySQLConnection
from mysql.connector.cursor import MySQLCursor
from mysql.connector.pooling import MySQLConnectionPool
from typing import Iterator, Dict
from setting import mydomain


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # 执行所有其他钩子，获取测试报告
    outcome = yield
    rep = outcome.get_result()
    # 把测试结果挂载到 request.node 上
    # rep.when 有三个阶段：setup(前置)、call(测试用例本身)、teardown(后置)
    setattr(item, f"rep_{rep.when}", rep)

@pytest.fixture(scope="session")
def new_play_driver():
    with sync_playwright() as p:
        yield p
@pytest.fixture(scope="session")
def new_chrome(new_play_driver:Playwright):
    my_chrome=new_play_driver.chromium.launch()
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
    my_login.login_click()
    yield user_manage_page
    user_manage_page.close()

@pytest.fixture
def my_traces(chrome_context:BrowserContext,request: pytest.FixtureRequest):
    chrome_context.tracing.start(snapshots=True,sources=True,screenshots=True) # 记录DOM快照# 记录源代码# 记录每个步骤的截图
    yield
   #测试执行后：判断是否失败，失败才保存追踪
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        test_name = request.node.name
        trace_path = f"mytraces/{test_name}.zip"
        # 保存追踪文件
        chrome_context.tracing.stop(path=trace_path)
        with open(trace_path, "rb") as f:
            allure.attach(
                body=f.read(),
                name=f"{test_name}",
                attachment_type="application/vnd.allure.playwright-trace",
                extension="zip"
            )
    else:
        chrome_context.tracing.stop()
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

@pytest.fixture
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

@pytest.fixture
def make_a_man(db_cursor,request: pytest.FixtureRequest)->Iterator[tuple[MySQLCursor,int]]:
    my_cursor,my_conn=db_cursor
    str = request.getfixturevalue("my_input")
    data: Dict[str] = json.loads(str)
    if data.get("zh") and data.get("nickname"):
        my_cursor.execute("insert into sys_user(user_id,user_name,nick_name) values (DEFAULT,%s,%s)",(data.get("zh"),data.get("nickname")))
        my_conn.commit()
        uid=my_cursor.lastrowid
    yield my_cursor,uid
    if data.get("zh"):
        my_cursor.execute("delete from sys_user where user_id=%s and user_name=%s",
                          (uid, data.get("zh")))
        my_conn.commit()

@pytest.fixture
def select_a_man(db_cursor,request: pytest.FixtureRequest)->Iterator[MySQLCursor]:
    my_cursor,my_conn=db_cursor
    str = request.getfixturevalue("my_input")
    data: Dict[str] = json.loads(str)
    yield my_cursor
    if data.get("zh") and data.get("nickname"):
            my_cursor.execute("delete from sys_user where user_name=%s And nick_name=%s",(data.get("zh"),data.get("nickname")))
            my_conn.commit()
@pytest.fixture
def create_session():
    session = requests.session()
    yield session
    session.close()

@pytest.fixture
def have_token():
    res=requests.post(url="http://example.wildgugugu.cn:8080/login",headers={ "Content-Type": "application/json"},json={ "username": "admin"  , "password": "admin123"})
    yield res.json().get('token')
