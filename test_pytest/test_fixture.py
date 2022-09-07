import pytest


@pytest.mark.usefixtures("setup")
#class name is capital
class Testing:
    def test_good(self):
        print("one")

@pytest.mark.skip
def test_boom(self):
    print("piyush")