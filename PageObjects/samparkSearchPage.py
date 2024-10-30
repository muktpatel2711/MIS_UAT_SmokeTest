from selenium.webdriver.common.by import By
from selenium import webdriver
from utilities import elements
from TestData import data

class samparksearch:
    def __init__(self,driver):
        self.driver=driver

    def clicksmanage_sampark(self):
        self.driver.find_element(By.XPATH, elements.manage_sampark_xpath).click()

    def clicksampark_search(self):
        self.driver.find_element(By.XPATH, elements.search_sampark_Karyakar_xpath).click()

    def clicksampark_button(self):
        self.driver.find_element(By.XPATH, elements.sampark_search_button).click()


    def sampark_count_verify(self):
        page_no = self.driver.find_element(By.XPATH, elements.sampark_count_xpath)
        page_no_text = page_no.text
        assert page_no_text == "10"
        pass
        print("A sampark search works fine")
        self.driver.quit()








