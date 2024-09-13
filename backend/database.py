import duckdb
from typing import Generator
import os

DATABASE_URL = "../dbt/grocery_mate.db"


def get_db() -> Generator:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, DATABASE_URL)
    db = duckdb.connect(db_path)
    try:
        yield db
    finally:
        db.close()
