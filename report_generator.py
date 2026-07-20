import os
import pandas as pd


def generate_data_quality_report(datasets):

    report = []

    for name, df in datasets.items():

        report.append({
            "Dataset": name,
            "Rows": len(df),
            "Columns": len(df.columns),
            "Missing Values": int(df.isnull().sum().sum()),
            "Duplicate Rows": int(df.duplicated().sum())
        })

    report_df = pd.DataFrame(report)

    # Project Root Directory
    BASE_DIR = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..")
    )

    # Create docs/etl_reports folder
    REPORT_FOLDER = os.path.join(BASE_DIR, "docs", "etl_reports")
    os.makedirs(REPORT_FOLDER, exist_ok=True)

    # Report Path
    report_path = os.path.join(REPORT_FOLDER, "Data_Quality_Report.csv")

    # Save Report
    report_df.to_csv(report_path, index=False)

    print(f"\n📄 Data Quality Report Saved → {report_path}")