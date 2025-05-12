import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.locators import *


def test_register_existing_user(driver, existing_email, valid_password):
    
    driver.get("https://qa-desk.stand.praktikum-services.ru/")

    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(LOGIN_REGISTER_BUTTON)).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(NO_ACCOUNT_BUTTON)).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(EMAIL_INPUT)).send_keys(existing_email)
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(PASSWORD_INPUT)).send_keys(valid_password)
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(REPEAT_PASSWORD_INPUT)).send_keys(valid_password)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(CREATE_ACC_BUTTON)).click()
    
    error = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(EMAIL_ERROR))
    assert error.is_displayed(), "Ожидалась ошибка под email"
    
    for name in ["email", "password", "submitPassword"]:
        wrapper = driver.find_element(By.NAME, name).find_element(By.XPATH, "./parent::div")
        class_value = wrapper.get_attribute("class")
        assert "input_inputError" in class_value, f"Поле {name} не подсвечено красным"
    driver.quit()
