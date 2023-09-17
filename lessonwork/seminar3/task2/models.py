# Задание 2
#
# - Создать базу данных для хранения информации о книгах в библиотеке
# - База данных должна содержать две таблицы: "Книги" и "Авторы"
# - В таблице "Книги" должны быть следующие поля: id, название, год издания, количество экземпляров и id автора
# - В таблице "Авторы" должны быть следующие поля: id, имя и фамилия
# - Необходимо создать связь между таблицами "Книги" и "Авторы"
# - Написать функцию-обработчик, которая будет выводить список всех книг с указанием их авторов
from datetime import datetime
from random import randint
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    year = db.Column(db.Integer, nullable=False, default=datetime.now().year)
    quantity = db.Column(db.Integer, nullable=False, default=10)
    id_author = db.Column(db.Integer, db.ForeignKey('author.id'))


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    books = db.relationship('Book', backref='author', lazy=True)
