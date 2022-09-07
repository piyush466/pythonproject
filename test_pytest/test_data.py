import pytest

from test_pytest.Baseclass import BaseClass


@pytest.mark.usefixtures("Dataload")
class Testdemo(BaseClass):
    def test_profile(self,Dataload):
        log = self.getLogger()
        log.info(Dataload[0])
        log.info(Dataload[1])
        # print(Dataload[0])
        # print(Dataload[2])
        print(Dataload)