# Задание 5.
# Написать функцию, которая будет выводить на экран HTML-страницу
# с заголовком "Моя первая HTML страница" и абзацем "Привет, мир!"


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index')
def index():
    return render_template('index.html')


# Задание 6.
# Написать функцию, которая будет выводить на экран HTML страницу с таблицей, содержащей информацию о студентах
# Таблица должна содержать следующие поля:
#     - "Имя"
#     - "Фамилия"
#     - "Возраст"
#     - "Средний балл"
# Данные о студентах должны быть переданы в шаблон через контекст


@app.route('/students')
def students_info():
    box_head = {
        'name': 'Имя',
        'surname': 'Фамилия',
        'age': 'Возраст',
        'rating': 'Средний балл'
    }

    students = [
        {
            'name': 'Иван',
            'surname': 'Петров',
            'age': 17,
            'rating': 4
        },
        {
            'name': 'Семён',
            'surname': 'Васильев',
            'age': 18,
            'rating': 3
        },
        {
            'name': 'Николай',
            'surname': 'Иванов',
            'age': 28,
            'rating': 5
        },
    ]

    return render_template('students.html', **box_head, students=students)


if __name__ == '__main__':
    app.run(debug=True)
