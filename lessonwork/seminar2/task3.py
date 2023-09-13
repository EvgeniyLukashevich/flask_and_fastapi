from flask import Flask, render_template, request


app = Flask(__name__)


# Задание 3
# Создать страницу, на которой будет форма для ввода логина и пароля
# При нажатии на кнопку "Отправить" будет произведена проверка соответствия
# логина и пароля и переход на страницу приветствия пользователя или страницу с ошибкой


__LOGIN = "Admin"
__PSWD = "qwerty"


@app.get("/")
def log_in():
    return render_template("t3_login.html")


@app.post("/")
def check():
    if __LOGIN == request.form.get("login") and __PSWD == request.form.get("pswd"):
        return render_template("t1_welcome.html", name=__LOGIN)
    else:
        return render_template("t3_error.html")


if __name__ == "__main__":
    app.run(debug=True)
