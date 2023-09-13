from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "reg3434g34g435h45h"


# Задание 8
# Создать страницу, на которой будет форма для ввода имени и кнопка "Отправить".
# При нажатии на кнопку будет произведено перенаправление на страницу с flash
# сообщением, где будет выведено "Привет, {имя}!"


@app.route("/", methods=["GET", "POST"])
def name_input():
    if request.method == "POST":
        name = request.form.get("name")
        flash(f"Привет, {name}", "success")
        return redirect(url_for("name_input"))
    return render_template("t8_name_in.html")




if __name__ == "__main__":
    app.run(debug=True)
