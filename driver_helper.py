from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions  as EC

from data import Data


class DriverHelper:
    def __init__(self, driver):
        self.driver = driver

    def wait_get_element(self, locator):
       return WebDriverWait(self.driver, Data.DEFAULT_TIMEOUT).until(EC.visibility_of_element_located(locator))
