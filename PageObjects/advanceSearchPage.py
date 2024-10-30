from selenium.webdriver.common.by import By
from selenium import webdriver
from utilities import elements
from TestData import data

class advancesearch:
    def __init__(self,driver):
        self.driver=driver
    def click_advance_search(self):
        self.driver.find_element(By.XPATH, elements.advance_search_xpath).click()

    def advance_search_button(self):
        self.driver.find_element(By.XPATH, elements.advance_search_button_xpath).click()

    def advance_name_verify(self):
        misid = self.driver.find_element(By.XPATH, elements.mis_id_verification_xpath)
        misid_text = misid.text
        assert misid_text == f"{data.misId}"
        pass
        print("An advance search works fine")
        self.driver.quit()







