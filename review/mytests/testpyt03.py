import pytest

@pytest.fixture(autouse=True)
def f():
    print('123')
    yield 23
    print('456')



def test_he(f):
    print(f)

def test_ad():
    pass