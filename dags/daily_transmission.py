import sys
import os
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'rahul',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}


with DAG(
        default_args=default_args,
        dag_id='daily_transmission',
        description='Aps transmission daily',
        start_date=datetime(2021, 1, 1),
        schedule_interval='@daily'

) as dag:

    task2 = BashOperator(
        task_id='daily_transmission',
        bash_command="""
        /aps/modules/transmission/daily_transmission.sh
        """,
        retries=3
    )
    task1