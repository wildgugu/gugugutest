import pytest
import csv
def add(a,b):
    return a+b
def read_add(path):
    with open(path) as p:
        reader=csv.reader(p)
        return (list(reader)[1:])
class TestAdd:
    @pytest.mark.web
    def test_int(self):
        res=add(1,3)
        assert res == 4
    @pytest.mark.skipif('a'=='b',reason='就跳')
    @pytest.mark.api
    def test_str(self):
        res=add('1','3')
        assert res == '13'
    @pytest.mark.xfail
    @pytest.mark.login
    def test_list(self):
        res=add([1],[2,3,4])
        assert res == [1,2,3,4]
    @pytest.mark.parametrize('a,b,c',read_add('review/mytests/files/add_.csv'))
    def test_ddt(self,a,b,c):
        res=add(int(a),int(b))
        assert res == int(c)
