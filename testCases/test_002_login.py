import pytest
from PageObjects.LoginPage import Loginpage
from PageObjects.PositionPage import selectPosition
from utilities import elements

import os


class Test_Login:

    def test_login(self,setup):
        self.driver =setup
        Url = elements.url
        self.driver.get(Url)
        login = Loginpage(self.driver)
        login.clickOnSSO()
        login.EnterUserName()
        login.EnterPassword()
        login.submit()
        position =selectPosition(self.driver)
        position.position()







