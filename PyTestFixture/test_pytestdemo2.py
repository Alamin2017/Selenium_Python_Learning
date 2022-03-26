import pytest

@pytest.yield_fixture()
def setup():
    print("Once before every method")
    yield
    print("Once After every method ")

def testMethod1(setup):
    print("This is test method1")

def testMethod2(setup):
    print("This is test method2")