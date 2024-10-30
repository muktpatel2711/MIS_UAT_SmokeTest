from selenium.webdriver.common.by import By
from selenium import webdriver
from utilities import elements

class searchPerson:
    def __init__(self,driver):
        self.driver=driver
    def manage_person(self):
        self.driver.find_element(By.XPATH, elements.manage_person_xpath).click()

    def search_person(self):
        self.driver.find_element(By.XPATH, elements.search_person_xpath).click()

    def search_buttton(self):
        self.driver.find_element(By.XPATH, elements.serach_button_xpath).click()

    def verification_page(self):
        page_no = self.driver.find_element(By.XPATH, "//span[text()='10']")
        page_no_text = page_no.text
        assert page_no_text == "10"
        pass
        print("A search works fine")
        self.driver.quit()







