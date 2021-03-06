from aps.common.db.config import db_config
from aps.common.gcs_helper.gcs import GCS
import pandas as pd
from os import environ as env
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))


class Operation:
    def __init__(self):
        self.cursor, self.conn = db_config(db=env['db'], user=env['user'], host=env['host'], password=env['pswd'])

    def retrieve_data(self):
        query = "select * from users"
        self.cursor.execute(query)
        res = self.cursor.fetchall()
        print(res)
        return res


def aps_daily(d):
    gcs_obj = GCS(bucket='aps_test')
    # op_obj = Operation()
    try:
        print("job started")
        # data = op_obj.retrieve_data()
        df = pd.DataFrame(d).apply(lambda x: ''.join(x) + '0', axis=1)
        gcs_obj.stream_push(df=df, key='APS/daily/12_jul_aps.txt')
        print("job completed")
    except Exception as er:
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print(f'{er}')
    finally:
        # op_obj.cursor.close()
        # op_obj.conn.close()
        print("job completed done")
