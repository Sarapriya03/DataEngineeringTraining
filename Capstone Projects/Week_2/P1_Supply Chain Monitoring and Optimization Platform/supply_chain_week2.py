"""
Supply Chain Monitoring and Optimization Platform - Week 2: Data Collection & Preprocessing
Tools: pandas, numpy, requests
"""

from pathlib import Path

import numpy as np
import pandas as pd
import requests

BASE = Path(__file__).parent

# Set API_URL to a real endpoint that returns a JSON list of orders to use requests.
# If it is None, the script reads the local CSV instead.
API_URL = None
REPORT_DATE = pd.Timestamp("2026-10-10")   # fixed "today" so results are repeatable

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 20)


# ---------------------------------------------------------------------
# 1. COLLECT DATA
# Use requests to fetch data from a sample API or local JSON/CSV.
# ---------------------------------------------------------------------
def load_orders():
    if API_URL:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        return pd.DataFrame(response.json())
    return pd.read_csv(BASE / "supply_chain_orders.csv")


orders = load_orders()
suppliers = pd.read_csv(BASE / "suppliers.csv")
inventory = pd.read_csv(BASE / "inventory.csv")

print("RAW ORDERS:", orders.shape)
print(orders.isnull().sum(), "\n")

# ---------------------------------------------------------------------
# 2. CLEAN DATA (pandas)
# Clean data using pandas (drop nulls, format dates, etc.)
# ---------------------------------------------------------------------
orders = orders.drop_duplicates()                                   # remove duplicate rows

# Drop rows missing a required field.
orders = orders.dropna(subset=["order_id", "supplier_id", "product_id", "quantity", "expected_date"])

orders[["order_id", "supplier_id", "product_id", "quantity"]] = \
    orders[["order_id", "supplier_id", "product_id", "quantity"]].astype(int)

for col in ["order_date", "expected_date", "delivery_date"]:        # text -> dates
    orders[col] = pd.to_datetime(orders[col])

orders["status"] = orders["status"].str.strip().str.title()         # " delayed " -> "Delayed"

print("CLEAN ORDERS:", orders.shape, "\n")

# ---------------------------------------------------------------------
# 3. CALCULATIONS (numpy)
# Perform basic calculations using numpy (e.g., delays, stock levels)
# ---------------------------------------------------------------------
# Delivered orders use delivery_date; undelivered orders are measured up to REPORT_DATE
end_date = orders["delivery_date"].fillna(REPORT_DATE)
days_late = (end_date - orders["expected_date"]).dt.days

orders["delay_days"] = np.maximum(days_late, 0)                     # early deliveries = 0
orders["is_delayed"] = np.where(orders["delay_days"] > 0, 1, 0)
orders["lead_time_days"] = (orders["delivery_date"] - orders["order_date"]).dt.days

print("PROCESSED ORDERS")
print(orders[["order_id", "supplier_id", "expected_date", "delivery_date",
              "delay_days", "is_delayed", "status"]], "\n")

# Delay summary per supplier
supplier_summary = (
    orders.groupby("supplier_id")
    .agg(total_orders=("order_id", "count"),
         delayed_orders=("is_delayed", "sum"),
         total_delay_days=("delay_days", "sum"))
    .reset_index()
)
supplier_summary["delay_rate_pct"] = np.round(
    supplier_summary["delayed_orders"] / supplier_summary["total_orders"] * 100, 1)
supplier_summary = supplier_summary.merge(suppliers[["supplier_id", "supplier_name"]], on="supplier_id")
supplier_summary = supplier_summary.sort_values("delayed_orders", ascending=False)

print("DELAY SUMMARY BY SUPPLIER")
print(supplier_summary[["supplier_name", "total_orders", "delayed_orders",
                        "total_delay_days", "delay_rate_pct"]].to_string(index=False), "\n")

# Stock levels
inventory["stock_status"] = np.where(inventory["stock_qty"] <= inventory["reorder_level"], "REORDER", "OK")
inventory["shortage_qty"] = np.maximum(inventory["reorder_level"] - inventory["stock_qty"], 0)
inventory["stock_value"] = inventory["stock_qty"] * inventory["unit_price"]

print("STOCK LEVELS")
print(inventory[["product_name", "stock_qty", "reorder_level", "stock_status",
                 "shortage_qty", "stock_value"]].to_string(index=False), "\n")

# ---------------------------------------------------------------------
# 4. SAVE CLEANED OUTPUT
# Display the cleaned and processed data.
# ---------------------------------------------------------------------
orders.to_csv(BASE / "cleaned_orders.csv", index=False)
inventory.to_csv(BASE / "cleaned_inventory.csv", index=False)
supplier_summary.to_csv(BASE / "supplier_delay_summary.csv", index=False)
print("Saved: cleaned_orders.csv, cleaned_inventory.csv, supplier_delay_summary.csv")
