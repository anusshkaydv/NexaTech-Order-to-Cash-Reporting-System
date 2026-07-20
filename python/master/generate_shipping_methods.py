import pandas as pd
from datetime import date
#GENERATE SHIPPING METHODS DATA
shipping_methods = [
    [1, "Standard", 5, 1, date.today()],
    [2, "Express", 2, 1, date.today()],
    [3, "Air Freight", 1, 1, date.today()],
    [4, "Surface Transport", 7, 1, date.today()],
    [5, "Pickup", 0, 1, date.today()]
]

columns = [
    "Shipping_Method_ID",
    "Shipping_Method_Name",
    "Estimated_Delivery_Days",
    "Is_Active",
    "Created_Date"
]

df = pd.DataFrame(shipping_methods, columns=columns)

df.to_csv("data/raw/shipping_methods.csv", index=False)

print(df)
print("\n✅ shipping_methods.csv created successfully!")
