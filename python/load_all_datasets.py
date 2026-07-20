import os
from io import StringIO

import pandas as pd
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

# Load environment variables
load_dotenv()

connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

# Connect to Azure
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

container_client = blob_service_client.get_container_client("raw")

# Dictionary to store all DataFrames
datasets = {}

print("📂 Loading datasets from Azure...\n")

for blob in container_client.list_blobs():

    file_name = blob.name

    blob_client = container_client.get_blob_client(file_name)

    csv_data = blob_client.download_blob().readall().decode("utf-8")

    df = pd.read_csv(StringIO(csv_data))

    table_name = file_name.replace(".csv", "")

    datasets[table_name] = df

    print(f"✅ {table_name} loaded successfully -> Shape: {df.shape}")

print("\n🎉 Total datasets loaded:", len(datasets))
