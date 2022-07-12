from google.cloud import storage


class GCS:
    def __init__(self, bucket: str):
        self.gcs_client = storage.Client()
        self.bucket = self.gcs_client.bucket(bucket)

    def stream_push(self, df, key: str, header=None, sep: str = ","):
        buffer = self.bucket.blob(key)
        buffer.upload_from_string(df.to_csv(header=header, index=None, sep=sep), 'text')