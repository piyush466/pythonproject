import pytest


@pytest.fixture(scope="class")

def setup():
    print("1st exicute")
    yield
    print("last exicute")


@pytest.fixture
def Dataload():
    print("1st printing")
    return ["piyush", "milind", "dravyakar"]

@pytest.fixture(params=[("chrome","piyush","dravyakar"),("Firefox","parikshit","tushar"), ("IE","ggood")])
def crossbrowser(request):
    return request.param
