import tkinter as tk
from tkinter import messagebox
import os


def save_blog_summary():
    blog_text = text_entry.get("1.0", "end-1c")
    author_name = author_entry.get()

    if not blog_text or not author_name:
        messagebox.showwarning("Ошибка ввода", "Пожалуйста, заполните все поля")
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
    """.format(blog_text, author_name)

    with open("blog_summary.txt", "w", encoding="utf-8") as file:
        file.write(summary_template)

    messagebox.showinfo("Файл сохранен",
                        "Пересказ блога сохранен в файл 'blog_summary.txt'")


# Создание основного окна
root = tk.Tk()
root.title("Блог Пересказ")

# Создание и расположение виджетов
tk.Label(root, text="Текст блога:").pack(pady=5)
text_entry = tk.Text(root, width=50, height=10)
text_entry.pack(pady=5)

tk.Label(root, text="Автор:").pack(pady=5)
author_entry = tk.Entry(root, width=50)
author_entry.pack(pady=5)

tk.Button(root, text="Сохранить пересказ", command=save_blog_summary).pack(
    pady=20)

# Запуск основного цикла
root.mainloop()
