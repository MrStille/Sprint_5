import pytest

from data import Data
from driver_helper import DriverHelper
from locators import Locators


class TestProfilePage:
    def test_open_profile_page(self, driver_in):
        wb = DriverHelper(driver_in)
        wb.wait_get_element(Locators.TOP_MENU_PROFILE_LINK).click()
        name = wb.wait_get_element(Locators.PROFILE_NAME_INPUT)
        login = driver_in.find_element(*Locators.PROFILE_EMAIL_INPUT)
        assert name.get_attribute('value') == Data.NAME
        assert login.get_attribute('value') == Data.EMAIL

    def test_return_to_construct_page(self, driver_in):
        wb = DriverHelper(driver_in)
        wb.wait_get_element(Locators.TOP_MENU_PROFILE_LINK).click()
        wb.wait_get_element(Locators.PROFILE_NAME_INPUT)
        wb.wait_get_element(Locators.TOP_MENU_CONSTRUCTOR_LINK).click()
        wb.wait_get_element(Locators.FOOD_ITEMS)
        items = driver_in.find_elements(*Locators.FOOD_ITEMS)
        assert len(items) > 1
        assert items[0].is_displayed() == True

