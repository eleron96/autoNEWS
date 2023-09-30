import requests

def chat_with_gpt_api(input_text):
    API_ENDPOINT = "https://api.openai.com/v1/engines/davinci/completions"  # Примерный URL, может отличаться
    HEADERS = {
        "Authorization": "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",  # Замените YOUR_API_KEY на ваш ключ API
        "Content-Type": "application/json"
    }
    DATA = {
        "prompt": input_text,
        "max_tokens": 150
    }

    response = requests.post(API_ENDPOINT, headers=HEADERS, json=DATA)
    response_data = response.json()

    return response_data.get("choices", [{}])[0].get("text", "").strip()
