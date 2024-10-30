import time

import pytest
from PageObjects.LoginPage import Loginpage
from PageObjects.PositionPage import selectPosition
from PageObjects.SearchPersonPage import searchPerson
from PageObjects.globalSearchPage import globalsearch
from PageObjects.advanceSearchPage import advancesearch
from utilities import elements

import os


class Test_Advance_search:

    def test_advance_Person(self,setup):
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
        advance_search =advancesearch(self.driver)
        advance_search.click_advance_search()
        advance_search.advance_search_button()
        time.sleep(10)
        advance_search.advance_name_verify()










