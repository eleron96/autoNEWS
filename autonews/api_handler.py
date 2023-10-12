import openai
import re

# Чтение API ключа из файла
with open("api_key.txt", "r") as file:
    openai.api_key = file.read().strip()

def clean_text(text):
    return re.sub(r'\\n\\s*\\n', '\\n', text.strip())

def summarize_text(text, author):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role": "user",
                "content": f"Summarize the following text(Blog) "
                           f"written by {author}."
                           f"use name autor in the text."
                           f"Rewrite the text in your own words as a freeform paraphrase. "
                           f"Make the story engaging and seamless. Limit the word count to 150:\n{text}"
            }],
            temperature=0.5,
            max_tokens=1024
        )
        message = response['choices'][0]['message']['content']
        return clean_text(message)
    except Exception as e:
        return str(e)
