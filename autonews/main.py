import os
import datetime
from chat_gpt_interface import \
    chat_with_gpt_api  # Импорт функции для взаимодействия с Chat GPT


def ensure_directory_exists(directory_name):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)


def save_summary_to_file(blog_text, author_name):
    ensure_directory_exists("summary")
    current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    current_date = datetime.datetime.now().strftime("%Y.%m.%d")
    filename = f"summary_{current_time}.txt"
    filepath = os.path.join("summary", filename)

    summary_template = """
    {}
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
    """.format(current_date, blog_text, author_name)

    gpt_response = chat_with_gpt_api(summary_template)

    with open(filepath, "w", encoding="utf-8") as file:
        file.write(gpt_response)

    return filepath


def get_all_summaries():
    return os.listdir("summary")


def read_summary_file(filename):
    with open(os.path.join("summary", filename), "r", encoding="utf-8") as file:
        return file.read()


def get_multiline_input(
        prompt="Введите текст (введите 'END' для завершения):\n"):
    lines = []
    print(prompt)
    while True:
        line = input()
        if line == "END":
            break
        lines.append(line)
    return "\n".join(lines)


def main_menu():
    while True:
        print("\nМеню:")
        print("1. Создать новый пересказ")
        print("2. Просмотреть историю пересказов")
        print("3. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            blog_text = get_multiline_input("\nВведите текст блога (введите 'END' для завершения):\n")
            author_name = input("Введите имя автора: ")

            if not blog_text or not author_name:
                print("Ошибка ввода: Пожалуйста, заполните все поля")
                continue

            filepath = save_summary_to_file(blog_text, author_name)
            print(
                f"Пересказ блога и ответ от Chat GPT сохранены в файл '{filepath}'")
        elif choice == "2":
            summaries = get_all_summaries()
            if not summaries:
                print("Нет сохраненных пересказов.")
                continue

            print("Список всех сохраненных пересказов:")
            for index, summary in enumerate(summaries, 1):
                print(f"{index}. {summary}")

            choice = input(
                "Введите номер пересказа, который вы хотите просмотреть, или 'q' для выхода: ")

            if choice.lower() == 'q':
                continue

            try:
                selected_summary = summaries[int(choice) - 1]
                content = read_summary_file(selected_summary)
                print(content)
            except (ValueError, IndexError):
                print("Неверный выбор. Пожалуйста, попробуйте снова.")
        elif choice == "3":
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    print("Добро пожаловать в консольное приложение 'Блог Пересказ'!")
    main_menu()
