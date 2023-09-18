from contextvars import ContextVar
from os import getenv

from dotenv import load_dotenv
from peewee import MySQLDatabase, _ConnectionState

load_dotenv()
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


db = MySQLDatabase(
    getenv("DB_SCHEMA"),
    host=getenv("DB_HOST"),
    password=getenv("DB_PASS"),
    port=int(getenv("DB_PORT")),
    user=getenv("DB_USER"),
)

db._state = PeeweeConnectionState()
