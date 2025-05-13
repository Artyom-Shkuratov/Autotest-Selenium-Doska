import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.locators import *
from locators.urls import BASE_URL



class TestRegisterUser:
    def test_login_existing_user(self,driver, email):
        
        driver.get(BASE_URL)

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(LOGIN_REGISTER_BUTTON)).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(NO_ACCOUNT_BUTTON)).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(EMAIL_INPUT)).send_keys(email)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PASSWORD_INPUT)).send_keys("Password123")
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(REPEAT_PASSWORD_INPUT)).send_keys("Password123")
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(CREATE_ACC_BUTTON)).click()

        avatar = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(USER_AVATAR))
        user_name = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(USER_NAME)).text
        
        assert user_name == "User.", f"Ошибка! Имя пользовталея '{user_name}'"
        assert avatar.is_displayed(), "Аватар пользователя не отображается"
        