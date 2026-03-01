import json
import csv

# ──────────────────────────────────────────────────
# Exercise 1: Save dict to a JSON and load it back
# ──────────────────────────────────────────────────
config = {
    "app_name": "AI Assistant",
    "version": 2,
    "debug": False,
    "max_users": 100,
    "database": {
        "host": "localhost",
        "port": 5432,
        "username": "admin",
        "timeout": 30
    },
    "features": ["chat", "search", "analytics"],
    "retry_attempts": 3
}

def save_config(data, path):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def load_config(path):
    with open(path, "r") as f:
        config = json.load(f)
        return config
    
save_config(config, "config.json")
    
loaded = load_config("config.json")


# ──────────────────────────────────────────────────
# Exercise 2: Filtered CSV data
# ──────────────────────────────────────────────────
with open("mobile-sales.csv", newline="") as f:
    reader = csv.DictReader(f)
    sales_data = list(reader)
    # for line in sales_data[:2]:
    #     print(line)

top_sales = []

for row in sales_data:
    sale_month = int(row["Sale_Month"])
    if sale_month > 10:
        top_sales.append(row)

with open("top-monthly-sales.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=[
        "Sale_ID",
        "Brand",
        "Model",
        "Country",
        "Storage",
        "Color",
        "Price_USD",
        "Units_Sold",
        "Revenue_USD",
        "Customer_Rating",
        "Payment_Method",
        "Sale_Month",
        "Sale_Year"
    ])
    writer.writeheader()
    writer.writerows(top_sales)
