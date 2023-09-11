# Задание 1.
# Напишите простое веб-приложение на Flask, которое будет
# выводить на экран текст "Hello, World!"

from flask import Flask

app = Flask(__name__)


@app.route('/')
def welcome():
    return 'Hello, World'


# Задание 2.
# Дорабатываем задачу 1:
# Добавьте две дополнительные страницы в ваше веб-приложение:
# страницу "about"
# страницу "contact"

@app.route('/about/')
def about():
    return 'Надо бы написать что-то обо мне, но я ещё не придумал что.'


@app.route('/contact/')
def contact():
    return 'Третий дом по левой стороне улицы Сезам'


# Задание 3.
# Написать функцию, которая будет принимать на вход два
# числа и выводить на экран их сумму


@app.route('/<int:num1>+<int:num2>/')
def my_sum(num1: int, num2: int) -> str:
    return str(f"{num1 + num2}")


# Задание 4.
# Написать функцию, которая будет принимать на вход строку и выводить на экран ее длину

@app.route('/length/<string:text>')
def string_length(text: str):
    return str(len(text))


if __name__ == '__main__':
    app.run(debug=True)
