import pytest
from selenium import webdriver
from utilits.helpers import generate_random_email
from utilits import data


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    return driver

@pytest.fixture
def email():
    return generate_random_email()

@pytest.fixture
def existing_email():
    return data.existing_email

@pytest.fixture
def valid_password():
    return data.valid_password

@pytest.fixture
def ad_data():
    return data.ad_data
