from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


class TestConstructor:
	def test_switching_to_sauces(self, driver):

		driver.find_element(*Locators.SAUCES_h).click()
		sauces = driver.find_element(*Locators.SAUCES_h)
		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.SAUCES_h))

		assert 'tab_tab_type_current_' in sauces.get_attribute('class')

	def test_switching_to_rolls(self, driver):
		driver.find_element(*Locators.SAUCES_h).click()
		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.SAUCES_h))

		driver.find_element(*Locators.ROLLS_h).click()
		rolls = driver.find_element(*Locators.ROLLS_h)
		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.ROLLS_h))

		assert 'tab_tab_type_current_' in rolls.get_attribute('class')

	def test_switching_to_fillings(self, driver):
		driver.find_element(*Locators.FILLINGS_h).click()

		fillings = driver.find_element(*Locators.FILLINGS_h)
		WebDriverWait(driver, 6).until(
			expected_conditions.visibility_of_element_located(Locators.FILLINGS_h))

		assert 'tab_tab_type_current_' in fillings.get_attribute('class')
