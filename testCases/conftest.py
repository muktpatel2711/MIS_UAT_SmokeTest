import os.path
from datetime import datetime

from selenium import webdriver

import pytest

from PageObjects.LoginPage import Loginpage

from utilities import elements
@pytest.fixture()
def setup(browser):
    if browser == 'edge':
        driver = webdriver.Edge()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture()
def login(setup):
    driver =setup
    baseURL =elements.url
    driver.get(baseURL)
    driver.maximize_window()
    login_page = Loginpage(driver)
    login_page.clickOnSSO()
    login_page.EnterUserName()
    login_page.EnterPassword()
    login_page.submit()

    yield driver

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

# report

def pytest_configure(config):
    config._metadata['Project Name'] = 'MIS_UAT'
    config._metadata['Module Name'] = "Position_136"
    config._metadata['Tester'] = "Mukt"

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # Generate report path with timestamp
    config.option.htmlpath = os.path.abspath(os.curdir) + "//reports//" + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html"

# You don't need pytest_metadata, instead use pytest_html_results_summary if needed
@pytest.hookimpl(optionalhook=True)
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([f"Project: MIS_UAT", f"Module: Position_136", f"Tester: Mukt"])

def pytest_addoption(parser):
    parser.addoption("--browser")