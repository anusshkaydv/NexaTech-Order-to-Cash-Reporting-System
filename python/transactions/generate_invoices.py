import pandas as pd
import random
from faker import Faker
from datetime import timedelta, date

fake = Faker("en_IN")

# ==========================================================
# Project : NexaTech Order-to-Cash Reporting System
# File    : generate_invoices.py
# Purpose : Generate Invoice data
#
# FIXED: Invoice_Amount now comes from the order's real
# Total_Amount instead of a random number. This is what
# makes the invoice actually match what was ordered.
# ==========================================================

# Read the orders we already generated (with correct Total_Amount)
orders = pd.read_csv("data/raw/orders.csv")

payment_status = [
    "Paid",
    "Partially Paid",
    "Unpaid"
]

invoices = []

# Loop over the real orders instead of a fake range()
for invoice_id, (_, order) in enumerate(orders.iterrows(), start=1):

    invoice_number = f"INV{invoice_id:06d}"

    # Use the order's real ID
    order_id = order["Order_ID"]

    invoice_date = fake.date_between(
        start_date="-1y",
        end_date="today"
    )

    due_date = invoice_date + timedelta(days=30)

    # Invoice amount = the order's actual total (the core fix)
    invoice_amount = round(order["Total_Amount"], 2)

    invoice_status = random.choices(
    ["Paid", "Partially Paid", "Unpaid"],
    weights=[70, 20, 10],
    k=1
)[0]

    invoices.append([
        invoice_id,
        invoice_number,
        order_id,
        invoice_date,
        invoice_amount,
        invoice_status,
        due_date,
        date.today()
    ])

columns = [
    "Invoice_ID",
    "Invoice_Number",
    "Order_ID",
    "Invoice_Date",
    "Invoice_Amount",
    "Invoice_Status",
    "Due_Date",
    "Created_Date"
]

df = pd.DataFrame(invoices, columns=columns)

df.to_csv("data/raw/invoices.csv", index=False)

print(df.head())
print(f"\nTotal Invoices Generated : {len(df)}")
print("\n✅ invoices.csv created successfully!")
