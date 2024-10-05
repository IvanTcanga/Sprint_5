from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


class TestPersonalAccount:
	def test_switching_to_account_with_personal_account_link(self, driver, account_registration):
		email, password = account_registration
		driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()

		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))

		driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(email)
		driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(password)

		driver.find_element(*Locators.LOGIN_BUTTON).click()
		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.CHECKOUT_BUTTON))

		driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()

		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.BUTTON_EXIT_FROM_ACCOUNT))

		assert driver.find_element(*Locators.BUTTON_EXIT_FROM_ACCOUNT).is_displayed()

	def test_switching_to_constructor_from_account(self, driver, account_registration):
		email, password = account_registration
		driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()

		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))

		driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(email)
		driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(password)

		driver.find_element(*Locators.LOGIN_BUTTON).click()
		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.CHECKOUT_BUTTON))

		driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()
		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.BUTTON_EXIT_FROM_ACCOUNT))

		driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.CHECKOUT_BUTTON))

		assert driver.find_element(*Locators.CHECKOUT_BUTTON).is_displayed()

	def test_switching_to_constructor_from_account_with_logo(self, driver, account_registration):
		email, password = account_registration
		driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()

		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))

		driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(email)
		driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(password)

		driver.find_element(*Locators.LOGIN_BUTTON).click()
		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.CHECKOUT_BUTTON))

		driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()
		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.BUTTON_EXIT_FROM_ACCOUNT))

		driver.find_element(*Locators.LOGO_STELLAR_BURGER_MAIN_PAGE).click()
		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.CHECKOUT_BUTTON))

		assert driver.find_element(*Locators.CHECKOUT_BUTTON).is_displayed()

	def test_logout_from_account(self, driver, account_registration):
		email, password = account_registration
		driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()

		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))

		driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(email)
		driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(password)

		driver.find_element(*Locators.LOGIN_BUTTON).click()
		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.CHECKOUT_BUTTON))

		driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()

		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.BUTTON_EXIT_FROM_ACCOUNT))

		driver.find_element(*Locators.BUTTON_EXIT_FROM_ACCOUNT).click()
		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))

		assert driver.find_element(*Locators.LOGIN_BUTTON).is_displayed()
