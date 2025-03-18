from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import driver
import testhelpers
import locators

class TestProfilePage:

    def test_open_profile_page_successful(self, driver):
        testhelpers.successful_login(driver)
        driver.find_element(By.XPATH, locators.PERSONAL_ACCOUNT_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.LOGOUT_BTN)))

        assert 'profile' in driver.current_url
