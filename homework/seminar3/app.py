from flask import Flask, render_template, redirect, url_for, request
from werkzeug.security import generate_password_hash
from flask_wtf.csrf import CSRFProtect
from models import db, User
from forms import RegistrationForm

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///my_db.db"
app.config[
    "SECRET_KEY"
] = "89f55340debe60e532e776da81276edfb0592d5a3bed02409dceedfdc07c4bd9"
csrf = CSRFProtect(app)
db.init_app(app)


@app.route("/", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if request.method == "POST" and form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        new_user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            password=hashed_password,
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("success"))
    return render_template("register.html", form=form)


@app.route("/success")
def success():
    return "Регистрация прошла успешно!"


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    print("Db connected")
    app.run(debug=True)
