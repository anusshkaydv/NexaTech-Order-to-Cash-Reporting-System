import pandas as pd
import pyodbc
from pathlib import Path

# ==========================================================
# Azure SQL Connection
# ==========================================================

SERVER = "nexatech-anushka-sql.database.windows.net"
DATABASE = "NexaTechERP"
USERNAME = ""
PASSWORD = ""

connection_string = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE};"
    f"UID={USERNAME};"
    f"PWD={PASSWORD};"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)

conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

# ==========================================================
# Raw Data Folder
# ==========================================================

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_FOLDER = BASE_DIR / "data" / "raw"

# ==========================================================
# Load Order
# ==========================================================

TABLES = {
    "regions.csv": "Regions",
    "payment_terms.csv": "Payment_Terms",
    "shipping_methods.csv": "Shipping_Methods",
    "product_categories.csv": "Product_Categories",
    "warehouses.csv": "Warehouses",
    "employees.csv": "Employees",
    "customers.csv": "Customers",
    "products.csv": "Products",
    "inventory.csv": "Inventory",
    "orders.csv": "Orders",
    "order_items.csv": "Order_Items",
    "shipments.csv": "Shipments",
    "invoices.csv": "Invoices",
    "payments.csv": "Payments",
    "returns.csv": "Returns",
    "discounts.csv": "Discounts"
}

# ==========================================================
# Identity Columns
# ==========================================================

IDENTITY_COLUMNS = {
    "Regions": "Region_ID",
    "Payment_Terms": "Payment_Term_ID",
    "Shipping_Methods": "Shipping_Method_ID",
    "Product_Categories": "Category_ID",
    "Warehouses": "Warehouse_ID",
    "Employees": "Employee_ID",
    "Customers": "Customer_ID",
    "Products": "Product_ID",
    "Inventory": "Inventory_ID",
    "Orders": "Order_ID",
    "Order_Items": "Order_Item_ID",
    "Shipments": "Shipment_ID",
    "Invoices": "Invoice_ID",
    "Payments": "Payment_ID",
    "Returns": "Return_ID",
    "Discounts": "Discount_ID"
}

print("=" * 60)
print("LOADING DATA INTO AZURE SQL")
print("=" * 60)

for file_name, table_name in TABLES.items():

    print(f"\nLoading {table_name}...")

    # ------------------------------------------
    # Skip table if already contains data
    # ------------------------------------------

    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    existing_rows = cursor.fetchone()[0]

    if existing_rows > 0:
        print(f"⏩ Skipped ({existing_rows} rows already exist)")
        continue

    # ------------------------------------------
    # Read CSV
    # ------------------------------------------

    file_path = DATA_FOLDER / file_name
    df = pd.read_csv(file_path)

    print(df.head())
    print(f"Rows in CSV: {len(df)}")

    # ------------------------------------------
    # Rename columns if required
    # ------------------------------------------

    if table_name == "Product_Categories":
        df.rename(
            columns={
                "Category_Description": "Description"
            },
            inplace=True
        )

    # ------------------------------------------
    # Remove columns that don't exist in SQL
    # ------------------------------------------

    if table_name == "Orders":
        df.drop(columns=["Is_Active"], errors="ignore", inplace=True)

    # ------------------------------------------
    # Remove Identity column
    # ------------------------------------------

    identity_column = IDENTITY_COLUMNS.get(table_name)

    if identity_column and identity_column in df.columns:
        df.drop(columns=[identity_column], inplace=True)

    # ------------------------------------------
    # Insert into SQL
    # ------------------------------------------

    columns = ",".join(df.columns)
    placeholders = ",".join(["?"] * len(df.columns))

    insert_query = f"""
    INSERT INTO {table_name}
    ({columns})
    VALUES ({placeholders})
    """

    cursor.fast_executemany = True
    cursor.executemany(insert_query, df.values.tolist())
    conn.commit()

    print(f"Inserted into {table_name}")
    print(f"✅ {len(df)} rows inserted")
cursor.close()
conn.close()

print("\n🎉 ALL DATA LOADED SUCCESSFULLY!")

