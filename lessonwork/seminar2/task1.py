from flask import Flask, render_template, request

app = Flask(__name__)

# Задание 1
# Создать страницу, на которой будет кнопка "Нажми меня"
# при нажатии на которую будет переход на другую страницу
# с приветствием пользователя по имени


@app.get("/")
def pushme():
    context = {
        "title": "PushMe Page",
        "button_text": "Нажми меня",
        "placeholder": "Введите ваше имя",
    }
    return render_template("t1_pushme.html", **context)


@app.post("/welcome")
def pushme_post():
    name = request.form.get("name")
    if name == "":
        name = "Незнакомец"
    return render_template("t1_welcome.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)
