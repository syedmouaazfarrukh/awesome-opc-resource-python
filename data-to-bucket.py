from google.cloud import storage

def upload_to_storage_bucket(project_id, service_account_key_path, bucket_name, file_path, destination_blob_name):
    """Upload a file to a GCP storage bucket using a service account.

    Args:
        project_id (str): Your GCP project ID.
        service_account_key_path (str): Path to the service account JSON key file.
        bucket_name (str): Name of the GCP storage bucket.
        file_path (str): Path to the local file to be uploaded.
        destination_blob_name (str): Name of the destination file in the storage bucket.

    Returns:
        str: The URL of the uploaded file.
    """
    client = storage.Client.from_service_account_json(service_account_key_path, project=project_id)
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(file_path)

    return f"gs://{bucket_name}/{destination_blob_name}"



if __name__ == '__main__':

    # Upload the data.json file to GCP storage bucket
    project_id = "your-project-id"
    service_account_key_path = "path/to/your/service/account/key.json"
    bucket_name = "your-bucket-name"
    file_path = "data.json"
    destination_blob_name = "data.json"

    url = upload_to_storage_bucket(project_id, service_account_key_path, bucket_name, file_path, destination_blob_name)
    print(f"File uploaded to: {url}")
