from flask import Flask, render_template
from random import choice as rch

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/pants/')
def pants():
    words1 = ['Классные', "Крутые", "Модные", "Стильные", "Лучшие"]
    words2 = ['брюки', 'шорты','джинсы','бриджи', 'ласины']
    pants = [f"{rch(words1)} {rch(words2)}" for _ in range(6)]
    return render_template('pants.html', pants=pants)


@app.route('/shoes/')
def shoes():
    words1 = ['Классные', "Крутые", "Модные", "Стильные", "Лучшие"]
    words2 = ['кроссы', 'кеды', 'туфли', 'тапки', 'тяги']
    shoes = [f"{rch(words1)} {rch(words2)}" for _ in range(6)]
    return render_template('shoes.html', shoes=shoes)


@app.route('/other/')
def other():
    words1 = ['Классная', "Крутая", "Модная", "Стильная", "Лучшая"]
    words2 = ['куртка', "парка", 'шляпка', 'блузка', 'тишка']
    other = [f"{rch(words1)} {rch(words2)}" for _ in range(6)]
    return render_template('other.html', other=other)


if __name__ == '__main__':
    app.run(debug=True)
