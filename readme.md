# 基于RuoYi-Vue，独立构建覆盖UI、接口、数据库、CI的自动化测试

基于 Playwright + Pytest + Requests 构建的 Web + Api自动化测试初期框架，日执行用例 100+

## 项目概述

- **技术选型**：Python + Playwright + Requests + Pytest + Allure + Jenkins + JMeter + MySQL
- **工程化**：接口封装 YAML 驱动的数据分离，编写自动化用例时间缩短 50%。
- **报告系统**：集成 Allure + Jenkins邮件通知，问题定位时间缩短。

## 技术栈

![Python](https://img.shields.io/badge/Python-3.10-blue) ![Pytest](https://img.shields.io/badge/Pytest-9.0.2-green) ![Playwright](https://img.shields.io/badge/Playwright-1.58-orange) ![MySQL](https://img.shields.io/badge/MySQL-8.0-blue)
[![PyPI Version](https://img.shields.io/badge/requests-2.33.31-blue)](https://pypi.org/project/requests)

- **核心框架**：Pytest + Playwright + Requests
- **用例管理**：PyYAML + CSV
- **数据库**：mysql-connector-python
- **持续集成**：Jenkins
- **报告**：Allure + Jenkins邮件通知

## 项目执行情况

| 指标 | 数据 |
|------|------|
| 用例总数 | 100+ |
| 稳定性 | 通过率 95.1% |


## 目录

```text
├── docs                            #文档，主要是测试用例
│   ├── apicsv                      #Jmeter参数驱动化存放目录
│   ├── report                      #Allure报告
│   ├── testreport                  #Jmeter报告
│   └── Yaml                        #接口用例存放文件夹
│       ├── web自动化测试用例.csv
│       ├── 测试用例.xlsx
│       ├── 登录接口测试用例.xlsx
│       └── 登录接口测试自动化用例.cs
├── mytraces                       #playwright trace文件
├── review                         #复习python时产生的代码
│   ├── mypython
│   ├── mysql
│   └── mytests
├── setting                        #一些全局配置
├── testCases                      #用例执行目录
│   ├── api
│   └── web
├── utils                          #工具
│   ├── myClass                    #按类存放的封装
│   │   └── myWeb                  #网页
│   │   └── myApi                  #接口
│   ├── myfunction                 #按函数存放的工具
│   │   └── myWeb                  #存放的csv读取方法
│   │   └── sqlMy                  #存放的sql查询方法
│   ├── myYaml                     #存放的yaml读取方法                  
├── .gitignore
├── conftest.py                    #配置了所需要的所有Fixtures
├── pytest.ini
├── readme.md
└── requirements.txt
```