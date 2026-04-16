from azure.storage.blob import BlobServiceClient
from django.conf import settings

def upload_file_to_azure(file):
    blob_service_client = BlobServiceClient.from_connection_string(
        settings.AZURE_CONNECTION_STRING
    )

    blob_client = blob_service_client.get_blob_client(
        container=settings.AZURE_CONTAINER,
        blob=file.name
    )

    blob_client.upload_blob(file, overwrite=True)

    return blob_client.url