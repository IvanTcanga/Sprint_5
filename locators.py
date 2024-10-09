from selenium.webdriver.common.by import By


def contains(class_name):
	return f'//*[contains(concat(" ",normalize-space(@class)," ")," {class_name} ")]'


class Locators:

	NAME_INPUT_FIELD = [By.XPATH, '//label[ text()="Имя" ]/parent::div/input']

	EMAIL_INPUT_FIELD = [By.XPATH, '//label[ text()="Email" ]/parent::div/input']

	PASSWORD_INPUT_FIELD = [By.XPATH, '//label[ text()="Пароль" ]/parent::div/input']

	SIGN_IN_ACCOUNT_BUTTON = (By.XPATH, '//button[ text()="Войти в аккаунт" ]') #кнопка входа в аккаунт

	REGISTRATION_HREF = (By.XPATH, '//a[ text()="Зарегистрироваться" ]') #ссылка регистрации

	REGISTRATION_BUTTON = (By.XPATH, '//button[ text()="Зарегистрироваться" ]') #кнопка регистрации

	CHECKOUT_BUTTON = (By.XPATH, '//button[ text()="Оформить заказ" ]') #кнопка оформить заказ

	LOGIN_BUTTON = (By.XPATH, '//button[ text()="Войти" ]') #кнопка войти

	INVALID_PASSWORD_ERROR = (By.XPATH, '//p[ text()="Некорректный пароль" ]') #ошибка неккоректный пароль

	PERSONAL_ACCOUNT_LINK = (By.XPATH, '//p[contains(text(),"Личный Кабинет")]') #личный кабинет

	LOGIN_LINK = (By.XPATH, '//a[ text()="Войти" ]') #ссылка на кнопку войти

	RESET_PASSWORD_LINK = (By.XPATH, '//a[ text()="Восстановить пароль" ]') #ссылка на кнопку восстановить пароль

	BUTTON_RESET = (By.XPATH, '//button[ text()="Восстановить" ]') #кнопка восстановить

	BUTTON_EXIT_FROM_ACCOUNT = (By.XPATH, '//button[ text()="Выход" ]') #кнопка Выход

	CONSTRUCTOR_BUTTON = (By.XPATH, '//p[contains(text(),"Конструктор")]') #constructor button

	ROLLS_h = (By.XPATH, '//span[text()="Булки"]/parent::div') #раздел булки

	SAUCES_h = (By.XPATH, '//span[text()="Соусы"]/parent::div') #раздел соусы

	FILLINGS_h = (By.XPATH, '//span[text()="Начинки"]/parent::div') #раздел начинка

	LOGO_STELLAR_BURGER_MAIN_PAGE = (By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]') #logo stellar burger main page