import pytest
import yaml


def read_case(path):
    with open(path,'r',encoding='utf-8') as f:
        all_value=yaml.load(f,Loader=yaml.FullLoader)
        return all_value

def read_paratre(path):
    lists=read_case(path)
    for adict in lists:
        aid=adict["caseid"] + adict["testcase"]
        yield pytest.param(adict,aid,id=adict["caseid"]+adict["testcase"])