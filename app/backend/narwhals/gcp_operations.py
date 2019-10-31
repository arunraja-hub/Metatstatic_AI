"""Programatically interact with a Google Cloud Storage bucket."""
from os import path
from google.cloud import storage
from config import bucketName, bucketFolder
import sys


def upload_file(bucket_name, source_file):
    """Uploads a file to the bucket."""
    storage_client = storage.Client.from_service_account_json(
        'gcp_creds.json')
    bucket = storage_client.get_bucket('narwhals')
    file_name = path.basename(source_file)
    blob = bucket.blob('test/' + file_name)

    blob.upload_from_filename(source_file)

    print('File {} uploaded to {}.'.format(
        file_name,
        'narwhals'))

if __name__ == "__main__":
    first_arg = sys.argv[1]
    second_arg = sys.argv[2]
    upload_file(first_arg, second_arg)

