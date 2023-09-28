import sqlalchemy
import databases
from homework.seminar6.config import config
from datetime import datetime

DATABASE_URL = config.DATABASE_URL
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('firstname', sqlalchemy.String(32)),
    sqlalchemy.Column('lastname', sqlalchemy.String(32)),
    sqlalchemy.Column('email', sqlalchemy.String(64)),
    sqlalchemy.Column('password', sqlalchemy.String(64)),
    sqlalchemy.Column('isActive', sqlalchemy.Boolean, default=True)
)

items = sqlalchemy.Table(
    'items',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String(64)),
    sqlalchemy.Column('description', sqlalchemy.String(256)),
    sqlalchemy.Column('price', sqlalchemy.Float),
    sqlalchemy.Column('isActive', sqlalchemy.Boolean, default=True)
)

orders = sqlalchemy.Table(
    'orders',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('user_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id')),
    sqlalchemy.Column('item_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('items.id')),
    sqlalchemy.Column('order_date', sqlalchemy.DATETIME, default=datetime.utcnow()),
    sqlalchemy.Column('order_status', sqlalchemy.Boolean, default=False)
)



engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)
