import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.locators import *
from locators.urls import BASE_URL



class TestLogoutUserAfterLogin:
    def test_logout_user_after_login(self,driver,valid_password,existing_email):
        driver.get(BASE_URL)
        
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(LOGIN_REGISTER_BUTTON)).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(EMAIL_INPUT)).send_keys(existing_email)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(PASSWORD_INPUT)).send_keys(valid_password)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(LOGIN_BUTTON)).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(LOGOUT_BUTTON)).click()
        
        assert  WebDriverWait(driver, 5).until(EC.invisibility_of_element_located(USER_AVATAR)), "Аватар должен исчезнуть после выхода"
        assert  WebDriverWait(driver, 5).until(EC.invisibility_of_element_located(USER_NAME)), "Имя пользователя должно исчезнуть после выхода"

