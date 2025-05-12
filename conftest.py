import pytest
import random
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    return driver


@pytest.fixture
def email():
    random_number = random.randint(1000, 9999)
    new_email = f"test{random_number}@example.com"
    return new_email

@pytest.fixture
def existing_email():
    return "test_test@test.ru"

@pytest.fixture
def valid_password():
    return "123456789!!!!!"

@pytest.fixture
def ad_data():
    return {
        "title": "Iphone 13 Pro 256 GB",
        "description": "Бу смартфон,есть царапины небольшие, аккумулятор 98%",
        "price": "25000"
    }