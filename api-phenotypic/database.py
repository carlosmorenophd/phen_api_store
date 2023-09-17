import os
from peewee import _ConnectionState, MySQLDatabase
from dotenv import load_dotenv
from contextvars import ContextVar

load_dotenv()
DATABASE_NAME = os.getenv('DB_SCHEMA')
db_state_default = {"closed": None, "conn": None, "ctx": None, "transactions": None}
db_state = ContextVar("db_state", default=db_state_default.copy())


class PeeweeConnectionState(_ConnectionState):
    def __init__(self, **kwargs):
        super().__setattr__("_state", db_state)
        super().__init__(**kwargs)

    def __setattr__(self, name, value):
        self._state.get()[name] = value

    def __getattr__(self, name):
        return self._state.get()[name]


db = MySQLDatabase(DATABASE_NAME, host=os.getenv("DB_HOST"), port=os.getenv('DB_PORT'), user=os.getenv('DB_USER'), password=os.getenv('DB_PASS'))

db._state = PeeweeConnectionState()
