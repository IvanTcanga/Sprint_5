from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from helpers.helpers import DataGenerator
import pytest


class TestRegistrationPage:

	def test_registration_success(self, driver):
		email = DataGenerator.generate_email()
		password = DataGenerator.generate_password()

		driver.find_element(*Locators.SIGN_IN_ACCOUNT_BUTTON).click()

		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.REGISTRATION_HREF))

		driver.find_element(*Locators.REGISTRATION_HREF).click()

		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.REGISTRATION_BUTTON))

		driver.find_element(*Locators.NAME_INPUT_FIELD).send_keys('Ivan')
		driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(email)
		driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(password)

		driver.find_element(*Locators.REGISTRATION_BUTTON).click()

		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))

		driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(email)
		driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(password)

		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))

		driver.find_element(*Locators.LOGIN_BUTTON).click()

		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.CHECKOUT_BUTTON))

		assert driver.find_element(*Locators.CHECKOUT_BUTTON).is_displayed()

	def test_negative_empty_field_name_not_submitted(self, driver):
		driver.find_element(*Locators.SIGN_IN_ACCOUNT_BUTTON).click()

		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.REGISTRATION_HREF))

		driver.find_element(*Locators.REGISTRATION_HREF).click()

		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.REGISTRATION_BUTTON))

		driver.find_element(*Locators.NAME_INPUT_FIELD).send_keys('')
		driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(DataGenerator.generate_email())
		driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(DataGenerator.generate_password())

		driver.find_element(*Locators.REGISTRATION_BUTTON).click()

		assert driver.find_element(*Locators.REGISTRATION_BUTTON).is_displayed()

	@pytest.mark.parametrize("email", [
		"123ya.ru",
		"123@",
		"@ya.ru",
		"123@.ru",
		"123 @ya.ru",
		"123@ya!ru",
		"123@@ya.ru",
		"123#@ya.ru"
	])
	def test_negative_invalid_email_not_submitted(self, driver, email):
		driver.find_element(*Locators.SIGN_IN_ACCOUNT_BUTTON).click()

		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.REGISTRATION_HREF))

		driver.find_element(*Locators.REGISTRATION_HREF).click()

		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.REGISTRATION_BUTTON))

		driver.find_element(*Locators.NAME_INPUT_FIELD).send_keys('Ivan')
		driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(email)
		driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys('123456')

		driver.find_element(*Locators.REGISTRATION_BUTTON).click()

		assert driver.find_element(*Locators.REGISTRATION_BUTTON).is_displayed()

	@pytest.mark.parametrize("password", [
		" ",
		"a",
		"12",
		"abc",
		"1234",
		"abcde"
	])
	def test_passwords_show_error(self, driver, password):
		driver.find_element(*Locators.SIGN_IN_ACCOUNT_BUTTON).click()

		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.REGISTRATION_HREF))

		driver.find_element(*Locators.REGISTRATION_HREF).click()

		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.REGISTRATION_BUTTON))

		driver.find_element(*Locators.NAME_INPUT_FIELD).send_keys('Ivan')
		driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys('ivan123@ya.ru')
		driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(password)

		driver.find_element(*Locators.REGISTRATION_BUTTON).click()
		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.INVALID_PASSWORD_ERROR))

		assert driver.find_element(*Locators.INVALID_PASSWORD_ERROR).text == 'Некорректный пароль'
