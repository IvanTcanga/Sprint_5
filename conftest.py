import pytest
from selenium import webdriver
from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data.urls import URLs
from helpers.helpers import DataGenerator


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(URLs.BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def account_registration(driver):

    name = 'Ivan'
    email = DataGenerator.generate_email()
    password = DataGenerator.generate_password()

    driver.find_element(*Locators.SIGN_IN_ACCOUNT_BUTTON).click()

    WebDriverWait(driver, 6).until(
        expected_conditions.visibility_of_element_located(Locators.REGISTRATION_HREF))

    driver.find_element(*Locators.REGISTRATION_HREF).click()

    WebDriverWait(driver, 6).until(
        expected_conditions.visibility_of_element_located(Locators.REGISTRATION_BUTTON))

    driver.find_element(*Locators.NAME_INPUT_FIELD).send_keys(name)
    driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(email)
    driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(password)

    driver.find_element(*Locators.REGISTRATION_BUTTON).click()

    WebDriverWait(driver, 6).until(
        expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))

    driver.get(URLs.BASE_URL)

    yield email, password
