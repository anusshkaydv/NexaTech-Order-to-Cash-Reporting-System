import pandas as pd

# ---------------------------------
# Read Data
#update_order_totals.py
# ---------------------------------

orders = pd.read_csv("data/raw/orders.csv")

order_items = pd.read_csv("data/raw/order_items.csv")

# ---------------------------------
# Calculate Total Amount
# ---------------------------------

order_totals = (
    order_items
    .groupby("Order_ID")["Line_Total"]
    .sum()
)

# ---------------------------------
# Update Orders
# ---------------------------------

orders["Total_Amount"] = orders["Order_ID"].map(order_totals)

orders["Total_Amount"] = orders["Total_Amount"].fillna(0)

# ---------------------------------
# Save Updated Orders
# ---------------------------------

orders.to_csv("data/raw/orders.csv", index=False)

print(orders.head())

print("\n✅ Orders updated successfully!")