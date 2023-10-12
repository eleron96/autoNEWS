import os
import datetime

def save_summary(author, summary):
    date_string = datetime.datetime.now().strftime("%Y_%m_%d")
    filename = f"summary/{date_string}_{author}.txt"

    os.makedirs("summary", exist_ok=True)

    with open(filename, "w", encoding="utf-8") as file:
        file.write(summary)
