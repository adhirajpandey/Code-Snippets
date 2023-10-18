from google.cloud import storage
import os
from dotenv import load_dotenv


# Load variables from .env
load_dotenv()

# Set the bucket config
bucket_name = os.getenv("GCS_BUCKET_NAME")
credentials_file = os.getenv("GCS_CREDENTIALS_FILE")


# Useful Functions
def upload_to_bucket(bucket_name, source_file_path, destination_blob_name):
    storage_client = storage.Client.from_service_account_json(credentials_file)

    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_path)
    
    print("File {} uploaded to {}.".format(source_file_path, destination_blob_name))


def download_from_bucket(bucket_name, source_file_path, destination_filename):
    storage_client = storage.Client.from_service_account_json(credentials_file)

    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(source_file_path)
    blob.download_to_filename(destination_filename)

    print("File {} downloaded to {}.".format(source_file_path, destination_filename))


def list_all_bucket_files(bucket_name):
    storage_client = storage.Client.from_service_account_json(credentials_file)

    bucket = storage_client.bucket(bucket_name)

    blobs = bucket.list_blobs()

    for file in blobs:
        print(str(file))


def delete_all_bucket_files(bucket_name):
    storage_client = storage.Client.from_service_account_json(credentials_file)

    bucket = storage_client.bucket(bucket_name)

    blobs = bucket.list_blobs()

    for blob in blobs:
        blob.delete()
        print("Deleted {}".format(blob.name))





