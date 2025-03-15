import time

from openpyxl.styles.builtins import normal
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
import allure


#@pytest.mark.usefixtures("setup")
@allure.title("Название теста")
@allure.description("Описание теста")
@allure.severity(allure.severity_level.CRITICAL)
class TestOne(BaseClass):

    @allure.step("Выполнение теста")
    def test_e2e(self):
        log = self.getlogger()
        homePage = HomePage(self.driver)
        self.driver.implicitly_wait(10)
        # driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        # self.driver.find_element(By.XPATH, "//a[contains(@href,'shop')]").click()
        with allure.step('Открыть страницу авторизации'):
            checkoutPage = homePage.shopItems()
        log.info("Getting all cards titles!")
        cards = checkoutPage.getCardTitles()
        i=-1
        for card in cards:
            i+=1
            log.info(card.text)
            if card.text =="Blackberry":
                checkoutPage.getCardFooter()[i].click()
        #self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn']").click()
        checkoutPage.getcheckoutbutton().click()
        #self.driver.find_element(By.CSS_SELECTOR, "button[class*='btn-success']").click()
        confirmPage=checkoutPage.checkOutItems()

        #self.driver.find_element(By.CSS_SELECTOR, "#country").send_keys("ind")
        confirmPage.getCountry().send_keys("ind")
        self.verifyLinkPresence("India")
        #self.driver.find_element(By.LINK_TEXT, "India").click()
        confirmPage.getIndia().click()
        #self.driver.find_element(By.XPATH, "//div[contains(@class,'checkbox-primary')]").click()
        confirmPage.getCheck().click()
        #self.driver.find_element(By.XPATH, "//*[@type='submit']").click()
        confirmPage.getSubmit().click()
        msg = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        log.info(msg)
        assert "Success" in msg
        time.sleep(6)