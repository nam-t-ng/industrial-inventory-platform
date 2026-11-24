import os
from contextlib import asynccontextmanager

import psycopg
from psycopg.rows import dict_row
from fastapi import FastAPI
from pydantic import BaseModel


def get_connection():
    return psycopg.connect(
        host=os.environ["DB_HOST"],
        dbname=os.environ["POSTGRES_DB"],
        user=os.environ["POSTGRES_USER"],
        password=os.environ["POSTGRES_PASSWORD"],
        row_factory=dict_row
    )


@asynccontextmanager
async def lifespan(app: FastAPI):
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS inventory (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                department VARCHAR(100) NOT NULL,
                quantity INTEGER NOT NULL
            )
        """)
    yield


app = FastAPI(lifespan=lifespan)


class InventoryItem(BaseModel):
    name: str
    department: str
    quantity: int

@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "environment": os.getenv("APP_ENV", "unknown")
    }

@app.get("/api/items")
def get_items():
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT * FROM inventory ORDER BY id"
        ).fetchall()

    return rows


@app.post("/api/items")
def create_item(item: InventoryItem):
    with get_connection() as conn:
        row = conn.execute(
            """
            INSERT INTO inventory (name, department, quantity)
            VALUES (%s, %s, %s)
            RETURNING *
            """,
            (item.name, item.department, item.quantity)
        ).fetchone()

    return row
