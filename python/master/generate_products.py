import pandas as pd
import random
from datetime import date

# ==========================================================
# Project : NexaTech Order-to-Cash Reporting System
# File    : generate_products.py
# Purpose : Generate Products Master Data
# ==========================================================

# ---------------------------------
# Read Product Categories
# ---------------------------------

categories = pd.read_csv("data/raw/product_categories.csv")

category_map = dict(
    zip(categories["Category_Name"], categories["Category_ID"])
)

NUM_PRODUCTS = 500

products = []

# ---------------------------------
# Product Catalog
# ---------------------------------

product_catalog = {

    "Laptop": [
        "Dell Latitude 5440",
        "HP EliteBook 840",
        "Lenovo ThinkPad E14",
        "Acer Aspire 5",
        "ASUS VivoBook 15",
        "Dell Inspiron 15",
        "HP ProBook 450",
        "Lenovo IdeaPad Slim 5"
    ],

    "Desktop": [
        "Dell OptiPlex 7010",
        "HP ProDesk 400",
        "Lenovo ThinkCentre M70",
        "Acer Veriton X",
        "ASUS ExpertCenter D5"
    ],

    "Keyboard": [
        "Logitech K120",
        "Dell KB216",
        "HP 320K",
        "Lenovo Preferred Pro",
        "Logitech MK120"
    ],

    "Mouse": [
        "Logitech M185",
        "Dell MS116",
        "HP X1000",
        "Lenovo 300 USB",
        "Logitech B170"
    ],

    "Monitor": [
        "Dell P2422H",
        "Samsung Odyssey G5",
        "LG UltraFine 24",
        "HP M24f",
        "Lenovo ThinkVision T24"
    ],

    "Printer": [
        "HP LaserJet Pro",
        "Canon Pixma G3020",
        "Brother HL-L2321D",
        "Epson EcoTank L3250",
        "HP Smart Tank 580"
    ],

    "Router": [
        "TP-Link Archer C6",
        "Cisco RV340",
        "Netgear R6700",
        "D-Link DIR-825",
        "ASUS RT-AX53U"
    ],

    "Switch": [
        "Cisco CBS250",
        "TP-Link TL-SG108",
        "Netgear GS308",
        "D-Link DGS-1008A",
        "Cisco Catalyst 1000"
    ],

    "Webcam": [
        "Logitech C270",
        "Logitech C920",
        "HP W300",
        "Dell WB3023",
        "Lenovo 300 FHD"
    ],

    "SSD": [
        "Samsung 980 SSD",
        "WD Blue SN570",
        "Crucial BX500",
        "Kingston NV2",
        "Seagate BarraCuda SSD"
    ]
}

# ---------------------------------
# Product -> Category Mapping
# ---------------------------------

product_category = {
    "Laptop": "Laptops",
    "Desktop": "Desktops",
    "Keyboard": "Accessories",
    "Mouse": "Accessories",
    "Webcam": "Accessories",
    "SSD": "Accessories",
    "Printer": "Accessories",
    "Monitor": "Monitors",
    "Router": "Networking",
    "Switch": "Networking"
}

# ---------------------------------
# Brand Mapping
# ---------------------------------

brand_mapping = {
    "Dell": "Dell",
    "HP": "HP",
    "Lenovo": "Lenovo",
    "Acer": "Acer",
    "ASUS": "ASUS",
    "Samsung": "Samsung",
    "LG": "LG",
    "Canon": "Canon",
    "Brother": "Brother",
    "Epson": "Epson",
    "TP-Link": "TP-Link",
    "Cisco": "Cisco",
    "Netgear": "Netgear",
    "D-Link": "D-Link",
    "Logitech": "Logitech",
    "Kingston": "Kingston",
    "Crucial": "Crucial",
    "WD": "Western Digital",
    "Seagate": "Seagate"
}

# ---------------------------------
# Cost Price Ranges
# ---------------------------------

price_ranges = {

    "Laptop": (30000, 80000),

    "Desktop": (25000, 70000),

    "Keyboard": (500, 3000),

    "Mouse": (300, 2000),

    "Monitor": (8000, 30000),

    "Printer": (6000, 25000),

    "Router": (2000, 15000),

    "Switch": (3000, 20000),

    "Webcam": (1000, 8000),

    "SSD": (2500, 12000)
}

product_types = list(product_catalog.keys())

# ---------------------------------
# Generate Products
# ---------------------------------

for product_id in range(1, NUM_PRODUCTS + 1):

    product_type = random.choice(product_types)

    product_name = random.choice(product_catalog[product_type])

    category_name = product_category[product_type]

    category_id = category_map[category_name]

    product_code = f"PRD{product_id:05d}"

    min_price, max_price = price_ranges[product_type]

    cost_price = random.randint(min_price, max_price)

    profit_margin = random.uniform(1.15, 1.60)

    unit_price = round(cost_price * profit_margin, 2)

    brand = product_name.split()[0]

    brand = brand_mapping.get(brand, brand)

    warranty_months = random.choice([12, 24, 36])

    products.append([
        product_id,
        product_code,
        product_name,
        category_id,
        unit_price,
        cost_price,
        brand,
        warranty_months,
        1,
        date.today()
    ])

# ---------------------------------
# DataFrame
# ---------------------------------

columns = [
    "Product_ID",
    "Product_Code",
    "Product_Name",
    "Category_ID",
    "Unit_Price",
    "Cost_Price",
    "Brand",
    "Warranty_Months",
    "Is_Active",
    "Created_Date"
]

df = pd.DataFrame(products, columns=columns)

# ---------------------------------
# Save CSV
# ---------------------------------

df.to_csv(
    "data/raw/products.csv",
    index=False
)

# ---------------------------------
# Display Output
# ---------------------------------

print(df.head())

print(f"\nTotal Products Generated : {len(df)}")

print("\n✅ products.csv created successfully!")
