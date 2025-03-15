from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:
    def __init__(self,driver):
        self.driver = driver

    shop = (By.XPATH, "//a[contains(@href,'shop')]")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    check1 = (By.ID, "exampleCheck1")
    submit = (By.XPATH, "//input[@type='submit']")
    alert = (By.CLASS_NAME, "alert-success")
    gender = (By.ID, "exampleFormControlSelect1")
    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage
        # self.driver.find_element(By.XPATH, "//a[contains(@href,'shop')]").click()

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getCheck1(self):
        return self.driver.find_element(*HomePage.check1)

    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getAlert(self):
        return self.driver.find_element(*HomePage.alert).text

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)