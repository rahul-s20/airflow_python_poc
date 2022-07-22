from airflow.providers.postgres.hooks.postgres import PostgresHook

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))


def fetch_data():
    query = 'select * from users'
    pg_hook = PostgresHook(postgres_conn_id='postgres_db', schema='test_airflow')
    conn = pg_hook.get_conn()
    curr = conn.cursor()
    curr.execute(query)
    data = curr.fetchall()
    # curr.close()
    # conn.close()
    return data
