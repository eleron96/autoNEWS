import os
import openai
import datetime
import re  # Импортируем модуль регулярных выражений
import textwrap

# Чтение API ключа из файла
with open("api_key.txt", "r") as file:
    openai.api_key = file.read().strip()

# Функция для удаления лишних пробелов и пустых строк
def clean_text(text):
    # Удаление лишних пробелов и пустых строк
    return re.sub(r'\n\s*\n', '\n', text.strip())

# Функция для отправки текста в API и получения ответа
def summarize_text(text, author):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user",
                       "content": f"Summarize the following text(Blog) "
                                  f"written by {author}."
                                  f"use name autor in the text."
                                  f"Rewrite the text in your own words as a freeform paraphrase. "
                                  f"Make the story engaging and seamless. Limit the word count to 150:\n{text}"}],
            temperature=0.5, # Temperature может быть полезно увеличить для более творческих ответов
            max_tokens=1024  # Ограничиваем ответ до 1024 токенов
        )
        message = response['choices'][0]['message']['content']
        return clean_text(message)  # Очистка полученного текста
    except Exception as e:
        return str(e)


# Сохранение текста в файл
def save_summary(author, summary):
    date_string = datetime.datetime.now().strftime("%Y_%m_%d")
    filename = f"summary/{date_string}_{author}.txt"

    os.makedirs("summary",
                exist_ok=True)  # Создание папки summary, если она не существует

    with open(filename, "w", encoding="utf-8") as file:
        file.write(summary)

# Вывод результата
def print_summarized_text(summarized_text):
    decorated_text = "\n" + "="*30 + " Summarized Text " + "="*30 + "\n"
    # textwrap.wrap возвращает список строк, которые соответствуют заданной ширине. 80 - это примерное значение,
    # вы можете установить его в зависимости от вашей консоли. Затем мы соединяем строки с помощью "\n" для печати.
    wrapped_text = "\n".join(textwrap.wrap(summarized_text, width=80))
    decorated_text += wrapped_text + "\n" + "="*80 + "\n"
    print(decorated_text)


# Ввод имени автора
author = input("Please input the author's name: ")

# Ввод текста пользователем
print(
    "Please input the text you want summarized. Input 'END' in a new line to finish.")
user_input_lines = []
while True:
    line = input()
    if line == 'END':
        break
    user_input_lines.append(line)

user_input_text = "\n".join(user_input_lines)

# Получаем и выводим пересказанный текст
print("\nSending text to OpenAI GPT...")
summarized_text = summarize_text(user_input_text, author)

# Выводим красиво оформленный текст
print_summarized_text(summarized_text)

# Сохраняем пересказанный текст в файл
save_summary(author, summarized_text)
