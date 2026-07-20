import pandas as pd
import numpy as np
from datetime import timedelta

customers = pd.read_csv("data/raw/customers.csv")
employees = pd.read_csv("data/raw/employees.csv")
shipping_methods = pd.read_csv("data/raw/shipping_methods.csv")

NUM_ORDERS = 50000
order_statuses = ["Pending", "Processing", "Shipped", "Delivered"]
rng = np.random.default_rng()

order_id = np.arange(1, NUM_ORDERS + 1)
order_number = [f"ORD{i:06d}" for i in order_id]
customer_id = rng.choice(customers["Customer_ID"].values, size=NUM_ORDERS)
employee_id = rng.choice(employees["Employee_ID"].values, size=NUM_ORDERS)
shipping_method_id = rng.choice(shipping_methods["Shipping_Method_ID"].values, size=NUM_ORDERS)

today = pd.Timestamp.today().normalize()
day_offsets = rng.integers(0, 365, size=NUM_ORDERS)
order_date = [(today - timedelta(days=int(d))).date() for d in day_offsets]
order_status = rng.choice(order_statuses, size=NUM_ORDERS)

df = pd.DataFrame({
    "Order_ID": order_id, "Order_Number": order_number, "Customer_ID": customer_id,
    "Employee_ID": employee_id, "Shipping_Method_ID": shipping_method_id,
    "Order_Date": order_date, "Total_Amount": 0.0, "Order_Status": order_status, "Is_Active": 1
})

df.to_csv("data/raw/orders.csv", index=False)
print(df.head())
print(f"\nTotal Orders Generated : {len(df)}")
print("\n✅ orders.csv created successfully!")
