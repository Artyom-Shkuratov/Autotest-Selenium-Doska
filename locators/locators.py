from selenium.webdriver.common.by import By


LOGIN_REGISTER_BUTTON = (By.XPATH, ".//button[contains(text(), 'Вход и регистрация')]")
NO_ACCOUNT_BUTTON = (By.XPATH, ".//button[contains(text(), 'Нет аккаунта')]")
EMAIL_INPUT = (By.NAME, "email")
PASSWORD_INPUT = (By.NAME, "password")
REPEAT_PASSWORD_INPUT = (By.NAME, "submitPassword")
CREATE_ACC_BUTTON = (By.CSS_SELECTOR, "button.buttonPrimary.inButtonText[style*='max-width: 192px']")
USER_AVATAR = (By.CSS_SELECTOR, "button.circleSmall")
USER_NAME = (By.XPATH, ".//h3[contains(@class, 'name') and text()='User.']")
EMAIL_ERROR = (By.XPATH, ".//span[contains(text(), 'Ошибка')]")
LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")
LOGOUT_BUTTON = (By.XPATH, ".//button[contains(text(), 'Выйти')]")
CREATE_AD_BUTTON = (By.XPATH, ".//button[contains(text(), 'Разместить объявление')]")
PUBLISH_AD_BITTON = (By.XPATH, ".//button[contains(text(), 'Опубликовать')]")

TITLE = (By.XPATH, ".//input[@placeholder='Название']")
DESCRIPTION = (By.XPATH, "//textarea[@placeholder='Описание товара']")
PRICE = (By.XPATH, ".//input[@placeholder='Стоимость']")
RADIO_BUTTON = (By.CLASS_NAME, "radioUnput_inputRegular__FbVbr")