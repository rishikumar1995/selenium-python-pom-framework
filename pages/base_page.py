from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator))

    def find(self, locator):
        return self.wait_for_element(locator)

    def type(self, locator, text):
        self.find(locator).send_keys(text)
