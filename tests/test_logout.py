from driver_helper import DriverHelper
from locators import Locators


class TestLogout:

    def test_logout_successful(self, driver_in):
        wb = DriverHelper(driver_in)
        wb.wait_get_element(Locators.TOP_MENU_PROFILE_LINK).click()
        wb.wait_get_element(Locators.LOGOUT_BUTTON).click()
        wb.wait_get_element(Locators.LOGIN_BUTTON)
        assert driver_in.find_element(*Locators.LOGIN_FORM_LABEL).is_displayed() == True