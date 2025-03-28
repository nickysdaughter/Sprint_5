import string
import random

from selenium.webdriver.common.by import By
import locators

from conftest import driver
from data import UserData

def successful_login(driver):
        driver.find_element(By.XPATH, locators.SIGN_IN_BTN).click()
        driver.find_element(By.XPATH, locators.EMAIL_FIELD_LOGIN_PAGE).send_keys(UserData.email)
        driver.find_element(By.XPATH, locators.PASSWORD_FIELD_LOGIN_PAGE).send_keys(UserData.password)
        driver.find_element(By.XPATH, locators.SIGN_IN_BTN_LOGIN_PAGE).click()

def generate_email():
        random_email = f'kuratova_{random.randint(100, 999)}@yandex.ru'

        return random_email

def generate_password():
        random_letters = ''.join((random.choice(string.ascii_letters) for x in range(2)))
        random_password = f'qwerty_{random_letters}_{random.randint(10, 99)}'
        return random_password