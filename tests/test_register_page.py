import pytest
from conftest import driver
import testhelpers
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import locators


class TestRegistration:

    def test_registration_new_account_successful_submit(self, driver):
        driver.find_element(By.XPATH, locators.sign_in_button).click()
        driver.find_element(By.XPATH, locators.sign_up_link).click()
        driver.find_element(By.XPATH, locators.name_field).send_keys('test')
        driver.find_element(By.XPATH, locators.email_field).send_keys(testhelpers.TestHelpers.generate_email())
        driver.find_element(By.XPATH, locators.password_field).send_keys(testhelpers.TestHelpers.generate_password())
        driver.find_element(By.XPATH, locators.registration_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.login_button)))

        assert 'login' in driver.current_url

    def test_registration_without_name_failed_submit(self, driver):
        driver.find_element(By.XPATH, locators.sign_in_button).click()
        driver.find_element(By.XPATH, locators.sign_up_link).click()
        driver.find_element(By.XPATH, locators.name_field).send_keys('')
        driver.find_element(By.XPATH, locators.email_field).send_keys(testhelpers.TestHelpers.generate_email())
        driver.find_element(By.XPATH, locators.password_field).send_keys(testhelpers.TestHelpers.generate_password())
        driver.find_element(By.XPATH, locators.registration_button).click()

        assert 'register' in driver.current_url

    @pytest.mark.parametrize('invalid_email', ['', '@mail.com', 'test@.com', 'test@mail'])
    def test_registration_with_invalid_email_failed_submit(self, driver, invalid_email):
        driver.find_element(By.XPATH, locators.sign_in_button).click()
        driver.find_element(By.XPATH, locators.sign_up_link).click()
        driver.find_element(By.XPATH, locators.name_field).send_keys('test')
        driver.find_element(By.XPATH, locators.email_field).send_keys(invalid_email)
        driver.find_element(By.XPATH, locators.password_field).send_keys(testhelpers.TestHelpers.generate_password())
        driver.find_element(By.XPATH, locators.registration_button).click()

        assert 'register' in driver.current_url

    @pytest.mark.parametrize('invalid_password', ['1','12345'])
    def test_registration_with_invalid_length_password_failed_submit(self, driver, invalid_password):
        driver.find_element(By.XPATH, locators.sign_in_button).click()
        driver.find_element(By.XPATH, locators.sign_up_link).click()
        driver.find_element(By.XPATH, locators.name_field).send_keys('test')
        driver.find_element(By.XPATH, locators.email_field).send_keys(testhelpers.TestHelpers.generate_email())
        driver.find_element(By.XPATH, locators.password_field).send_keys(invalid_password)
        driver.find_element(By.XPATH, locators.registration_button).click()

        error_element = driver.find_element(By.XPATH, locators.invalid_password_error)

        assert error_element.is_displayed()

    def test_registration_with_empty_password_failed_submit(self, driver):
        driver.find_element(By.XPATH, locators.sign_in_button).click()
        driver.find_element(By.XPATH, locators.sign_up_link).click()
        driver.find_element(By.XPATH, locators.name_field).send_keys('test')
        driver.find_element(By.XPATH, locators.email_field).send_keys(testhelpers.TestHelpers.generate_email())
        driver.find_element(By.XPATH, locators.password_field).send_keys('')
        driver.find_element(By.XPATH, locators.registration_button).click()

        assert 'register' in driver.current_url














