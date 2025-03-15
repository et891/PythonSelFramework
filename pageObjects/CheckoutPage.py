from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    # r = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkoutbutton = (By.XPATH, "//a[contains(@class,'btn')]")
    checkoutbutton2 = (By.XPATH, "//button[@class = 'btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckoutPage.cardFooter)

    def getcheckoutbutton(self):
        return self.driver.find_element(*CheckoutPage.checkoutbutton)

    def checkOutItems(self):
        self.driver.find_element(*CheckoutPage.checkoutbutton2).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
