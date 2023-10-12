import tkinter as tk
from tkinter import ttk
from api_handler import summarize_text
from db_handler import create_table, insert_summary, get_summaries
import datetime


class App:
    def __init__(self, root):
        self.root = root
        root.title("AutoNews Summarizer")
        self.create_main_frame()

    def create_main_frame(self):
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(expand=True)

        self.button_new_request = ttk.Button(self.main_frame, text="New Request", command=self.create_request_frame, width=20)
        self.button_new_request.pack(pady=5, ipadx=20, ipady=10)

        self.button_view_summaries = ttk.Button(self.main_frame, text="View Summaries", command=self.create_summaries_frame, width=20)
        self.button_view_summaries.pack(pady=5, ipadx=20, ipady=10)

        self.button_exit = ttk.Button(self.main_frame, text="Exit", command=self.root.destroy, width=20)
        self.button_exit.pack(pady=5, ipadx=20, ipady=10)

    def create_request_frame(self):
        self.main_frame.pack_forget()
        self.request_frame = ttk.Frame(self.root)
        self.request_frame.pack(fill=tk.BOTH, expand=True)

        self.label_author = ttk.Label(self.request_frame, text="Author:")
        self.label_author.pack(pady=5)

        self.entry_author = ttk.Entry(self.request_frame)
        self.entry_author.pack(pady=5, padx=5, fill=tk.X)

        self.label_text = ttk.Label(self.request_frame, text="Blog Text:")
        self.label_text.pack(pady=5)

        self.text_blog = tk.Text(self.request_frame, height=10)
        self.text_blog.pack(pady=5, padx=5, fill=tk.X)

        self.label_article_title = ttk.Label(self.request_frame,
                                             text="Article Title:")
        self.label_article_title.pack(pady=5)

        self.entry_article_title = ttk.Entry(self.request_frame, width=50)
        self.entry_article_title.pack(pady=5, padx=5, fill=tk.X)

        self.label_article_link = ttk.Label(self.request_frame,
                                            text="Article Link:")
        self.label_article_link.pack(pady=5)

        self.entry_article_link = ttk.Entry(self.request_frame, width=50)
        self.entry_article_link.pack(pady=5, padx=5, fill=tk.X)

        self.button_exit = ttk.Button(self.request_frame, text="Exit",
                                      command=self.root.destroy)
        self.button_exit.pack(pady=5, side=tk.RIGHT)

        self.button_back = ttk.Button(self.request_frame, text="Back",
                                      command=self.back_to_main_from_request)
        self.button_back.pack(pady=5, side=tk.RIGHT)

        self.button_submit = ttk.Button(self.request_frame, text="Submit",
                                        command=self.submit)
        self.button_submit.pack(pady=5, side=tk.RIGHT)





    def back_to_main_from_request(self):
        self.request_frame.pack_forget()
        self.create_main_frame()

    def submit(self):
        author = self.entry_author.get()
        blog_text = self.text_blog.get("1.0", tk.END)
        summarized_text = summarize_text(blog_text, author)

        date_string = datetime.datetime.now().strftime("%Y-%m-%d")
        insert_summary(author, summarized_text, date_string, self.entry_article_title.get(), self.entry_article_link.get())

        self.request_frame.pack_forget()
        self.show_result(summarized_text)

    def show_result(self, summarized_text):
        self.result_frame = ttk.Frame(self.root)
        self.result_frame.pack(fill=tk.BOTH, expand=True)

        self.text_result = tk.Text(self.result_frame, height=10, width=80)
        self.text_result.insert(tk.END, summarized_text)
        self.text_result.pack(pady=5, padx=5, fill=tk.X)

        self.button_close = ttk.Button(self.result_frame, text="Close",
                                       command=self.back_to_main_from_result)
        self.button_close.pack(pady=5)

    def back_to_main_from_result(self):
        self.result_frame.pack_forget()
        self.create_main_frame()

    def create_summaries_frame(self):
        self.main_frame.pack_forget()
        self.summaries_frame = ttk.Frame(self.root)
        self.summaries_frame.pack(fill=tk.BOTH, expand=True)

        self.listbox_summaries = tk.Listbox(self.summaries_frame, height=10, width=80)
        self.listbox_summaries.pack(pady=5, padx=5, fill=tk.X)

        summaries = get_summaries()
        for summary in summaries:
            # Используйте article_title как короткую тему
            short_topic = summary[4]  # article_title из вашей базы данных
            display_text = f"{summary[3]} | {summary[1]} | {short_topic} | {len(summary[2])} chars"
            self.listbox_summaries.insert(tk.END, display_text)

        self.listbox_summaries.bind('<Double-1>', self.view_summary)

    def view_summary(self, event=None):
        selected_index = self.listbox_summaries.curselection()
        if not selected_index:
            return

        summary = get_summaries()[selected_index[0]]
        author = summary[1]
        text = summary[2]
        article_title = summary[4]  # Добавлено
        article_link = summary[5]   # Добавлено

        self.summaries_frame.pack_forget()
        self.show_summary_detail(author, text, article_title, article_link)

    def show_summary_detail(self, author, text, article_title=None, article_link=None):
        self.summary_detail_frame = ttk.Frame(self.root)
        self.summary_detail_frame.pack(fill=tk.BOTH, expand=True)

        self.text_author = tk.Text(self.summary_detail_frame, height=1,
                                   width=50)
        self.text_author.insert(tk.END, f"Author: {author}")
        self.text_author.config(
            state=tk.DISABLED)  # Сделать текстовое поле только для чтения
        self.text_author.pack(pady=5)

        self.text_summary = tk.Text(self.summary_detail_frame, height=10,
                                    width=80)
        self.text_summary.insert(tk.END, text)
        self.text_summary.pack(pady=5, padx=5, fill=tk.X)

        self.text_article_title = tk.Text(self.summary_detail_frame, height=1,
                                          width=50)
        self.text_article_title.insert(tk.END,
                                       f"Article Title: {article_title}")
        self.text_article_title.config(
            state=tk.DISABLED)  # Сделать текстовое поле только для чтения
        self.text_article_title.pack(pady=5)

        self.text_article_link = tk.Text(self.summary_detail_frame, height=1,
                                         width=50)
        self.text_article_link.insert(tk.END, f"Article Link: {article_link}")
        self.text_article_link.config(
            state=tk.DISABLED)  # Сделать текстовое поле только для чтения
        self.text_article_link.pack(pady=5)

        self.button_close = ttk.Button(self.summary_detail_frame, text="Exit",
                                       command=self.close_summary_detail)
        self.button_close.pack(pady=5, side=tk.RIGHT)

        self.button_back = ttk.Button(self.summary_detail_frame, text="Back",
                                      command=self.back_to_summaries_from_detail)
        self.button_back.pack(pady=5, side=tk.RIGHT)

    def close_summary_detail(self):
        self.summary_detail_frame.pack_forget()
        self.create_main_frame()

    def back_to_summaries_from_detail(self):
        self.summary_detail_frame.pack_forget()
        self.create_summaries_frame()


def start_gui():
    root = tk.Tk()
    root.geometry("600x400")  # Задаем одинаковый размер для всех окон
    app = App(root)
    root.mainloop()
