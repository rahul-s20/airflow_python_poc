import sys
import os
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from aps.modules.aps.daily_extraction import aps_daily
from aps.common.db_fetch.fetchd import fetch_data

default_args = {
    'owner': 'rahul',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

d = fetch_data()

with DAG(
        default_args=default_args,
        dag_id='aps_daily',
        description='Aps daily',
        start_date=datetime(2021, 1, 1),
        schedule_interval='@daily'

) as dag:

    task1 = PythonOperator(
        task_id='push-to-gcs-common-daily',
        python_callable=aps_daily,
        op_args=[d]
    )

    task2 = BashOperator(
        task_id='daily_transmission',
        bash_command="""
            ./daily_transmission.sh
            """,
        retries=3
    )
    task1 >> task2
