import os
from datetime import datetime

# Get project root directory
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# Create docs/etl_reports path
LOG_FOLDER = os.path.join(BASE_DIR, "docs", "etl_reports")

LOG_FILE = os.path.join(LOG_FOLDER, "ETL_Log.txt")


def write_log(message):

    os.makedirs(LOG_FOLDER, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {message}\n")