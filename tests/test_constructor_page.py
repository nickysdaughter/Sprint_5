from selenium.webdriver.common.by import By

from conftest import driver
from testhelpers import TestHelpers
import locators


class TestConstructorPage:

    def test_from_personal_page_to_constructor_page_by_btn(self, driver):
        TestHelpers.successful_login(driver)
        driver.find_element(By.XPATH, locators.personal_account_button).click()
        driver.find_element(By.XPATH, locators.constructor_btn).click()
        make_order_element = driver.find_element(By.XPATH, locators.make_order_button)

        assert make_order_element.is_displayed()

    def test_from_personal_page_to_constructor_page_by_logo(self, driver):
        TestHelpers.successful_login(driver)
        driver.find_element(By.XPATH, locators.personal_account_button).click()
        driver.find_element(By.XPATH, locators.main_logo).click()
        make_order_element = driver.find_element(By.XPATH, locators.make_order_button)

        assert make_order_element.is_displayed()

    def test_transfer_from_buns_to_sauce_section_successes(self, driver):
        driver.find_element(By.XPATH, locators.sauces_section).click()
        sauces_header_element = driver.find_element(By.XPATH, locators.sauces_header)

        assert sauces_header_element.is_displayed()

    def test_transfer_from_sauce_to_toppings_section_successes(self, driver):
        driver.find_element(By.XPATH, locators.sauces_section).click()
        driver.find_element(By.XPATH, locators.toppings_section).click()
        toppings_section_element = driver.find_element(By.XPATH, locators.toppings_header)

        assert toppings_section_element.is_displayed()

    def test_transfer_from_buns_to_toppings_section_successes(self, driver):
        driver.find_element(By.XPATH, locators.toppings_section).click()
        toppings_section_element = driver.find_element(By.XPATH, locators.toppings_header)

        assert toppings_section_element.is_displayed()

    def test_transfer_from_toppings_to_sauce_section_successes(self, driver):
        driver.find_element(By.XPATH, locators.toppings_section).click()
        driver.find_element(By.XPATH, locators.sauces_section).click()
        sauces_header_element = driver.find_element(By.XPATH, locators.sauces_header)

        assert sauces_header_element.is_displayed()

    def test_transfer_from_sauce_to_buns_section_successes(self, driver):
        driver.find_element(By.XPATH, locators.sauces_section).click()
        driver.find_element(By.XPATH, locators.buns_section).click()
        buns_header_element = driver.find_element(By.XPATH, locators.buns_header)

        assert buns_header_element.is_displayed()

    def test_transfer_toppings_to_buns_section_successes(self, driver):
        driver.find_element(By.XPATH, locators.toppings_section).click()
        driver.find_element(By.XPATH, locators.buns_section).click()
        buns_header_element = driver.find_element(By.XPATH, locators.buns_header)

        assert buns_header_element.is_displayed()













