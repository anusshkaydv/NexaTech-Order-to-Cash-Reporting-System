from io import StringIO
import pandas as pd

from config import blob_service_client, RAW_CONTAINER

def load_datasets():

    container_client = blob_service_client.get_container_client(RAW_CONTAINER)

    datasets = {}

    print("\n📂 Loading datasets from Azure Blob Storage...\n")

    for blob in container_client.list_blobs():

        blob_client = container_client.get_blob_client(blob.name)

        csv_data = blob_client.download_blob().readall().decode("utf-8")

        df = pd.read_csv(StringIO(csv_data))

        table_name = blob.name.replace(".csv", "")

        datasets[table_name] = df

        print(f"✅ {table_name:<20} {df.shape}")

    print("\n🎉 Total datasets loaded:", len(datasets))

    return datasets
