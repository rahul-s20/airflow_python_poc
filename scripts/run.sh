#!/bin/bash

cd D:/Projects/airflow_poc

export db='test_airflow'
export user='postgres'
export host='35.222.254.172'
export pswd='123456789'
export GOOGLE_APPLICATION_CREDENTIALS='data/feisty-album-354905-906697a6b545.json'

python -c 'from modules.aps.daily_extraction import aps_daily; aps_daily()'
