from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from locators.locators import *
from locators.urls import BASE_URL
from utilits.data import existing_email, valid_password, ad_data


def safe_click(driver, locator, timeout=5, attempts=3):
    for _ in range(attempts):
        try:
            WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator)).click()
            return
        except StaleElementReferenceException:
            continue
    raise Exception(f"Не удалось кликнуть по элементу {locator} после {attempts} попыток")


class TestCreareAdByAuthUser:
    def test_create_ad_by_auth_user(self, driver):
        driver.get(BASE_URL)

        safe_click(driver, LOGIN_REGISTER_BUTTON)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(EMAIL_INPUT)).send_keys(existing_email)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(PASSWORD_INPUT)).send_keys(valid_password)
        safe_click(driver, LOGIN_BUTTON)

        WebDriverWait(driver, 5).until(EC.presence_of_element_located(CREATE_AD_BUTTON))
        safe_click(driver, CREATE_AD_BUTTON)


        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TITLE)).send_keys(ad_data["title"])
        safe_click(driver, DROPDOWN_CATEGORY)
        safe_click(driver, CATEGORY_TECH)
        safe_click(driver, RADIO_BUTTON)
        safe_click(driver, DROPDOWN_CITY)
        safe_click(driver, CITY_SPB)

        description_input = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(DESCRIPTION))
        driver.execute_script("arguments[0].scrollIntoView();", description_input)
        description_input.send_keys(ad_data["description"])

        price_input = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(PRICE))
        driver.execute_script("arguments[0].scrollIntoView();", price_input)
        price_input.send_keys(ad_data["price"])
        

        safe_click(driver, PUBLISH_AD_BUTTON)
        WebDriverWait(driver, 7).until(EC.element_to_be_clickable(USER_AVATAR))
        safe_click(driver, USER_AVATAR)

        ads_section = WebDriverWait(driver, 7).until(EC.visibility_of_element_located(ADS__SECTION))
        driver.execute_script("arguments[0].scrollIntoView();", ads_section)

        ad_title_locator = (By.XPATH, AD_TITLE.format(ad_data["title"]))

        ad_title = WebDriverWait(driver, 7).until(EC.visibility_of_element_located(ad_title_locator))

        assert ad_title.is_displayed(), f'Объявление "{ad_data["title"]}" не найдено в блоке "Мои объявления"'
