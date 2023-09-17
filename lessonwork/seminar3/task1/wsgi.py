# Задание 1
#
# - Создать базу данных для хранения информации о студентах университета
# - База данных должна содержать две таблицы: "Студенты" и "Факультеты"
# - В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, возраст, пол, группа и id факультета
# - В таблице "Факультеты" должны быть следующие поля: id и название факультета
# - Необходимо создать связь между таблицами "Студенты" и "Факультеты"
# - Написать функцию-обработчик, которая будет выводить список всех
# студентов с указанием их факультета.


from app import app

if __name__ == '__main__':
    app.run(debug=True)
