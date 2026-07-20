import pandas as pd
import random
from faker import Faker
from datetime import date

fake = Faker("en_IN")

# ==========================================================
# Project : NexaTech Order-to-Cash Reporting System
# File    : generate_returns.py
# Purpose : Generate Returns data
#
# FIXED: Refund_Amount is now based on a portion of the
# order's real Total_Amount, instead of a random rupee
# amount unrelated to the order.
# ==========================================================

orders = pd.read_csv("data/raw/orders.csv")

RETURN_SHARE_OF_ORDERS = 0.20
MIN_RETURN_PCT = 0.10
MAX_RETURN_PCT = 1.00

return_reasons = [
    "Damaged Product", "Defective Product", "Wrong Product Delivered",
    "Late Delivery", "Customer Changed Mind"
]
return_statuses = ["Approved", "Pending", "Rejected"]

num_returned_orders = int(len(orders) * RETURN_SHARE_OF_ORDERS)
returned_orders = orders.sample(n=num_returned_orders, random_state=None)

returns = []

for return_id, (_, order) in enumerate(returned_orders.iterrows(), start=1):
    return_number = f"RET{return_id:06d}"
    return_date = fake.date_between(start_date="-1y", end_date="today")
    return_reason = random.choice(return_reasons)
    return_status = random.choice(return_statuses)

    return_pct = random.uniform(MIN_RETURN_PCT, MAX_RETURN_PCT)
    refund_amount = round(order["Total_Amount"] * return_pct, 2)

    if return_status == "Rejected":
        refund_amount = 0.0

    returns.append([
        return_id, return_number, order["Order_ID"], return_date,
        return_reason, return_status, refund_amount, date.today()
    ])

columns = [
    "Return_ID", "Return_Number", "Order_ID", "Return_Date",
    "Return_Reason", "Return_Status", "Refund_Amount", "Created_Date"
]

df = pd.DataFrame(returns, columns=columns)
df.to_csv("data/raw/returns.csv", index=False)
print(df.head())
print(f"\nTotal Returns Generated : {len(df)}")
print("\n✅ returns.csv created successfully!")
