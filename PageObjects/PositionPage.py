from selenium.webdriver.common.by import By
from selenium import webdriver
from utilities import elements

class selectPosition:
    def __init__(self,driver):
        self.driver=driver
    def position(self):
        self.driver.find_element(By.XPATH, elements.select_pisition_xpath).click()