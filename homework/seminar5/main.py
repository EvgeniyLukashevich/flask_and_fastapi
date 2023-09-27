import uvicorn
from fastapi import FastAPI, Request, Form
from pydantic import BaseModel
import logging
from typing import Optional
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from random import randint as ri, choice as rch

app = FastAPI()
templates = Jinja2Templates(directory='./templates')
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class User(BaseModel):
    id: int
    name: str
    email: Optional[str] = None
    password: str
    isActive: bool


class UserIn(BaseModel):
    name: str
    email: Optional[str] = None
    password: str
    isActive: bool


welcome_message = 'Seminar 5. Homework'

users = []

firstnames = [
    'Эван', "Иван", "Эмма", "Мари", "Стюарт", "Филлип",
    'Кейт', "Джон", "Джулия", "Деннис", "Маркус", "Ариана",
    'Энн', "Мэри", "Кейтлин", "Софи", "Николас", "Роберт"
]
lastnames = [
    'Уилсон', 'Тюрам', 'Дюма', 'Эрнандес', 'Уайт', 'Гонсалес',
    'Рамси', 'Шакири', 'Джеррард', 'Терри', 'Руни', 'МакКолмак',
    'Балотелли', 'Игуаин', 'Лам', 'Алаба', 'Марсьяль', 'Гейтс'
]

for i in range(ri(5, 15)):
    user_id: int
    if len(users) != 0:
        user_id = len(users) + 1
    else:
        user_id = 1

    if ri(0, 3):
        user = User(
            id=user_id,
            name=f'{rch(firstnames)} {rch(lastnames)}',
            email=f'user{user_id}@gmail.com',
            password=f'{user_id}passwd{user_id}',
            isActive=True
        )
    else:
        user = User(
            id=user_id,
            name=f'{rch(firstnames)} {rch(lastnames)}',
            password=f'{user_id}passwd{user_id}',
            isActive=True
        )
    users.append(user)


@app.get('/', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request, 'welcome_message': welcome_message})


@app.get('/users/', response_class=HTMLResponse)
def show_users(request: Request):
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})


@app.post('/users/', response_class=HTMLResponse)
async def del_user(request: Request, user_id: int = Form(...)):
    for user in users:
        if user.id == user_id:
            user.isActive = False
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})


@app.get('/user_add/', response_class=HTMLResponse)
def reg_form(request: Request):
    return templates.TemplateResponse('user_add.html', {'request': request})


@app.post('/user_add/', response_class=HTMLResponse)
async def reg_form(request: Request):
    data = await request.form()
    users.append(User(
        id=users[-1].id + 1,
        name=data.get('name'),
        email=data.get('email'),
        password=data.get('password'),
        isActive=True))
    return RedirectResponse("/users/", status_code=303)


if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)
