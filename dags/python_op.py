from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from modules.aps.daily_extraction import aps_daily


default_args = {
    'owner': 'coder2j',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    default_args=default_args,
    dag_id='aps_daily',
    description='Aps daily',
    schedule_interval='@daily'

) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=aps_daily
    )
    task1