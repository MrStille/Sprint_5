from selenium.webdriver.common.by import By

from driver_helper import DriverHelper
from locators import Locators


class TestConstructorPage:
    def test_scroll_to_toppings(self, driver):
        wb = DriverHelper(driver)
        wb.wait_get_element(Locators.MIDDLE_MENU_TOPPINGS).click()
        wb.wait_get_element(Locators.FOOD_ITEMS)
        parent_div = driver.find_element(By.XPATH, Locators.MIDDLE_MENU_TOPPINGS[1] + "/parent::div")
        css = parent_div.get_attribute("class")
        assert "tab_tab_type_current" in css

    def test_scroll_to_buns(self, driver):
        wb = DriverHelper(driver)
        wb.wait_get_element(Locators.MIDDLE_MENU_SAUCES).click()
        wb.wait_get_element(Locators.MIDDLE_MENU_BUNS).click()
        wb.wait_get_element(Locators.FOOD_ITEMS)
        parent_div = driver.find_element(By.XPATH, Locators.MIDDLE_MENU_BUNS[1] + "/parent::div")
        css = parent_div.get_attribute("class")
        assert "tab_tab_type_current" in css

    def test_scroll_to_sauces(self, driver):
        wb = DriverHelper(driver)
        wb.wait_get_element(Locators.MIDDLE_MENU_SAUCES).click()
        wb.wait_get_element(Locators.FOOD_ITEMS)
        parent_div = driver.find_element(By.XPATH, Locators.MIDDLE_MENU_SAUCES[1] + "/parent::div")
        css = parent_div.get_attribute("class")
        assert "tab_tab_type_current" in css
