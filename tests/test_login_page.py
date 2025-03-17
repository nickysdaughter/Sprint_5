from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import driver
import locators


class TestLoginPage:

    #вход по кнопке «Войти в аккаунт» на главной
    def test_main_page_login_button_successful(self, driver):
        driver.find_element(By.XPATH, locators.sign_in_button).click()
        driver.find_element(By.XPATH, locators.email_field_login_page).send_keys('kuratova_19@mail.ru')
        driver.find_element(By.XPATH, locators.password_field_login_page).send_keys('123456789')
        driver.find_element(By.XPATH, locators.sign_in_button_login_page).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.make_order_button)))
        make_order_element = driver.find_element(By.XPATH, locators.make_order_button)

        assert make_order_element.is_displayed()

    # вход через кнопку «Личный кабинет»
    def test_login_main_page_personal_account_button_successful(self, driver):
        driver.find_element(By.XPATH, locators.personal_account_button).click()
        driver.find_element(By.XPATH, locators.email_field_login_page).send_keys('kuratova_19@mail.ru')
        driver.find_element(By.XPATH, locators.password_field_login_page).send_keys('123456789')
        driver.find_element(By.XPATH, locators.sign_in_button_login_page).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.make_order_button)))
        make_order_element = driver.find_element(By.XPATH, locators.make_order_button)

        assert make_order_element.is_displayed()

    #вход через кнопку в форме регистрации
    def test_login_register_page_successful(self, driver):
        driver.find_element(By.XPATH, locators.personal_account_button).click()
        driver.find_element(By.XPATH, locators.sign_up_link).click()
        driver.find_element(By.XPATH, locators.sign_in_btn_register_page).click()
        driver.find_element(By.XPATH, locators.email_field_login_page).send_keys('kuratova_19@mail.ru')
        driver.find_element(By.XPATH, locators.password_field_login_page).send_keys('123456789')
        driver.find_element(By.XPATH, locators.sign_in_button_login_page).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.make_order_button)))
        make_order_element = driver.find_element(By.XPATH, locators.make_order_button)

        assert make_order_element.is_displayed()

    #вход через кнопку в форме восстановления пароля
    def test_sign_in_password_recovery_successful(self, driver):
        driver.find_element(By.XPATH, locators.personal_account_button).click()
        driver.find_element(By.XPATH, locators.password_recovery_btn).click()
        driver.find_element(By.XPATH, locators.sign_in_butn_forgot_password_page).click()
        driver.find_element(By.XPATH, locators.email_field_login_page).send_keys('kuratova_19@mail.ru')
        driver.find_element(By.XPATH, locators.password_field_login_page).send_keys('123456789')
        driver.find_element(By.XPATH, locators.sign_in_button_login_page).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.make_order_button)))
        make_order_element = driver.find_element(By.XPATH, locators.make_order_button)

        assert make_order_element.is_displayed()







