from selenium.webdriver.common.by import By
from selenium import webdriver
from utilities import elements
from TestData import data

class globalsearch:
    def __init__(self,driver):
        self.driver=driver
    def clickGlobal_search(self):
        self.driver.find_element(By.XPATH, elements.global_search_xpath).click()

    def Enter_global_firstName(self):
        self.driver.find_element(By.XPATH, elements.first_name_xpath).send_keys(data.first_name)

    def Enter_last_name(self):
        self.driver.find_element(By.XPATH, elements.last_name_xpath).send_keys(data.last_name)

    def Enter_bapsid(self):
        self.driver.find_element(By.XPATH, elements.baps_id_xpath).send_keys(data.misId)

    def global_search_button(self):
        self.driver.find_element(By.XPATH, elements.global_search_button_xpath).click()

    def global_name_verify(self):
        misid = self.driver.find_element(By.XPATH, elements.mis_id_verification_xpath)
        misid_text = misid.text
        assert misid_text == f"{data.misId}"
        pass
        print("A global_search works fine")
        self.driver.quit()







