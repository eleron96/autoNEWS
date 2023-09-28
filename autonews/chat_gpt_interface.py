from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def chat_with_gpt(input_text):
    # Инициализация драйвера (в этом примере используется Chrome)
    driver = webdriver.Chrome()

    try:
        # Откройте веб-интерфейс Chat GPT
        driver.get("https://chat.openai.com/?model=gpt-4")

        # Кликните по кнопке "Log in" перед отправкой текста
        login_button = WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='login-button']"))
        )
        login_button.click()

        # Введите имя пользователя
        username_input = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        username_input.send_keys("eleron96")

        # Нажмите кнопку "Continue" после ввода имени пользователя
        continue_button_username = WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button._button-login-id"))
        )
        continue_button_username.click()

        # Подождите 3 секунды
        time.sleep(3)

        # Введите пароль
        password_input = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        password_input.send_keys("Iamluckyman20")

        # Нажмите кнопку "Continue" после ввода пароля
        continue_button_password = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button._button-login-password"))
        )
        continue_button_password.click()

        # Найдите поле ввода и введите ваш текст
        input_element = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#prompt-textarea"))
        )
        input_element.send_keys(input_text)

        # Нажмите кнопку отправки
        send_button = WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='send-button']"))
        )
        send_button.click()

        # Ждите ответа и извлеките его (вам также понадобится CSS-селектор для поля ответа)
        response_element = WebDriverWait(driver, 500).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-testid^='conversation-turn-'] div.markdown.prose"))
        )
        response_text = response_element.text

        return response_text

    finally:
        driver.quit()
