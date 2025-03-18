# кнопка "Войти в аккаунт"
from copyreg import constructor

from selenium.webdriver.common.devtools.v85.service_worker import RegistrationID

SIGN_IN_BTN = './/button[text() = "Войти в аккаунт"]'

# ссылка "Зарегистрироваться"
SIGN_OP_LINK = '//a[text() = "Зарегистрироваться"]'

# поле для ввода имени на странице регистрации
NAME_FIELD = '//fieldset[1]//input[@name="name"]'

# поле для ввода email
EMAIL_FIELD = '//fieldset[2]//input[@name="name"]'

# поле для ввода пароля
PASSWORD_FIELD = './/input[@name = "Пароль"]'

# кнопка "Зарегистрироваться"
REGISTRATION_BTN = '//button[text() = "Зарегистрироваться"]'

# кнопка "Войти"
LOGIN_BTN = "//button[text() = 'Войти']"

# ошибка при некорректном пароле
INVALID_PASSWORD_ERROR = "//p[text() = 'Некорректный пароль']"

# поле для ввода email на странице авторизации
EMAIL_FIELD_LOGIN_PAGE = "//label[text()='Email']/following-sibling::input"

# поле для пароля на странице авторизации
PASSWORD_FIELD_LOGIN_PAGE = "//input[@name = 'Пароль']"

# кнопка "Войти" на странице авторизации
SIGN_IN_BTN_LOGIN_PAGE = "//button[text() = 'Войти']"

# кнопка "Оформить заказ"
MAKE_ORDER_BTN = "//button[text() = 'Оформить заказ']"

# кнопка "Личный кабинет"
PERSONAL_ACCOUNT_BTN = "//p[text() = 'Личный Кабинет']"

# кнопка "Войти" на странице регистрации
SIGN_IN_BTN_REGISTER_PAGE = "//a[text() = 'Войти']"

# кнопка "Восстановить пароль"
PASSWORD_RECOVERY_BTN = "//a[text() = 'Восстановить пароль']"

# кнопка "Войти" на странице восстановления пароля
SIGN_IN_BTN_FORGOT_PASSWORD_PAGE = "//a[text() = 'Войти']"

# кнопка "Конструктор"
CONSTRUCTOR_BTN = ".//p[text() = 'Конструктор']"

# логотип stellar burgers
MAIN_LOGO = "//div[@class='AppHeader_header__logo__2D0X2']"

# кнопка "Выход" в личном кабинете
LOGOUT_BTN = "//button[text() = 'Выход']"

# блок "Соусы"
SAUCES_SECTION = "//div[.='Соусы']"

# блок "Булки"
BUNS_SECTION = "//div[.='Булки']"

# блок "Начинки"
TOPPINGS_SECTION = "//div[.='Начинки']"

# заголовок "Булки"
BUNS_HEADER = "//h2[.='Булки']"

# заголовок "Соусы"
SAUCES_HEADER = "//h2[.='Соусы']"

# заголовок "Начинки"
TOPPINGS_HEADER = "//h2[.='Начинки']"