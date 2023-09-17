# Задание 1
#
# - Создать базу данных для хранения информации о студентах университета
# - База данных должна содержать две таблицы: "Студенты" и "Факультеты"
# - В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, возраст, пол, группа и id факультета
# - В таблице "Факультеты" должны быть следующие поля: id и название факультета
# - Необходимо создать связь между таблицами "Студенты" и "Факультеты"
# - Написать функцию-обработчик, которая будет выводить список всех
# студентов с указанием их факультета.


from flask import Flask, render_template
from models import db, Student, Faculty
from random import randint, choice

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///university.db"
db.init_app(app)

firstnames = ['Иван', "Василий", "Петр", "Мария", "Дарья", "София"]
lastnames = ['Неценко', 'Захарчук', 'Видич', 'Кравченко', 'Литвинец', 'Матич']
faculties = ['Тестирование', "Управление", "Дизайн", "Фотография"]


@app.cli.command('init-db')
def init_db():
    db.create_all()
    for faculty_name in faculties:
        faculty = Faculty(name=faculty_name)
        db.session.add(faculty)
        db.session.commit()
        print(f'\n### Факультет записан в БД ###\nid: {faculty.id}\nname: {faculty.name}\n')


@app.cli.command('fill-db')
def fill_db():
    id = 1
    while True:
        if Faculty.query.get(id) == None:
            break
        else:
            for i in range(5):
                student = Student(
                    firstname=choice(firstnames),
                    lastname=choice(lastnames),
                    age=randint(18, 25),
                    gender=choice(['m', 'f']),
                    group=randint(1, 2),
                    id_faculty=id
                )
                db.session.add(student)
            id += 1
        db.session.commit()


@app.get('/')
def start():
    return render_template('index.html')


@app.get('/students/')
def show_students():
    faculties = Faculty.query.all()
    return render_template('library.html', faculties=faculties)



if __name__ == '__main__':
    app.run()
