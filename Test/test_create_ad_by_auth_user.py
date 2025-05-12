from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.locators import *
import time


def test_create_ad_by_auth_user(driver,existing_email,valid_password,ad_data):

    driver.get("https://qa-desk.stand.praktikum-services.ru/")
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(LOGIN_REGISTER_BUTTON)).click()
    
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(EMAIL_INPUT)).send_keys(existing_email)
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(PASSWORD_INPUT)).send_keys(valid_password)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(LOGIN_BUTTON)).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable(CREATE_AD_BUTTON)).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TITLE)).send_keys(ad_data["title"])
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ".//button[contains(@class, 'dropDownMenu_arrowDown')]"))).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ".//span[text()='Технологии']"))).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(RADIO_BUTTON)).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "(.//button[contains(@class, 'dropDownMenu_arrowDown')])[2]"))).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ".//span[text()='Санкт-Петербург']"))).click()
    
    description_input = WebDriverWait(driver,5).until(EC.visibility_of_element_located(DESCRIPTION))
    driver.execute_script("arguments[0].scrollIntoView();", description_input)
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(DESCRIPTION)).send_keys(ad_data["description"])
    price_input = WebDriverWait(driver,5).until(EC.visibility_of_element_located(PRICE)) 
    driver.execute_script("arguments[0].scrollIntoView();", price_input)
    
    price_input.send_keys(ad_data['price'])
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable(PUBLISH_AD_BITTON)).click()
    driver.find_element(*USER_AVATAR).click()
    
    ads_section = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//h1[text()='Мои объявления']")))
    driver.execute_script("arguments[0].scrollIntoView();", ads_section)
    ad_title = ad_title = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, f".//div[@class='about']/h2[text()='{ad_data['title']}']")))
    
    
    assert ad_title.is_displayed(), f'Объявление с заголовком {ad_data["title"]} не найдено на странице профиля'
    
    driver.quit()
