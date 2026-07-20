import pandas as pd
from datetime import date

product_categories = [
    [1, "Laptops", "Business and personal laptops", 1, date.today()],
    [2, "Desktops", "Desktop computers", 1, date.today()],
    [3, "Accessories", "Keyboard, Mouse, Webcam, etc.", 1, date.today()],
    [4, "Monitors", "LED and LCD monitors", 1, date.today()],
    [5, "Networking", "Routers, Switches and Modems", 1, date.today()]
]

columns = [
    "Category_ID",
    "Category_Name",
    "Category_Description",
    "Is_Active",
    "Created_Date"
]

df = pd.DataFrame(product_categories, columns=columns)

df.to_csv("data/raw/product_categories.csv", index=False)

print(df)
print("\n✅ product_categories.csv created successfully!")
