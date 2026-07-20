import os
from io import StringIO

import pandas as pd
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

# Load .env
load_dotenv()

connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

blob_service_client = BlobServiceClient.from_connection_string(connection_string)

container_client = blob_service_client.get_container_client("raw")

print("Files in raw container:\n")

for blob in container_client.list_blobs():
    print(blob.name)

print("\nReading orders.csv...\n")

blob_client = container_client.get_blob_client("orders.csv")

csv_data = blob_client.download_blob().readall().decode("utf-8")

orders_df = pd.read_csv(StringIO(csv_data))

print("✅ orders.csv loaded successfully!")

print("\nShape:")
print(orders_df.shape)

print("\nFirst 5 Rows:")
print(orders_df.head())