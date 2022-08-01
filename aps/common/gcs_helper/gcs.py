from google.cloud import storage
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))


class GCS:
    def __init__(self, bucket: str):
        self.gcs_client = storage.Client()
        self.bucket = self.gcs_client.bucket(bucket)

    def stream_push(self, df, key: str, header=None, sep: str = ","):
        buffer = self.bucket.blob(key)
        buffer.upload_from_string(df.to_csv(header=header, index=None, sep=sep), 'text')
