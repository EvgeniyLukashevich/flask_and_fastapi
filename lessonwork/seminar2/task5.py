from flask import Flask, render_template, request

app = Flask(__name__)

# Задание 5
# Создать страницу, на которой будет форма для ввода двух чисел и выбор операции
# (сложение, вычитание, умножение или деление) и кнопка "Вычислить".
# При нажатии на кнопку будет произведено вычисление результата
# выбранной операции и переход на страницу с результатом.


@app.route("/", methods=["GET", "POST"])
def calculator():
    if request.method == "POST":
        num1 = float(request.form.get("num1"))
        num2 = float(request.form.get("num2"))
        operation = request.form.get("operation")

        if operation == "addition":
            result = num1 + num2
            operation_name = "сложение"
        elif operation == "subtraction":
            result = num1 - num2
            operation_name = "вычитание"
        elif operation == "multiplication":
            result = num1 * num2
            operation_name = "умножение"
        elif operation == "division":
            if num2 == 0:
                return "Ошибка: деление на ноль!"
            result = num1 / num2
            operation_name = "деление"

        return render_template(
            "t5_result.html",
            num1=num1,
            num2=num2,
            operation_name=operation_name,
            result=result,
        )

    return render_template("t5_num_in.html")


if __name__ == "__main__":
    app.run()
