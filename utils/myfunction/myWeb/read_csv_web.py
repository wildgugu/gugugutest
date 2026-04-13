import csv
import pytest
def read_rt_input_result_csv(filepath,*num,left=None,right=None):
    with open(filepath,'r',encoding='utf8') as f:
        reader = csv.DictReader(f)
        for index,include in enumerate(reader):
            if left  is not None and right is not None:
                if left<=index<=right:
                    name=include['用例编号']+include['测试标题']
                    yield pytest.param(include['测试输入'],include['预期结果'],name,id=name)
            else:
                if index in num:
                    name = include['用例编号'] + include['测试标题']
                    yield pytest.param(include['测试输入'], include['预期结果'],name, id=name)

def read_rt_input_csv(filepath,*num,left=None,right=None):
    with open(filepath,'r',encoding='utf8') as f:
        reader = csv.DictReader(f)
        for index,include in enumerate(reader):
            if left is not None and right is not None:
                if left <= index <= right:
                    name = include['用例编号'] + include['测试标题']
                    yield pytest.param(include['测试输入'],name, id=name)
            else:
                if index in num:
                    name = include['用例编号'] + include['测试标题']
                    yield pytest.param(include['测试输入'],name, id=name)