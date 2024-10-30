import time

import pytest
from PageObjects.LoginPage import Loginpage
from PageObjects.PositionPage import selectPosition
from PageObjects.SearchPersonPage import searchPerson
from PageObjects.samparkSearchPage import samparksearch
from utilities import elements

import os


class Test_searchSampark:

    def test_searchSampark(self,setup):
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
        time.sleep(5)
        searchsampark =samparksearch(self.driver)
        searchsampark.clicksmanage_sampark()
        time.sleep(5)
        searchsampark.clicksampark_search()
        searchsampark.clicksampark_button()
        searchsampark.sampark_count_verify()








