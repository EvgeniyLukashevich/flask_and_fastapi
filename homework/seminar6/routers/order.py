from fastapi import APIRouter
from homework.seminar6.database import database, orders
from homework.seminar6.models import Order, OrderIn
from typing import List

orders_router = APIRouter()


@orders_router.get('/orders/', response_model=List[Order])
async def read_orders():
    query = orders.select()
    return await database.fetch_all(query)


@orders_router.get('/orders/{order_id}', response_model=Order)
async def read_order(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    return await database.fetch_one(query)


@orders_router.post('/orders/', response_model=Order)
async def create_order(order: OrderIn):
    query = orders.insert().values(**dict(order))
    last_id = await database.execute(query)
    return {**dict(order), 'id': last_id}


@orders_router.put('/orders/{order_id}', response_model=Order)
async def update_order(order_id: int, updated_order: OrderIn):
    query = orders.update().where(orders.c.id == order_id).values(**dict(updated_order))
    await database.execute(query)
    return {**dict(updated_order), 'id': order_id}


@orders_router.delete('/orders/{order_id}', response_model=dict)
async def hard_del_order(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    await database.execute(query)
    return {'message': f'Item #{order_id} deleted.'}
