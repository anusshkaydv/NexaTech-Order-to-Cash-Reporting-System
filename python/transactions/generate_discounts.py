import pandas as pd
import random
from datetime import date

# ==========================================================
# Project : NexaTech Order-to-Cash Reporting System
# File    : generate_discounts.py
# Purpose : Generate Discounts data
#
# FIXED: Discount_Value is now a percentage of the order's
# real Total_Amount, not a random rupee amount. Only a
# portion of orders receive a discount (not every order).
# ==========================================================

orders = pd.read_csv("data/raw/orders.csv")

DISCOUNT_SHARE_OF_ORDERS = 0.20   # 20% of orders get a discount
MIN_DISCOUNT_PCT = 0.05           # 5%
MAX_DISCOUNT_PCT = 0.20           # 20%

discount_types = [
    "Festival Offer", "New Customer", "Corporate Discount",
    "Seasonal Offer", "Promotional Campaign"
]

num_discounted_orders = int(len(orders) * DISCOUNT_SHARE_OF_ORDERS)
discounted_orders = orders.sample(n=num_discounted_orders, random_state=None)

discounts = []

for discount_id, (_, order) in enumerate(discounted_orders.iterrows(), start=1):
    discount_type = random.choice(discount_types)
    discount_pct = random.uniform(MIN_DISCOUNT_PCT, MAX_DISCOUNT_PCT)
    discount_value = round(order["Total_Amount"] * discount_pct, 2)
    discount_reason = f"{discount_type} Applied"

    if discount_id <= 5:        
      print("DEBUG Order_ID:", order["Order_ID"])

    discounts.append([
        discount_id, order["Order_ID"], discount_type,
        discount_value, discount_reason, date.today()
    ])

columns = [
    "Discount_ID", "Order_ID", "Discount_Type",
    "Discount_Value", "Discount_Reason", "Created_Date"
]

df = pd.DataFrame(discounts, columns=columns)
df.to_csv("data/raw/discounts.csv", index=False)
print(df.head())
print(f"\nTotal Discounts Generated : {len(df)}")
print("\n✅ discounts.csv created successfully!")
