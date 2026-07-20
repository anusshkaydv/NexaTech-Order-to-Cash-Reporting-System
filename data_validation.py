import os
from io import StringIO

import pandas as pd
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

# ----------------------------
# Load Azure Connection
# ----------------------------

load_dotenv()

connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

blob_service_client = BlobServiceClient.from_connection_string(connection_string)

container_client = blob_service_client.get_container_client("raw")

datasets = {}

# ----------------------------
# Load all datasets
# ----------------------------

for blob in container_client.list_blobs():

    blob_client = container_client.get_blob_client(blob.name)

    csv_data = blob_client.download_blob().readall().decode("utf-8")

    datasets[blob.name.replace(".csv", "")] = pd.read_csv(StringIO(csv_data))

# ----------------------------
# Data Validation Report
# ----------------------------

print("=" * 70)
print("DATA VALIDATION REPORT")
print("=" * 70)

for name, df in datasets.items():

    print(f"\n{name.upper()}")

    print("-" * 50)

    print(f"Rows               : {df.shape[0]}")

    print(f"Columns            : {df.shape[1]}")

    print(f"Missing Values     : {df.isnull().sum().sum()}")

    print(f"Duplicate Rows     : {df.duplicated().sum()}")