from fastapi import APIRouter
from homework.seminar6.database import database, users, items, orders
from random import randint, choice
from datetime import datetime

fill_db_router = APIRouter()

firstnames = [
    'Avon', "Ivan", "Emma", "Mary", "Stuart", "Philipp",
    'Kate', "John", "Julia", "Dennis", "Markus", "Ariana",
    'Ann', "Maria", "Christy", "Sofia", "Nickolas", "Robert"
]
lastnames = [
    'Wilson', 'Thuram', 'Duma', 'Hernandes', 'White', 'Gonzales',
    'Ramsey', 'Shakiri', 'Gerrard', 'Terry', 'Rooney', 'McKolmack',
    'Ballotelli', 'Iguain', 'Lahm', 'Alaba', 'Martial', 'Gates'
]


@fill_db_router.get('/fill/{quantity}')
async def fill_database(quantity: int):
    for i in range(quantity):
        firstname = choice(firstnames)
        lastname = choice(lastnames)
        users_query = users.insert().values(
            firstname=firstname,
            lastname=lastname,
            email=f'{firstname.lower()}{lastname.lower()}@gmail.com',
            password=f'{i + 1}{lastname}{i + 1}',
            isActive=True
        )
        items_query = items.insert().values(
            name=f'ITEM #{i + 1}',
            description=f'Описание товара №{i + 1}',
            price=randint(100, 100000),
            isActive=True
        )
        await database.execute(users_query)
        await database.execute(items_query)
    return {'message': 'Database filled'}
