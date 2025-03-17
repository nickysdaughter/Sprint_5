from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import driver
import testhelpers
import locators


class TestLogout:

    def test_logout_in_profile_page_successful(self, driver):
        testhelpers.TestHelpers.successful_login(driver)
        driver.find_element(By.XPATH, locators.personal_account_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.logout_btn)))
        driver.find_element(By.XPATH, locators.logout_btn).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.sign_in_button_login_page)))

        assert 'login' in driver.current_url
