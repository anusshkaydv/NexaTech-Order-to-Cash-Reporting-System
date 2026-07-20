import os
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

# Load environment variables
load_dotenv()

# Get connection string
connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

# Connect to Azure Blob Storage
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

print("✅ Connected Successfully!")

# Access the raw container
container_client = blob_service_client.get_container_client("raw")

print("\n📂 Files inside 'raw' container:\n")

# List all blobs
for blob in container_client.list_blobs():
    print(blob.name)