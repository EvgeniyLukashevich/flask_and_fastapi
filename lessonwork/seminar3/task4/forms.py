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

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo


class RegistrationForm(FlaskForm):
    name = StringField('Логин', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    confirm_password = PasswordField('Подтвердите пароль', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Вступить в сообщество')