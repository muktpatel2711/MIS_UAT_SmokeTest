import time

import pytest
from PageObjects.LoginPage import Loginpage
from PageObjects.PositionPage import selectPosition
from PageObjects.SearchPersonPage import searchPerson
from PageObjects.globalSearchPage import globalsearch
from utilities import elements

import os


class Test_Global_search:

    def test_globalPerson(self,setup):
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
        time.sleep(10)
        searchperson.manage_person()
        global_search =globalsearch(self.driver)
        global_search.clickGlobal_search()
        time.sleep(5)
        global_search.Enter_global_firstName()
        global_search.Enter_last_name()
        global_search.Enter_bapsid()
        global_search.global_search_button()
        time.sleep(5)
        global_search.global_name_verify()










