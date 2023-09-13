from flask import Flask, render_template, request

app = Flask(__name__)

# Задание 4
# Создать страницу, на которой будет форма для ввода текста и кнопка "Отправить"
# При нажатии кнопки будет произведен подсчет количества слов в тексте
# и переход на страницу с результатом


def words_count(text: str) -> int:
    return len(text.split(" "))


@app.get("/")
def input_text():
    return render_template("t4_text_in.html")


@app.post("/")
def result():
    count = words_count(request.form.get("text"))
    return render_template("t4_result.html", count=count)


if __name__ == "__main__":
    app.run(debug=True)
