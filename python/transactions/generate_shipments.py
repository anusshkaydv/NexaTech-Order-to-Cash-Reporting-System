import pandas as pd
import numpy as np

orders = pd.read_csv("data/raw/orders.csv")
order_items = pd.read_csv("data/raw/order_items.csv")
shipping_methods = pd.read_csv("data/raw/shipping_methods.csv")

rng = np.random.default_rng()
n = len(orders)

first_item_warehouse = (
    order_items.drop_duplicates(subset="Order_ID", keep="first")
    .set_index("Order_ID")["Warehouse_ID"]
)
warehouse_id_col = orders["Order_ID"].map(first_item_warehouse).values

orders_with_method = orders.merge(
    shipping_methods[["Shipping_Method_ID", "Estimated_Delivery_Days"]],
    on="Shipping_Method_ID", how="left"
)
estimated_days = orders_with_method["Estimated_Delivery_Days"].values

order_date = pd.to_datetime(orders["Order_Date"])
shipped_date = order_date + pd.to_timedelta(rng.integers(0, 3, size=n), unit="D")
expected_delivery = shipped_date + pd.to_timedelta(estimated_days, unit="D")

shipment_status = rng.choice(["Pending", "In Transit", "Delivered"], size=n)
delay_offset = rng.integers(-1, 5, size=n)
actual_delivery_all = expected_delivery + pd.to_timedelta(delay_offset, unit="D")
actual_delivery = np.where(shipment_status == "Delivered", actual_delivery_all.dt.date, None)
tracking_number = [f"TRK{i:08d}" for i in orders["Order_ID"]]

df = pd.DataFrame({
    "Shipment_ID": orders["Order_ID"], "Shipment_Number": [f"SHP{i:06d}" for i in orders["Order_ID"]],
    "Order_ID": orders["Order_ID"], "Warehouse_ID": warehouse_id_col,
    "Shipment_Date": shipped_date.dt.date, "Expected_Delivery_Date": expected_delivery.dt.date,
    "Actual_Delivery_Date": actual_delivery, "Shipment_Status": shipment_status,
    "Tracking_Number": tracking_number
})

df.to_csv("data/raw/shipments.csv", index=False)
print(df.head())
print(f"\nTotal Shipments Generated: {len(df)}")
print("\n✅ shipments.csv created successfully!")
