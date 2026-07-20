import pandas as pd
from datetime import date

payment_terms = [
    [1, "Immediate", 0, 1, date.today()],
    [2, "Net 15", 15, 1, date.today()],
    [3, "Net 30", 30, 1, date.today()],
    [4, "Net 45", 45, 1, date.today()],
    [5, "Net 60", 60, 1, date.today()]
]

columns = [
    "Payment_Term_ID",
    "Payment_Term_Name",
    "Credit_Days",
    "Is_Active",
    "Created_Date"
]

df = pd.DataFrame(payment_terms, columns=columns)

df.to_csv("data/raw/payment_terms.csv", index=False)

print(df)
print("\n✅ payment_terms.csv created successfully!")