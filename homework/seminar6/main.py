from fastapi import FastAPI
import uvicorn
from database import database
from routers import users_router, items_router, orders_router, fill_db_router

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(users_router, tags=['Users'])
app.include_router(items_router, tags=['Items'])
app.include_router(orders_router, tags=['Orders'])
app.include_router(fill_db_router)

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
