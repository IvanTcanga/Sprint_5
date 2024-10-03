import pytest
from selenium import webdriver
import random
from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()


@pytest.fixture
def account_registration(driver, generate_email, generate_password):

    name = 'Ivan'
    email = generate_email
    password = generate_password

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

    driver.get("https://stellarburgers.nomoreparties.site/")

    yield email, password


@pytest.fixture
def generate_email():
    username = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz', random.randint(2, 10)))
    email = f"{username}@ya.ru"
    yield email


@pytest.fixture
def generate_password():
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
    password = ''.join(random.sample(characters, random.randint(6, 10)))
    yield password

