# кнопка "Войти в аккаунт"
from copyreg import constructor

sign_in_button = './/button[text() = "Войти в аккаунт"]'

# ссылка "Зарегистрироваться"
sign_up_link = '//a[text() = "Зарегистрироваться"]'

# поле для ввода имени на странице регистрации
name_field = '//fieldset[1]//input[@name="name"]'

# поле для ввода email
email_field = '//fieldset[2]//input[@name="name"]'

# поле для ввода пароля
password_field = './/input[@name = "Пароль"]'

# кнопка "Зарегистрироваться"
registration_button = '//button[text() = "Зарегистрироваться"]'

# кнопка "Войти"
login_button = "//button[text() = 'Войти']"

# ошибка при некорректном пароле
invalid_password_error = "//p[text() = 'Некорректный пароль']"

# поле для ввода email на странице авторизации
email_field_login_page = "//label[text()='Email']/following-sibling::input"

# поле для пароля на странице авторизации
password_field_login_page = "//input[@name = 'Пароль']"

# кнопка "Войти" на странице авторизации
sign_in_button_login_page = "//button[text() = 'Войти']"

# кнопка "Оформить заказ"
make_order_button = "//button[text() = 'Оформить заказ']"

# кнопка "Личный кабинет"
personal_account_button = "//p[text() = 'Личный Кабинет']"

# кнопка "Войти" на странице регистрации
sign_in_btn_register_page = "//a[text() = 'Войти']"

# кнопка "Восстановить пароль"
password_recovery_btn = "//a[text() = 'Восстановить пароль']"

# кнопка "Войти" на странице восстановления пароля
sign_in_butn_forgot_password_page = "//a[text() = 'Войти']"

# кнопка "Конструктор"
constructor_btn = ".//p[text() = 'Конструктор']"

# логотип stellar burgers
main_logo = "//div[@class='AppHeader_header__logo__2D0X2']"

# кнопка "Выход" в личном кабинете
logout_btn = "//button[text() = 'Выход']"

# блок "Соусы"
sauces_section = "//div[.='Соусы']"

# блок "Булки"
buns_section = "//div[.='Булки']"

# блок "Начинки"
toppings_section = "//div[.='Начинки']"

# заголовок "Булки"
buns_header = "//h2[.='Булки']"

# заголовок "Соусы"
sauces_header = "//h2[.='Соусы']"

# заголовок "Начинки"
toppings_header = "//h2[.='Начинки']"