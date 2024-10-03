from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


class TestConstructor:
	def test_switching_to_sauces(self, driver, account_registration):
		email, password = account_registration

		driver.find_element(*Locators.SIGN_IN_ACCOUNT_BUTTON).click()

		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))

		driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(email)
		driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(password)

		driver.find_element(*Locators.LOGIN_BUTTON).click()

		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.CHECKOUT_BUTTON))

		driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

		driver.find_elements(*Locators.SAUCES_h).click()
		sauces = driver.find_elements(*Locators.SAUCES_h)
		driver.execute_script("arguments[0].scrollIntoView();", sauces)
		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.SAUCE_CART_FOR_ASSERT))

		assert driver.find_element(*Locators.SAUCE_CART_FOR_ASSERT).is_displayed()

	def test_switching_to_rolls(self, driver, account_registration):
		email, password = account_registration

		driver.find_element(*Locators.SIGN_IN_ACCOUNT_BUTTON).click()

		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))

		driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(email)
		driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(password)

		driver.find_element(*Locators.LOGIN_BUTTON).click()

		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.CHECKOUT_BUTTON))

		driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

		driver.find_elements(*Locators.ROLLS_h).click()
		rolls = driver.find_elements(*Locators.ROLLS_h)
		driver.execute_script("arguments[0].scrollIntoView();", rolls)
		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.ROLLS_CART_FOR_ASSERT))

		assert driver.find_element(*Locators.ROLLS_CART_FOR_ASSERT).is_displayed()

	def test_switching_to_fillings(self, driver, account_registration):
		email, password = account_registration

		driver.find_element(*Locators.SIGN_IN_ACCOUNT_BUTTON).click()

		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))

		driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(email)
		driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(password)

		driver.find_element(*Locators.LOGIN_BUTTON).click()

		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.CHECKOUT_BUTTON))

		driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

		driver.find_elements(*Locators.FILLINGS_h).click()
		fillings = driver.find_elements(*Locators.FILLINGS_h)
		driver.execute_script("arguments[0].scrollIntoView();", fillings)
		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.FILLINGS_CART_FOR_ASSERT))

		assert driver.find_element(*Locators.FILLINGS_CART_FOR_ASSERT).is_displayed()
