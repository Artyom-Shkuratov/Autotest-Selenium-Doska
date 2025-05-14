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

