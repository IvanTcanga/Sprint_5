from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


class TestLoginPage:

	def test_log_in_account_with_login_button(self, driver, account_registration):
		email, password = account_registration

		driver.find_element(*Locators.SIGN_IN_ACCOUNT_BUTTON).click()

		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))

		driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(email)
		driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(password)

		driver.find_element(*Locators.LOGIN_BUTTON).click()

		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.CHECKOUT_BUTTON))

		assert driver.find_element(*Locators.CHECKOUT_BUTTON).is_displayed()

	def test_log_in_account_with_personal_account_link(self, driver, account_registration):
		email, password = account_registration
		driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()

		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))

		driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(email)
		driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(password)

		driver.find_element(*Locators.LOGIN_BUTTON).click()

		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.CHECKOUT_BUTTON))

		assert driver.find_element(*Locators.CHECKOUT_BUTTON).is_displayed()

	def test_log_in_account_with_login_link_in_reg_form(self, driver, account_registration):
		email, password = account_registration

		driver.find_element(*Locators.SIGN_IN_ACCOUNT_BUTTON).click()

		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))

		driver.find_element(*Locators.REGISTRATION_HREF).click()

		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.REGISTRATION_BUTTON))

		driver.find_element(*Locators.LOGIN_LINK).click()
		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))

		driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(email)
		driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(password)

		driver.find_element(*Locators.LOGIN_BUTTON).click()

		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.CHECKOUT_BUTTON))

		assert driver.find_element(*Locators.CHECKOUT_BUTTON).is_displayed()

	def test_log_in_account_with_reset_password_link(self, driver, account_registration):
		email, password = account_registration

		driver.find_element(*Locators.SIGN_IN_ACCOUNT_BUTTON).click()

		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))

		driver.find_element(*Locators.RESET_PASSWORD_LINK).click()

		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.BUTTON_RESET))

		driver.find_element(*Locators.LOGIN_LINK).click()
		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))

		driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(email)
		driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(password)

		driver.find_element(*Locators.LOGIN_BUTTON).click()

		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.CHECKOUT_BUTTON))

		assert driver.find_element(*Locators.CHECKOUT_BUTTON).is_displayed()
