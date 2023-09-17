# Задание 1
#
# - Создать базу данных для хранения информации о студентах университета
# - База данных должна содержать две таблицы: "Студенты" и "Факультеты"
# - В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, возраст, пол, группа и id факультета
# - В таблице "Факультеты" должны быть следующие поля: id и название факультета
# - Необходимо создать связь между таблицами "Студенты" и "Факультеты"
# - Написать функцию-обработчик, которая будет выводить список всех
# студентов с указанием их факультета.

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    group = db.Column(db.Integer, nullable=False)
    id_faculty = db.Column(db.Integer, db.ForeignKey('faculty.id'))

    def __repr__(self):
        return f'\nName: {self.firstname} {self.lastname}\nAge: {self.age}\nGroup: {self.group}\n'


class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    students = db.relationship('Student', backref='faculty', lazy=True)

    def __repr__(self):
        return f'Faculty: {self.name}\n'