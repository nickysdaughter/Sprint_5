import pytest
from conftest import driver
import helpers
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import locators


class TestRegistration:

    def test_registration_new_account_successful_submit(self, driver):
        driver.find_element(By.XPATH, locators.SIGN_IN_BTN).click()
        driver.find_element(By.XPATH, locators.SIGN_OP_LINK).click()
        driver.find_element(By.XPATH, locators.NAME_FIELD).send_keys('test')
        driver.find_element(By.XPATH, locators.EMAIL_FIELD).send_keys(helpers.generate_email())
        driver.find_element(By.XPATH, locators.PASSWORD_FIELD).send_keys(helpers.generate_password())
        driver.find_element(By.XPATH, locators.REGISTRATION_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.LOGIN_BTN)))

        assert 'login' in driver.current_url

    def test_registration_without_name_failed_submit(self, driver):
        driver.find_element(By.XPATH, locators.SIGN_IN_BTN).click()
        driver.find_element(By.XPATH, locators.SIGN_OP_LINK).click()
        driver.find_element(By.XPATH, locators.NAME_FIELD).send_keys('')
        driver.find_element(By.XPATH, locators.EMAIL_FIELD).send_keys(helpers.generate_email())
        driver.find_element(By.XPATH, locators.PASSWORD_FIELD).send_keys(helpers.generate_password())
        driver.find_element(By.XPATH, locators.REGISTRATION_BTN).click()

        assert 'register' in driver.current_url

    @pytest.mark.parametrize('invalid_email', ['', '@mail.com', 'test@.com', 'test@mail'])
    def test_registration_with_invalid_email_failed_submit(self, driver, invalid_email):
        driver.find_element(By.XPATH, locators.SIGN_IN_BTN).click()
        driver.find_element(By.XPATH, locators.SIGN_OP_LINK).click()
        driver.find_element(By.XPATH, locators.NAME_FIELD).send_keys('test')
        driver.find_element(By.XPATH, locators.EMAIL_FIELD).send_keys(invalid_email)
        driver.find_element(By.XPATH, locators.PASSWORD_FIELD).send_keys(helpers.generate_password())
        driver.find_element(By.XPATH, locators.REGISTRATION_BTN).click()

        assert 'register' in driver.current_url

    @pytest.mark.parametrize('invalid_password', ['1','12345'])
    def test_registration_with_invalid_length_password_failed_submit(self, driver, invalid_password):
        driver.find_element(By.XPATH, locators.SIGN_IN_BTN).click()
        driver.find_element(By.XPATH, locators.SIGN_OP_LINK).click()
        driver.find_element(By.XPATH, locators.NAME_FIELD).send_keys('test')
        driver.find_element(By.XPATH, locators.EMAIL_FIELD).send_keys(helpers.generate_email())
        driver.find_element(By.XPATH, locators.PASSWORD_FIELD).send_keys(invalid_password)
        driver.find_element(By.XPATH, locators.REGISTRATION_BTN).click()

        error_element = driver.find_element(By.XPATH, locators.INVALID_PASSWORD_ERROR)

        assert error_element.is_displayed()

    def test_registration_with_empty_password_failed_submit(self, driver):
        driver.find_element(By.XPATH, locators.SIGN_IN_BTN).click()
        driver.find_element(By.XPATH, locators.SIGN_OP_LINK).click()
        driver.find_element(By.XPATH, locators.NAME_FIELD).send_keys('test')
        driver.find_element(By.XPATH, locators.EMAIL_FIELD).send_keys(helpers.generate_email())
        driver.find_element(By.XPATH, locators.PASSWORD_FIELD).send_keys('')
        driver.find_element(By.XPATH, locators.REGISTRATION_BTN).click()

        assert 'register' in driver.current_url














