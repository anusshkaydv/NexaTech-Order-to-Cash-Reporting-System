import os
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

# Load environment variables
load_dotenv()

# Azure Storage Connection String
CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

# Container Names
RAW_CONTAINER = "raw"
PROCESSED_CONTAINER = "processed"

# Blob Service Client
blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
