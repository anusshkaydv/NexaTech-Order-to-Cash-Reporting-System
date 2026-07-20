from io import BytesIO

from config import blob_service_client, PROCESSED_CONTAINER


def upload_datasets(datasets):

    print("\n" + "=" * 70)
    print("UPLOADING PROCESSED DATASETS")
    print("=" * 70)

    container_client = blob_service_client.get_container_client(PROCESSED_CONTAINER)

    for name, df in datasets.items():

        csv_buffer = BytesIO()

        df.to_csv(csv_buffer, index=False)

        csv_buffer.seek(0)

        blob_client = container_client.get_blob_client(f"{name}.csv")

        blob_client.upload_blob(csv_buffer, overwrite=True)

        print(f"✅ Uploaded: {name}.csv")

    print("\n🎉 All processed datasets uploaded successfully!")