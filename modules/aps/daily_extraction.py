from common.db.config import db_config
from common.gcs_helper.gcs import GCS
import pandas as pd
from os import environ as env


class Operation:
    def __init__(self):
        self.cursor, self.conn = db_config(db=env['db'], user=env['user'], host=env['host'], password=env['pswd'])

    def retrieve_data(self):
        query = "select * from users"
        self.cursor.execute(query)
        res = self.cursor.fetchall()
        print(res)
        return res


def aps_daily():
    gcs_obj = GCS(bucket='aps_test')
    op_obj = Operation()
    try:
        print("job started")
        data = op_obj.retrieve_data()
        df = pd.DataFrame(data).apply(lambda x: ''.join(x) + '0', axis=1)
        gcs_obj.stream_push(df=df, key='APS/daily/12_jul_aps.txt')
        print("job completed")
    except Exception as er:
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print(f'{er}')
    finally:
        # op_obj.cursor.close()
        op_obj.conn.close()

