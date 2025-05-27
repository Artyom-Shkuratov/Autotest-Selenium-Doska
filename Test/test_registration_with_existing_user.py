from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.locators import *
from locators.urls import BASE_URL
from utilits.data import existing_email, valid_password


class TestRegistrationWithExistingUser:
    def test_register_existing_user(self, driver):
        driver.get(BASE_URL)

        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(LOGIN_REGISTER_BUTTON)).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(NO_ACCOUNT_BUTTON)).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(EMAIL_INPUT)).send_keys(existing_email)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(PASSWORD_INPUT)).send_keys(valid_password)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(REPEAT_PASSWORD_INPUT)).send_keys(valid_password)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(CREATE_ACC_BUTTON)).click()

        error = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(EMAIL_ERROR))
        assert error.is_displayed(), "Ожидалась ошибка под email"

        name_locators = [
            EMAIL_INPUT_BY_NAME,
            PASSWORD_INPUT_BY_NAME,
            SUBMIT_PASSWORD_INPUT_BY_NAME
        ]

        for locator in name_locators:
            wrapper = driver.find_element(*locator).find_element(*PARENT_DIV_BY_XPATH)
            class_value = wrapper.get_attribute("class")
            assert "input_inputError" in class_value, f"Поле {locator[1]} не подсвечено красным"
