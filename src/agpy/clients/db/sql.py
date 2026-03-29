from sqlalchemy import Engine
from sqlmodel import create_engine
from agpy.clients.db.config import get_database_settings

def get_engine() -> Engine:
    global engine
    if engine is None:
        engine = create_engine(get_database_settings().url)
    return engine
engine: Engine | None = get_engine()