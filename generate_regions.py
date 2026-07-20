import pandas as pd
from datetime import date
# GENERATE REGIONS DATA
regions = [
    [1, "NR", "North", "Delhi", 1, date.today()],
    [2, "SR", "South", "Bengaluru", 1, date.today()],
    [3, "ER", "East", "Kolkata", 1, date.today()],
    [4, "WR", "West", "Mumbai", 1, date.today()],
    [5, "CR", "Central", "Nagpur", 1, date.today()]
]

columns = [
    "Region_ID",
    "Region_Code",
    "Region_Name",
    "Headquarters_City",
    "Is_Active",
    "Created_Date"
]

df = pd.DataFrame(regions, columns=columns)

df.to_csv("data/raw/regions.csv", index=False)

print(df)
print("\n✅ regions.csv created successfully!")