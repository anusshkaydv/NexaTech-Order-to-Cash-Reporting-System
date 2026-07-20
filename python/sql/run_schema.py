import pyodbc
from pathlib import Path

# -----------------------------
# Azure SQL Connection
# -----------------------------
server = "nexatech-anushka-sql.database.windows.net"
database = "NexaTechERP"
username = "nexatechadmin"
password = "Qwertyuiop@123"

connection_string = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password};"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)

conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

# -----------------------------
# Folder containing SQL scripts
# -----------------------------
sql_folder = Path("sql/oltp")

# Skip these files
skip_files = {
    "01_create_database.sql",
    "02_use_database.sql"
}

# Execute scripts in order
for sql_file in sorted(sql_folder.glob("*.sql")):

    if sql_file.name in skip_files:
        print(f"⏭ Skipped {sql_file.name}")
        continue

    print(f"▶ Executing {sql_file.name}")

    with open(sql_file, "r", encoding="utf-8") as f:
        sql = f.read()

    # Remove unsupported statements
    sql = sql.replace("USE NexaTechERP;", "")
    sql = sql.replace("GO", "")

    try:
        cursor.execute(sql)
        conn.commit()
        print(f"✅ {sql_file.name} completed")

    except Exception as e:
        print(f"❌ Error in {sql_file.name}")
        print(e)

cursor.close()
conn.close()

print("\n🎉 Schema created successfully!")

import pandas as pd

df = pd.read_csv("data/raw/inventory.csv")

print(df.head())

print(df["Product_ID"].min())
print(df["Product_ID"].max())
