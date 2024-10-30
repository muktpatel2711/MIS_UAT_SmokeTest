from selenium.webdriver.common.by import By
from selenium import webdriver
from utilities import elements
from TestData import data

class searchBusiness:
    def __init__(self,driver):
        self.driver=driver

    def clicksmanage_business(self):
        self.driver.find_element(By.XPATH, elements.manage_business_xpath).click()

    def clickbusiness_search(self):
        self.driver.find_element(By.XPATH, elements.search_business_xpath).click()

    def clickbusiness_search_button(self):
        self.driver.find_element(By.XPATH, elements.search_business_button_xpath).click()


    def business_count_verify(self):
        page_no = self.driver.find_element(By.XPATH, elements.business_count_xpath)
        page_no_text = page_no.text
        assert page_no_text == "10"
        pass
        print("A Business search works fine")
        self.driver.quit()








