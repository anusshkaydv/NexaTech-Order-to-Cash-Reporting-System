from loader import load_datasets
from validator import validate_datasets
from transformer import transform_datasets
from uploader import upload_datasets
from report_generator import generate_data_quality_report
from logger import write_log


def main():

    write_log("========== ETL Pipeline Started ==========")

    # Step 1 - Load
    datasets = load_datasets()
    write_log(f"Loaded {len(datasets)} datasets from Azure Blob Storage.")

    # Step 2 - Validate
    validate_datasets(datasets)
    write_log("Data validation completed successfully.")

    # Step 3 - Transform
    transformed = transform_datasets(datasets)
    write_log("Data transformation completed successfully.")

    # Step 4 - Upload
    upload_datasets(transformed)
    write_log("Processed datasets uploaded to Azure Blob Storage.")

    # Step 5 - Generate Report
    generate_data_quality_report(transformed)
    write_log("Data Quality Report generated.")

    write_log("========== ETL Pipeline Completed Successfully ==========\n")

    print("\n" + "=" * 70)
    print("NEXATECH ETL PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 70)


if __name__ == "__main__":
    main()