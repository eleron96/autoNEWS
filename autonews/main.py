import os
import datetime
from autonews.chat_gpt_interface import chat_with_gpt


def get_input_from_user(prompt):
    return input(prompt)


def save_blog_summary(blog_text, author_name):
    if not blog_text or not author_name:
        print("Ошибка ввода: Пожалуйста, заполните все поля")
        return

    # Убедитесь, что папка 'summary' существует
    if not os.path.exists("summary"):
        os.makedirs("summary")

    current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"summary_{current_time}.txt"
    filepath = os.path.join("summary", filename)


    summary_template = """
    Напиши короткий пересказ на блог ниже ( я его пометил Блог). 
    Вот дополнительные правила:
    - пересказ должен указывать автора
    - текст должен быть кратким пересказом оригинального
    - используй форматирование текста 
    - не пересказывай весь блог. только важное. 150 слов . а в конце напиши "подробнее можно прочитать по ссылке"

    вот пример логики пересказа
    "Плагин, который управляет плагинами Revit – о чём ещё можно мечтать долгими летними вечерами? Скорее читайте статью от Николаса и качайте DiRoots App Manager! 
    «Quickly Enable / Disable Revit Plugins with DiRoots App Manager»"

    вот сам блог
    [{}]

    blog by [{}]
    """.format(blog_text,
               author_name)  # Тут ваш шаблон, я его сократил для краткости

    with open(filepath, "w", encoding="utf-8") as file:
        file.write(summary_template)

    # Получите ответ от Chat GPT
    gpt_response = chat_with_gpt(summary_template)

    # Добавьте ответ в файл пересказа
    with open(filepath, "a", encoding="utf-8") as file:
        file.write("\n\n" + gpt_response)

    print(f"Пересказ блога и ответ от Chat GPT сохранены в файл '{filepath}'")

def view_summary_history():
    summaries = os.listdir("summary")
    if not summaries:
        print("Нет сохраненных пересказов.")
        return

    print("Список всех сохраненных пересказов:")
    for index, summary in enumerate(summaries, 1):
        print(f"{index}. {summary}")

    choice = input("Введите номер пересказа, который вы хотите просмотреть, или 'q' для выхода: ")
    if choice.lower() == 'q':
        return

    try:
        selected_summary = summaries[int(choice) - 1]
        with open(os.path.join("summary", selected_summary), "r", encoding="utf-8") as file:
            content = file.read()
            print(content)
    except (ValueError, IndexError):
        print("Неверный выбор. Пожалуйста, попробуйте снова.")

def main_menu():
    while True:
        print("\nМеню:")
        print("1. Создать новый пересказ")
        print("2. Просмотреть историю пересказов")
        print("3. Выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            blog_text = get_input_from_user("\nВведите текст блога: ")
            author_name = get_input_from_user("Введите имя автора: ")
            save_blog_summary(blog_text, author_name)
        elif choice == "2":
            view_summary_history()
        elif choice == "3":
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    print("Добро пожаловать в консольное приложение 'Блог Пересказ'!")
    main_menu()
