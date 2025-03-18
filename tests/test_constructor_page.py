from selenium.webdriver.common.by import By

import helpers
from conftest import driver
import locators


class TestConstructorPage:

    def test_from_personal_page_to_constructor_page_by_btn(self, driver):
        helpers.successful_login(driver)
        driver.find_element(By.XPATH, locators.PERSONAL_ACCOUNT_BTN).click()
        driver.find_element(By.XPATH, locators.CONSTRUCTOR_BTN).click()
        make_order_element = driver.find_element(By.XPATH, locators.MAKE_ORDER_BTN)

        assert make_order_element.is_displayed()

    def test_from_personal_page_to_constructor_page_by_logo(self, driver):
        helpers.successful_login(driver)
        driver.find_element(By.XPATH, locators.PERSONAL_ACCOUNT_BTN).click()
        driver.find_element(By.XPATH, locators.MAIN_LOGO).click()
        make_order_element = driver.find_element(By.XPATH, locators.MAKE_ORDER_BTN)

        assert make_order_element.is_displayed()

    def test_transfer_from_buns_to_sauce_section_successes(self, driver):
        driver.find_element(By.XPATH, locators.SAUCES_SECTION).click()
        sauces_header_element = driver.find_element(By.XPATH, locators.SAUCES_HEADER)

        assert sauces_header_element.is_displayed()

    def test_transfer_from_sauce_to_toppings_section_successes(self, driver):
        driver.find_element(By.XPATH, locators.SAUCES_SECTION).click()
        driver.find_element(By.XPATH, locators.TOPPINGS_SECTION).click()
        toppings_section_element = driver.find_element(By.XPATH, locators.TOPPINGS_HEADER)

        assert toppings_section_element.is_displayed()

    def test_transfer_from_buns_to_toppings_section_successes(self, driver):
        driver.find_element(By.XPATH, locators.TOPPINGS_SECTION).click()
        toppings_section_element = driver.find_element(By.XPATH, locators.TOPPINGS_HEADER)

        assert toppings_section_element.is_displayed()

    def test_transfer_from_toppings_to_sauce_section_successes(self, driver):
        driver.find_element(By.XPATH, locators.TOPPINGS_SECTION).click()
        driver.find_element(By.XPATH, locators.SAUCES_SECTION).click()
        sauces_header_element = driver.find_element(By.XPATH, locators.SAUCES_HEADER)

        assert sauces_header_element.is_displayed()

    def test_transfer_from_sauce_to_buns_section_successes(self, driver):
        driver.find_element(By.XPATH, locators.SAUCES_SECTION).click()
        driver.find_element(By.XPATH, locators.BUNS_SECTION).click()
        buns_header_element = driver.find_element(By.XPATH, locators.BUNS_HEADER)

        assert buns_header_element.is_displayed()

    def test_transfer_toppings_to_buns_section_successes(self, driver):
        driver.find_element(By.XPATH, locators.TOPPINGS_SECTION).click()
        driver.find_element(By.XPATH, locators.BUNS_SECTION).click()
        buns_header_element = driver.find_element(By.XPATH, locators.BUNS_HEADER)

        assert buns_header_element.is_displayed()













