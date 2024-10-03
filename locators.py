from selenium.webdriver.common.by import By


def contains(class_name):
	return f'//*[contains(concat(" ",normalize-space(@class)," ")," {class_name} ")]'


class Locators:

	NAME_INPUT_FIELD = [By.XPATH, '//label[ text()="Имя" ]/parent::div/input']

	EMAIL_INPUT_FIELD = [By.XPATH, '//label[ text()="Email" ]/parent::div/input']

	PASSWORD_INPUT_FIELD = [By.XPATH, '//label[ text()="Пароль" ]/parent::div/input']

	SIGN_IN_ACCOUNT_BUTTON = (By.XPATH, '//button[ text()="Войти в аккаунт" ]') #кнопка входа в аккаунт

	REGISTRATION_HREF = (By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a') #ссылка регистрации

	REGISTRATION_BUTTON = (By.XPATH, '//button[ text()="Зарегистрироваться" ]') #кнопка регистрации

	CHECKOUT_BUTTON = (By.XPATH, '//button[ text()="Оформить заказ" ]') #кнопка оформить заказ

	LOGIN_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/form/button') #кнопка войти

	INVALID_PASSWORD_ERROR = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/p') #ошибка пароля

	PERSONAL_ACCOUNT_LINK = (By.XPATH, '//*[@id="root"]/div/header/nav/a/p') #личный кабинет

	LOGIN_LINK = (By.XPATH, '//*[@id="root"]/div/main/div/div/p/a') #ссылка на кнопку войти

	RESET_PASSWORD_LINK = (By.XPATH, '//*[@id="root"]/div/main/div/div/p[2]/a') #ссылка на кнопку восстановить пароль

	BUTTON_RESET = (By.XPATH, '//*[@id="root"]/div/main/div/form/button') #кнопка восстановить

	BUTTON_EXIT_FROM_ACCOUNT = (By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[3]/button') #кнопка выхода из аккаунта

	CONSTRUCTOR_BUTTON = (By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[1]/a') #constructor button

	ROLLS_h = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]') #раздел rolls

	SAUCES_h = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]') #раздел sauces

	FILLINGS_h = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]') #раздел fillings

	SAUCE_CART_FOR_ASSERT = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[2]/a[1]') #карточка соуса

	ROLLS_CART_FOR_ASSERT = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[1]/a[1]') #карточка булок

	FILLINGS_CART_FOR_ASSERT = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[3]/a[1]') #карточка начинок

	LOGO_STELLAR_BURGER_MAIN_PAGE = (By.XPATH, '//*[@id="root"]/div/header/nav/div/a/svg') #logo stellar burger main page