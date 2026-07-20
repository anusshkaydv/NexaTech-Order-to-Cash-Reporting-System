import pandas as pd
import numpy as np

orders = pd.read_csv("data/raw/orders.csv")
products = pd.read_csv("data/raw/products.csv")
warehouses = pd.read_csv("data/raw/warehouses.csv")

rng = np.random.default_rng()
items_per_order = rng.integers(1, 6, size=len(orders))
order_id_col = np.repeat(orders["Order_ID"].values, items_per_order)
total_lines = len(order_id_col)

product_id_col = rng.choice(products["Product_ID"].values, size=total_lines)
warehouse_id_col = rng.choice(warehouses["Warehouse_ID"].values, size=total_lines)
quantity_col = rng.integers(1, 6, size=total_lines)

line_df = pd.DataFrame({
    "Order_ID": order_id_col, "Product_ID": product_id_col,
    "Warehouse_ID": warehouse_id_col, "Quantity": quantity_col
})
line_df = line_df.merge(products[["Product_ID", "Unit_Price"]], on="Product_ID", how="left")
line_df["Line_Total"] = (line_df["Quantity"] * line_df["Unit_Price"]).round(2)
line_df.insert(0, "Order_Item_ID", np.arange(1, len(line_df) + 1))

line_df.to_csv("data/raw/order_items.csv", index=False)
print(line_df.head())
print(f"\nTotal Order Items Generated : {len(line_df)}")
print("\n✅ order_items.csv created successfully!")