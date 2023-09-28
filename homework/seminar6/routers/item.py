from fastapi import APIRouter
from homework.seminar6.database import database, items
from homework.seminar6.models import Item, ItemIn
from typing import List

items_router = APIRouter()


@items_router.get('/items/', response_model=List[Item])
async def read_items():
    query = items.select().where(items.c.isActive)
    return await database.fetch_all(query)


@items_router.get('/items/{item_id}', response_model=Item)
async def read_item(item_id: int):
    query = items.select().where(items.c.id == item_id)
    return await database.fetch_one(query)


@items_router.post('/items/', response_model=Item)
async def create_item(item: ItemIn):
    query = items.insert().values(**dict(item))
    last_id = await database.execute(query)
    return {**dict(item), 'id': last_id}


@items_router.put('/items/{item_id}', response_model=Item)
async def update_item(item_id: int, updated_item: ItemIn):
    query = items.update().where(items.c.id == item_id).values(**dict(updated_item))
    await database.execute(query)
    return {**dict(updated_item), 'id': item_id}


@items_router.delete('/items/{item_id}', response_model=dict)
async def hard_del_item(item_id: int):
    query = items.delete().where(items.c.id == item_id)
    await database.execute(query)
    return {'message': f'Item #{item_id} deleted.'}
