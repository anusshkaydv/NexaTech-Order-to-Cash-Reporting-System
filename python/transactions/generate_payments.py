import pandas as pd
import random
from faker import Faker
from datetime import date, timedelta

fake = Faker("en_IN")

# ==========================================================
# Project : NexaTech Order-to-Cash Reporting System
# File    : generate_payments.py
# Purpose : Generate realistic payment transactions
#
# Logic:
# Paid            -> 100% payment
# Partially Paid  -> 40-80% payment
# Unpaid          -> No payment generated
# ==========================================================

# Read data
invoices = pd.read_csv("data/raw/invoices.csv")
invoices["Invoice_Date"] = pd.to_datetime(invoices["Invoice_Date"])

orders = pd.read_csv("data/raw/orders.csv")
customers = pd.read_csv("data/raw/customers.csv")
payment_terms = pd.read_csv("data/raw/payment_terms.csv")

# Merge to get customer payment terms
invoices_with_terms = (
    invoices
    .merge(
        orders[["Order_ID", "Customer_ID"]],
        on="Order_ID",
        how="left"
    )
    .merge(
        customers[["Customer_ID", "Payment_Term_ID"]],
        on="Customer_ID",
        how="left"
    )
    .merge(
        payment_terms[["Payment_Term_ID", "Credit_Days"]],
        on="Payment_Term_ID",
        how="left"
    )
)

payment_methods = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "NEFT",
    "RTGS",
    "Bank Transfer",
    "Cheque"
]

payments = []
payment_id = 1

for _, invoice in invoices_with_terms.iterrows():

    invoice_amount = round(invoice["Invoice_Amount"], 2)
    invoice_date = invoice["Invoice_Date"]
    credit_days = int(invoice["Credit_Days"])
    invoice_status = invoice["Invoice_Status"]

    base_delay = max(credit_days, 5)

    low = int(base_delay * 0.6)
    high = int(base_delay * 1.3) + 5

    # ==========================
    # PAID
    # ==========================
    if invoice_status == "Paid":

        payment_amount = invoice_amount
        payment_status = "Paid"

        payment_date = (
            invoice_date +
            timedelta(days=random.randint(low, high))
        ).date()

        payments.append([
            payment_id,
            f"PAY{payment_id:06d}",
            invoice["Invoice_ID"],
            payment_date,
            random.choice(payment_methods),
            payment_amount,
            payment_status,
            fake.uuid4(),
            date.today()
        ])

        payment_id += 1

    # ==========================
    # PARTIALLY PAID
    # ==========================
    elif invoice_status == "Partially Paid":

        payment_amount = round(
            invoice_amount * random.uniform(0.40, 0.80),
            2
        )

        payment_status = "Partially Paid"

        payment_date = (
            invoice_date +
            timedelta(days=random.randint(low, high))
        ).date()

        payments.append([
            payment_id,
            f"PAY{payment_id:06d}",
            invoice["Invoice_ID"],
            payment_date,
            random.choice(payment_methods),
            payment_amount,
            payment_status,
            fake.uuid4(),
            date.today()
        ])

        payment_id += 1

    # ==========================
    # UNPAID
    # ==========================
    elif invoice_status == "Unpaid":

        # No payment generated
        continue

columns = [
    "Payment_ID",
    "Payment_Number",
    "Invoice_ID",
    "Payment_Date",
    "Payment_Method",
    "Payment_Amount",
    "Payment_Status",
    "Transaction_Reference",
    "Created_Date"
]

df = pd.DataFrame(payments, columns=columns)

df.to_csv("data/raw/payments.csv", index=False)

print(df.head())
print(f"\nTotal Payments Generated : {len(df)}")
print("\n✅ payments.csv created successfully!")
