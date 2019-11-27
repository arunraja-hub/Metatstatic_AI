"""Programatically interact with a Google Cloud Storage bucket."""
from os import path
from google.cloud import storage
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

def download_subdir(bucket_name, subdir, localdir):
    "Download a file to the backend"
    storage_client = storage.Client.from_service_account_json('narwhals/gcp_creds.json')
    bucket = storage_client.get_bucket(bucket_name)
    blobs =  bucket.list_blobs(prefix=subdir)  # Get list of files
    for blob in blobs:
        filename = blob.name.replace('/', '_') 
        blob.download_to_filename(localdir + filename)  # Download


