import psycopg2 as pg
import psycopg2

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))


def db_config(db: str, user: str, host: str, password: str, port: str = '5432'):
    try:
        conn = pg.connect(database=db, user=user, password=password, host=host, port=port, connect_timeout=5)
        conn.autocommit = True
        cursor = conn.cursor()
        print("connected")
        return cursor, conn
    except Exception as er:
        print("db err")
        print(f'{er}')
