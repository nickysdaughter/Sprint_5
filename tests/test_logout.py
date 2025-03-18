from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import driver
import testhelpers
import locators


class TestLogout:

    def test_logout_in_profile_page_successful(self, driver):
        testhelpers.successful_login(driver)
        driver.find_element(By.XPATH, locators.PERSONAL_ACCOUNT_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.LOGOUT_BTN)))
        driver.find_element(By.XPATH, locators.LOGOUT_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.SIGN_IN_BTN_LOGIN_PAGE)))

        assert 'login' in driver.current_url
