import time

import pytest
from PageObjects.LoginPage import Loginpage
from PageObjects.PositionPage import selectPosition
from PageObjects.SearchPersonPage import searchPerson
from utilities import elements

import os


class Test_searchPerson:

    def test_searchPerson(self,setup):
        self.driver =setup
        self.driver.implicitly_wait(20)
        Url = elements.url
        self.driver.get(Url)
        login = Loginpage(self.driver)
        login.clickOnSSO()
        login.EnterUserName()
        login.EnterPassword()
        login.submit()
        position =selectPosition(self.driver)
        position.position()
        searchperson =searchPerson(self.driver)
        time.sleep(5)
        searchperson.manage_person()
        searchperson.search_person()
        searchperson.search_buttton()
        time.sleep(10)
        searchperson.verification_page()








