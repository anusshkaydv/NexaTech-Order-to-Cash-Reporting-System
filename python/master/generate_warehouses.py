import pandas as pd
from datetime import date

warehouses = [
    [1, "WH-NR-001", "Delhi Central Warehouse", 1, "Delhi", 1, date.today()],
    [2, "WH-SR-001", "Bengaluru Warehouse", 2, "Bengaluru", 1, date.today()],
    [3, "WH-ER-001", "Kolkata Warehouse", 3, "Kolkata", 1, date.today()],
    [4, "WH-WR-001", "Mumbai Warehouse", 4, "Mumbai", 1, date.today()],
    [5, "WH-CR-001", "Nagpur Warehouse", 5, "Nagpur", 1, date.today()]
]

columns = [
    "Warehouse_ID",
    "Warehouse_Code",
    "Warehouse_Name",
    "Region_ID",
    "City",
    "Is_Active",
    "Created_Date"
]

df = pd.DataFrame(warehouses, columns=columns)

df.to_csv("data/raw/warehouses.csv", index=False)

print(df)
print("\n✅ warehouses.csv created successfully!")
