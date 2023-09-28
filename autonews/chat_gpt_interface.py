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
        driver.get("https://chat.openai.com/?model=gpt-4")

        # Найдите поле ввода и введите ваш текст
        input_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#prompt-textarea"))
        )
        input_element.send_keys(input_text)

        # Нажмите кнопку отправки
        send_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='send-button']"))
        )
        send_button.click()

        # Ждите ответа и извлеките его (вам также понадобится CSS-селектор для поля ответа)
        response_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-testid^='conversation-turn-'] div.markdown.prose"))
        )
        response_text = response_element.text

        return response_text

    finally:
        driver.quit()
