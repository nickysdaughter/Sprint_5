from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import driver
import locators
from data import UserData


class TestLoginPage:

    #вход по кнопке «Войти в аккаунт» на главной
    def test_main_page_login_button_successful(self, driver):
        driver.find_element(By.XPATH, locators.SIGN_IN_BTN).click()
        driver.find_element(By.XPATH, locators.EMAIL_FIELD_LOGIN_PAGE).send_keys(UserData.email)
        driver.find_element(By.XPATH, locators.PASSWORD_FIELD_LOGIN_PAGE).send_keys(UserData.password)
        driver.find_element(By.XPATH, locators.SIGN_IN_BTN_LOGIN_PAGE).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.MAKE_ORDER_BTN)))
        make_order_element = driver.find_element(By.XPATH, locators.MAKE_ORDER_BTN)

        assert make_order_element.is_displayed()

    # вход через кнопку «Личный кабинет»
    def test_login_main_page_personal_account_button_successful(self, driver):
        driver.find_element(By.XPATH, locators.PERSONAL_ACCOUNT_BTN).click()
        driver.find_element(By.XPATH, locators.EMAIL_FIELD_LOGIN_PAGE).send_keys(UserData.email)
        driver.find_element(By.XPATH, locators.PASSWORD_FIELD_LOGIN_PAGE).send_keys(UserData.password)
        driver.find_element(By.XPATH, locators.SIGN_IN_BTN_LOGIN_PAGE).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.MAKE_ORDER_BTN)))
        make_order_element = driver.find_element(By.XPATH, locators.MAKE_ORDER_BTN)

        assert make_order_element.is_displayed()

    #вход через кнопку в форме регистрации
    def test_login_register_page_successful(self, driver):
        driver.find_element(By.XPATH, locators.PERSONAL_ACCOUNT_BTN).click()
        driver.find_element(By.XPATH, locators.SIGN_OP_LINK).click()
        driver.find_element(By.XPATH, locators.SIGN_IN_BTN_REGISTER_PAGE).click()
        driver.find_element(By.XPATH, locators.EMAIL_FIELD_LOGIN_PAGE).send_keys(UserData.email)
        driver.find_element(By.XPATH, locators.PASSWORD_FIELD_LOGIN_PAGE).send_keys(UserData.password)
        driver.find_element(By.XPATH, locators.SIGN_IN_BTN_LOGIN_PAGE).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.MAKE_ORDER_BTN)))
        make_order_element = driver.find_element(By.XPATH, locators.MAKE_ORDER_BTN)

        assert make_order_element.is_displayed()

    #вход через кнопку в форме восстановления пароля
    def test_sign_in_password_recovery_successful(self, driver):
        driver.find_element(By.XPATH, locators.PERSONAL_ACCOUNT_BTN).click()
        driver.find_element(By.XPATH, locators.PASSWORD_RECOVERY_BTN).click()
        driver.find_element(By.XPATH, locators.SIGN_IN_BTN_FORGOT_PASSWORD_PAGE).click()
        driver.find_element(By.XPATH, locators.EMAIL_FIELD_LOGIN_PAGE).send_keys(UserData.email)
        driver.find_element(By.XPATH, locators.PASSWORD_FIELD_LOGIN_PAGE).send_keys(UserData.password)
        driver.find_element(By.XPATH, locators.SIGN_IN_BTN_LOGIN_PAGE).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.MAKE_ORDER_BTN)))
        make_order_element = driver.find_element(By.XPATH, locators.MAKE_ORDER_BTN)

        assert make_order_element.is_displayed()







