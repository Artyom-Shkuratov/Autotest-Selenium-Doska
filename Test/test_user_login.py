import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.locators import *
from locators.urls import BASE_URL



class TestUSerLogin:
    def test_user_login(self,driver,existing_email,valid_password):

        driver.get(BASE_URL)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(LOGIN_REGISTER_BUTTON)).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(EMAIL_INPUT)).send_keys(existing_email)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(PASSWORD_INPUT)).send_keys(valid_password)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(LOGIN_BUTTON)).click()

        avatar = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(USER_AVATAR))
        user_name = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(USER_NAME)).text
        
        assert user_name == "User.", f"Ошибка! Имя пользовталея '{user_name}'"
        assert avatar.is_displayed(), "Аватар пользователя не отображается"
        