import pandas as pd
import random
from faker import Faker
from datetime import date

fake = Faker("en_IN")

# ==========================================================
# Project : NexaTech Order-to-Cash Reporting System
# File    : generate_employees.py
# Purpose : Generate Employees master data
#
# Note:
# This CSV matches the Employees SQL table exactly.
# ==========================================================

# Number of employees to generate
NUM_EMPLOYEES = 100

employees = []

departments = [
    "Sales",
    "Warehouse",
    "Operations",
    "Inventory"
]

designations = [
    "Sales Executive",
    "Warehouse Manager",
    "Sales Manager",
    "Inventory Executive"
]

for emp_id in range(1, NUM_EMPLOYEES + 1):

    employee_code = f"EMP{emp_id:04d}"

    first_name = fake.first_name()

    last_name = fake.last_name()

    email = fake.email()

    phone = fake.msisdn()[:10]

    department = random.choice(departments)

    designation = random.choice(designations)

    warehouse_id = random.randint(1, 5)

    # Employee joining date
    hire_date = fake.date_between(
        start_date="-5y",
        end_date="today"
    )

    employees.append([
        emp_id,
        employee_code,
        first_name,
        last_name,
        email,
        phone,
        department,
        designation,
        warehouse_id,
        hire_date,
        1,
        date.today()
    ])

columns = [
    "Employee_ID",
    "Employee_Code",
    "First_Name",
    "Last_Name",
    "Email",
    "Phone",
    "Department",
    "Designation",
    "Warehouse_ID",
    "Hire_Date",
    "Is_Active",
    "Created_Date"
]

df = pd.DataFrame(employees, columns=columns)

df.to_csv("data/raw/employees.csv", index=False)

print(df.head())

print(f"\nTotal Employees Generated : {len(df)}")

print("\n✅ employees.csv created successfully!")