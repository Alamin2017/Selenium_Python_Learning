import pytest

@pytest.fixture()
def setup():
    print("once before every method")

def testmethod1(setup):
    print("This is test method1")

def testmethod2(setup):
    print("This is test method2")
