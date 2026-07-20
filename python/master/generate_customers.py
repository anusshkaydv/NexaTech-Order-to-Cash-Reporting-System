import pandas as pd
import random
from faker import Faker
from datetime import date

fake = Faker("en_IN")

# ==========================================================
# Project : NexaTech Order-to-Cash Reporting System
# File    : generate_customers.py
# Purpose : Generate Customers master data
# ==========================================================

# ----------------------------------------------------------
# Read Master Tables
# ----------------------------------------------------------

regions = pd.read_csv("data/raw/regions.csv")
payment_terms = pd.read_csv("data/raw/payment_terms.csv")
employees = pd.read_csv("data/raw/employees.csv")

NUM_CUSTOMERS = 5000

customers = []

# ----------------------------------------------------------
# Generate Customers
# ----------------------------------------------------------

for customer_id in range(1, NUM_CUSTOMERS + 1):

    customer_code = f"CUST{customer_id:05d}"

    company_name = fake.company()

    contact_person = fake.name()

    email = fake.company_email()

    phone = fake.msisdn()[:10]

    city = fake.city()

    region_id = random.choice(regions["Region_ID"])

    payment_term_id = random.choice(payment_terms["Payment_Term_ID"])

    account_manager = random.choice(employees["Employee_ID"])

    customers.append([
        customer_id,
        customer_code,
        company_name,
        contact_person,
        email,
        phone,
        city,
        region_id,
        payment_term_id,
        account_manager,
        1,
        date.today()
    ])

# ----------------------------------------------------------
# Create DataFrame
# ----------------------------------------------------------

columns = [
    "Customer_ID",
    "Customer_Code",
    "Company_Name",
    "Contact_Person",
    "Email",
    "Phone",
    "City",
    "Region_ID",
    "Payment_Term_ID",
    "Account_Manager_ID",
    "Is_Active",
    "Created_Date"
]

df = pd.DataFrame(customers, columns=columns)

# ----------------------------------------------------------
# Save CSV
# ----------------------------------------------------------

df.to_csv(
    "data/raw/customers.csv",
    index=False
)

# ----------------------------------------------------------
# Display Output
# ----------------------------------------------------------

print(df.head())

print(f"\nTotal Customers Generated : {len(df)}")

print("\n✅ customers.csv created successfully!")
