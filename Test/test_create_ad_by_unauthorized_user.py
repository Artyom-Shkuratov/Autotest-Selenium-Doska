import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.locators import *

def test_create_ad_by_unauthorized_user(driver):
    driver.get("https://qa-desk.stand.praktikum-services.ru/")

    WebDriverWait(driver, 3).until(EC.element_to_be_clickable(CREATE_AD_BUTTON)).click()
    modal_window = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, ".//h1[contains(text(), 'Чтобы разместить объявление, авторизуйтесь')]")))
    assert modal_window.is_displayed(), "Окно входа не отображается!"
    driver.quit()
