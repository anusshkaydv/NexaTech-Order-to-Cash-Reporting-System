import pandas as pd
import random
from datetime import date

# ---------------------------------
# Read Master Data
# ---------------------------------

products = pd.read_csv("data/raw/products.csv")
warehouses = pd.read_csv("data/raw/warehouses.csv")

inventory = []

inventory_id = 1

# ---------------------------------
# Generate Inventory
# ---------------------------------

for _, warehouse in warehouses.iterrows():

    for _, product in products.iterrows():

        quantity = random.randint(10, 500)

        reorder_level = random.randint(10, 50)

        inventory.append([
            inventory_id,
            warehouse["Warehouse_ID"],
            product["Product_ID"],
            quantity,
            reorder_level,
            date.today()
        ])

        inventory_id += 1

# ---------------------------------
# DataFrame
# ---------------------------------

columns = [
    "Inventory_ID",
    "Warehouse_ID",
    "Product_ID",
    "Quantity_On_Hand",
    "Reorder_Level",
    "Last_Updated"
]

df = pd.DataFrame(inventory, columns=columns)

df.to_csv("data/raw/inventory.csv", index=False)

print(df.head())

print(f"\nTotal Inventory Records: {len(df)}")

print("\n✅ inventory.csv created successfully!")
