from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def chat_with_gpt(input_text):
    # Инициализация драйвера (в этом примере используется Chrome)
    driver = webdriver.Chrome()

    try:
        # Откройте веб-интерфейс Chat GPT
        driver.get("URL_OF_CHAT_GPT_WEB_INTERFACE")

        # Найдите поле ввода и введите ваш текст
        input_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "CSS_SELECTOR_OF_INPUT_FIELD"))
        )
        input_element.send_keys(input_text)
        input_element.send_keys(Keys.RETURN)

        # Ждите ответа и извлеките его
        response_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "CSS_SELECTOR_OF_RESPONSE_FIELD"))
        )
        response_text = response_element.text

        return response_text

    finally:
        driver.quit()

