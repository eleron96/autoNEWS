import subprocess

def get_input_from_user(placeholder):
    result = subprocess.run(["gum", "input", "--placeholder", placeholder], stdout=subprocess.PIPE, text=True)
    return result.stdout.strip()

def save_blog_summary(blog_text, author_name):
    if not blog_text or not author_name:
        print("Ошибка ввода: Пожалуйста, заполните все поля")
        return

    summary_template = """
    ...
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
