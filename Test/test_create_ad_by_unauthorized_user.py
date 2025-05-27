import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.locators import *
from locators.urls import BASE_URL


class TestCreateAdByUnauthorizedUser:
    def test_create_ad_by_unauthorized_user(self,driver):
        driver.get(BASE_URL)

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(CREATE_AD_BUTTON)).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MODAL_WINDOW))
        modal = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MODAL_WINDOW))
        assert modal.is_displayed(), "Окно входа не отображается!"
        
