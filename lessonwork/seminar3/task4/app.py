# Задание 4
#
# - Создайте форму регистрации пользователя с использованием Flask-WTF. Форма должна содержать следующие поля:
#     - Имя пользователя (обязательное поле)
#     - Электронная почта (обязательное поле, с валидацией на корректность ввода email)
#     - Пароль (обязательное поле, с валидацией на минимальную длину пароля)
#     - Подтверждение пароля (обязательное поле, с валидацией на совпадение с паролем)
# - После отправки формы данные должны сохраняться в базе данных (можно использовать SQLite)
# и выводиться сообщение об успешной регистрации. Если какое-то из обязательных полей не заполнено
# или данные не прошли валидацию, то должно выводиться соответствующее сообщение об ошибке
# - Дополнительно: добавьте проверку на уникальность имени пользователя и электронной почты в базе данных.
# Если такой пользователь уже зарегистрирован, то должно выводиться сообщение об ошибке


from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash
from models import db, User
from forms import RegistrationForm

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///task4_database.db"
app.config["SECRET_KEY"] = '89f55340debe60e532e776da81276edfb0592d5a3bed02409dceedfdc07c4bd9'
db.init_app(app)

message = 'Будьте так любезны, зарегистрируйтесь'

@app.cli.command("db-init")
def db_init():
    db.create_all()


@app.get('/')
def index():
    global message
    return render_template('index.html', message=message)


@app.route('/registration/', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()

    if request.method == 'POST' and form.validate_on_submit():
        error = ''
        existing_user = User.query.filter_by(name=form.name.data).first()
        if existing_user:
            error = 'Пользователь с таким именем уже зарегистрирован'
            return render_template('registration.html', name_error=error, form=form)

        existing_email = User.query.filter_by(email=form.email.data).first()
        if existing_email:
            error = 'Пользователь с такой электронной почтой уже зарегистрирован'
            return render_template('registration.html', email_error=error, form=form)

        hashed_password = generate_password_hash(form.password.data)
        user = User(
            name=form.name.data,
            email=form.email.data,
            password=hashed_password,
        )
        db.session.add(user)
        db.session.commit()
        global message
        message = 'Вы зарегистрированы!'
        return redirect(url_for('index', message=message))
    else:
        return render_template('registration.html', form=form)


@app.route('/userlist/')
def users():
    user_list = User.query.all()
    return render_template('user_list.html', user_list=user_list)
