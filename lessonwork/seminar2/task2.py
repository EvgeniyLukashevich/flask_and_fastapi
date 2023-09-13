from pathlib import PurePath, Path
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)


# Задание 2
# Создать страницу, на которой будет изображение и ссылка на другую страницу,
# на которой будет отображаться форма для загрузки изображений

picture_path = "../static/img/t2_upload/"
picture_name = "default.jpg"


@app.route("/")
def picture_view():
    global picture_name
    global picture_path
    return render_template(
        "t2_base.html", picture_name=picture_name, picture_path=picture_path
    )


@app.route("/upload/", methods=["GET", "POST"])
def picture_upload():
    global picture_name
    global picture_path
    if request.method == "POST":
        picture = request.files.get("image")
        picture_name = secure_filename(picture.filename)
        picture.save(
            PurePath.joinpath(
                Path.cwd(), "lessonwork/seminar2/static/img/t2_upload", picture_name
            )
        )
        return render_template(
            "t2_base.html", picture_name=picture_name, picture_path=picture_path
        )
    else:
        return render_template("t2_upload.html")


if __name__ == "__main__":
    app.run(debug=True)
