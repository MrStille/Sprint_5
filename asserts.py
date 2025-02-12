from driver_helper import DriverHelper
from locators import Locators


class PageAsserts:

    @staticmethod
    def assert_login_page_loaded(driver):
        wb = DriverHelper(driver)
        wb.wait_get_element(Locators.EMAIL_INPUT)
        wb.wait_get_element(Locators.LOGIN_FORM_LABEL)