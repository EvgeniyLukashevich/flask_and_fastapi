# Задание 2
#
# - Создать базу данных для хранения информации о книгах в библиотеке
# - База данных должна содержать две таблицы: "Книги" и "Авторы"
# - В таблице "Книги" должны быть следующие поля: id, название, год издания, количество экземпляров и id автора
# - В таблице "Авторы" должны быть следующие поля: id, имя и фамилия
# - Необходимо создать связь между таблицами "Книги" и "Авторы"
# - Написать функцию-обработчик, которая будет выводить список всех книг с указанием их авторов

from flask import Flask, render_template
from models import db, Book, Author
from random import randint, choice
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///university.db"
db.init_app(app)

firstnames = [
    'Эван', "Иван", "Эмма", "Мари", "Стюарт", "Филлип",
    'Кейт', "Джон", "Джулия", "Деннис", "Маркус", "Ариана",
    'Энн', "Мэри", "Кейтлин", "Софи", "Николас", "Роберт"
]
lastnames = [
    'Уилсон', 'Тюрам', 'Дюма', 'Эрнандес', 'Уайт', 'Гонсалес',
    'Рамси', 'Шакири', 'Джеррард', 'Терри', 'Руни', 'МакКолмак',
    'Балотелли', 'Игуаин', 'Лам', 'Алаба', 'Марсьяль', 'Гейтс'
]
booknames = [
    'Пропавшие', "Потерянный остров", "На краю", "Любовь в терновнике", "Унесенные варваром",
    "Жидкий мост", "Семь дней", "Лазеры", "Сухой пергамент", "Лабиринт", "Кристалл из бездны",
    "Лишний шум", "Герой из магния", "Пол это лава", "Любовная трапеция", "Королева-лягушка",
    "Разборки в Шанхае", "Горный перевал", "Летят дятлы", "Рецепты казинаков", "Синяя река"
]

min_year = 1950
max_year = datetime.now().year

min_quantity = 1
max_quantity = 100


@app.cli.command('db-init')
def init_db():
    db.create_all()


@app.cli.command('db-fill')
def fill_db():
    for book_name in booknames:
        author = Author(firstname=choice(firstnames), lastname=choice(lastnames))
        db.session.add(author)
        db.session.commit()
        book = Book(
            name=book_name,
            year=randint(min_year,max_year),
            quantity=randint(min_quantity,max_quantity),
            id_author=author.id,
        )
        db.session.add(book)
    db.session.commit()

@app.get('/')
def start():
    return render_template('index.html')


@app.get('/library/')
def show_students():
    books = Book.query.all()
    return render_template('library.html', books=books)


