def get_input_from_user(prompt):
    return input(prompt)

def save_blog_summary(blog_text, author_name):
    if not blog_text or not author_name:
        print("Ошибка ввода: Пожалуйста, заполните все поля")
        return

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
    """.format(blog_text, author_name)  # Тут ваш шаблон, я его сократил для краткости

    with open("blog_summary.txt", "w", encoding="utf-8") as file:
        file.write(summary_template)

    print("Пересказ блога сохранен в файл 'blog_summary.txt'")

def main_menu():
    while True:
        print("\nМеню:")
        print("1. Создать пересказ блога")
        print("2. Выход")
        choice = get_input_from_user("Выберите действие (1/2): ")

        if choice == "1":
            blog_text = get_input_from_user("\nВведите текст блога: ")
            author_name = get_input_from_user("Введите имя автора: ")
            save_blog_summary(blog_text, author_name)
        elif choice == "2":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    print("Добро пожаловать в консольное приложение 'Блог Пересказ'!")
    main_menu()
