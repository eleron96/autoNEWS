import pytest
import sqlite3
from autonews import db_handler  # Пожалуйста, убедитесь, что путь импорта верен


# Фикстура для создания и удаления тестовой базы данных
@pytest.fixture
def setup_db():
    db_handler.create_table()  # Создание таблицы перед тестом
    yield
    conn = db_handler.create_connection()
    c = conn.cursor()
    c.execute('DROP TABLE summaries')  # Удаление таблицы после теста
    conn.commit()
    conn.close()


def test_insert_summary(setup_db):
    # Подготовка
    author = "Test Author"
    summary = "Test Summary"
    date = "2022-01-01"
    article_title = "Test Article Title"
    article_link = "https://example.com"

    # Выполнение
    db_handler.insert_summary(author, summary, date, article_title,
                              article_link)

    # Проверка
    conn = db_handler.create_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM summaries WHERE author=?', (author,))
    fetched_data = c.fetchone()

    assert fetched_data is not None
    assert fetched_data[1] == author
    assert fetched_data[2] == summary
    assert fetched_data[3] == date
    assert fetched_data[4] == article_title
    assert fetched_data[5] == article_link

    # Очистка
    c.execute('DELETE FROM summaries WHERE author=?', (author,))
    conn.commit()
    conn.close()
