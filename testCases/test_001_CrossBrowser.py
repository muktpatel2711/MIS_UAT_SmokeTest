import webbrowser

import pytest
from selenium import webdriver

from PageObjects.LoginPage import Loginpage
from PageObjects.PositionPage import selectPosition
from utilities import elements

import os


class Test_Browser:
    Browser = ["Chrome","Firefox","safari"]

    @pytest.mark.parametrize("browser", Browser)
    def test_login(self,browser):
        if browser == "Chrome":
            self.driver = webdriver.Chrome()
        elif browser == "Firefox":
            self.driver = webdriver.Firefox()
        elif browser == "Safari":
            self.driver = webdriver.Safari()
        else:
            print(f"{browser} is not a supported browser.")
            return
        self.driver.get(elements.url)
        self.driver.quit()







