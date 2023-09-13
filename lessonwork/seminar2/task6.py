from flask import Flask, render_template, request

app = Flask(__name__)

# Задание 6
# Создать страницу, на которой будет форма для ввода имени
# и возраста пользователя и кнопка "Отправить".
# При нажатии на кнопку будет произведена проверка возраста и переход
# на страницу с результатом или на страницу с ошибкой в случае некорректного возраста.


__MAGICWORD = "Астралябия"


@app.route("/", methods=["GET", "POST"])
def age_check():

    if request.method == "POST":
        name = request.form.get("name")
        age = int(request.form.get("age"))
        
        if age >= 18:
            text = f"""Поздравляю, {name}!
            Тебе {age} и ты готов(-а) узнать секрет.
            Стоп-слово: {__MAGICWORD}"""
        else:
            text = f"""{name}!
            Тебе всего {age}...
            Ты не готов(-а) узнать стоп-слово!"""
        return render_template("t6_access.html", text=text)
    
    return render_template("t6_age_in.html")


if __name__ == "__main__":
    app.run()
