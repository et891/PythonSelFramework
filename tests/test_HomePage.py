import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_formSubmission(self,getData):
        log = self.getlogger()
        homepage = HomePage(self.driver)
        log.info("Привет")
        print(self.driver.title)
        print(self.driver.current_url)
        homepage.getName().send_keys(getData["n"])
        log.info("Имя " + getData["n"])
        homepage.getEmail().send_keys("hello@gmail.com")
        homepage.getPassword().send_keys(getData["f"])
        homepage.getCheck1().click()
        self.selectOptionByText(homepage.getGender(), getData["g"])
        #driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
        #driver.find_element(By.ID, "exampleInputPassword1").send_keys("password")
        #driver.find_element(By.ID, "exampleCheck1").click()
        # XPATH - //tagname[@attribute='value']
        #driver.find_element(By.XPATH, "//input[@type='submit']").click()
        #message = driver.find_element(By.CLASS_NAME, "alert-success")
        homepage.getSubmit().click()
        message =homepage.getAlert()
        print(message)
        assert "Success" in message
        time.sleep(2)
        self.driver.refresh()
    @pytest.fixture(params=HomePageData.getTestData("Test1"))
    def getData(self,request):
        return request.param