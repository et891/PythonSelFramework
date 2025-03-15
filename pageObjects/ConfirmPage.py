from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self,driver):
        self.driver = driver

    country = (By.CSS_SELECTOR, "#country")
    india = (By.LINK_TEXT, "India")
    check = (By.XPATH, "//div[contains(@class,'checkbox-primary')]")
    submit = (By.XPATH, "//*[@type='submit']")

    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.country)

    def getIndia(self):
        return self.driver.find_element(*ConfirmPage.india)

    def getCheck(self):
        return self.driver.find_element(*ConfirmPage.check)

    def getSubmit(self):
        return self.driver.find_element(*ConfirmPage.submit)