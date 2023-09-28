from fastapi import APIRouter
from homework.seminar6.database import database, users
from homework.seminar6.models import User, UserIn
from typing import List

users_router = APIRouter()


@users_router.get('/users/', response_model=List[User])
async def read_users():
    query = users.select().where(users.c.isActive)
    return await database.fetch_all(query)


@users_router.get('/users/{user_id}', response_model=User)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


@users_router.post('/users/', response_model=User)
async def create_user(user: UserIn):
    query = users.insert().values(**dict(user))
    last_id = await database.execute(query)
    return {**dict(user), 'id': last_id}


@users_router.put('/users/{user_id}', response_model=User)
async def update_user(user_id: int, updated_user: UserIn):
    query = users.update().where(users.c.id == user_id).values(**dict(updated_user))
    await database.execute(query)
    return {**dict(updated_user), 'id': user_id}


@users_router.delete('/users/{user_id}', response_model=dict)
async def hard_del_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': f'User #{user_id} deleted.'}
