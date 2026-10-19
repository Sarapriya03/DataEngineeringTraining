"""
Customer Order Insights & Delivery Tracker - Week 2: Data Processing with Python
Tools: pandas, numpy, requests
"""

from pathlib import Path

import numpy as np
import pandas as pd
import requests

BASE = Path(__file__).parent

# Set API_URL to an endpoint that returns a JSON list of orders to use requests.
# If it is None, the script reads the local CSV instead.
API_URL = None
REPORT_DATE = pd.Timestamp("2026-10-10")   # fixed "today" so results are repeatable

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 20)


# ---------------------------------------------------------------------
# 1. LOAD DATA
#  Use Python to load customer order data from an API or CSV.
# ---------------------------------------------------------------------
def load_orders():
    if API_URL:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        return pd.DataFrame(response.json())
    return pd.read_csv(BASE / "orders.csv")


df = load_orders()
customers = pd.read_csv(BASE / "customers.csv")

print("RAW DATA:", df.shape)
print(df.isnull().sum(), "\n")

# ---------------------------------------------------------------------
# 2. CLEAN DATA
# Clean missing fields and convert timestamps.
# ---------------------------------------------------------------------
df = df.drop_duplicates()                              # remove duplicate rows
df = df.dropna(subset=["customer_id"])                 # an order must belong to a customer
df["customer_id"] = df["customer_id"].astype(int)

df["quantity"] = df["quantity"].fillna(1).astype(int)  # missing quantity -> 1

df["status"] = df["status"].str.strip().str.title()
df["issue"] = df["issue"].str.strip().str.title()      # "weather" -> "Weather"
# Delayed orders with no reason recorded -> "Unknown"
df.loc[(df["status"] == "Delayed") & (df["issue"].isnull()), "issue"] = "Unknown"

# Convert timestamps (delivery_date stays empty for undelivered orders)
for col in ["order_date", "expected_date", "delivery_date"]:
    df[col] = pd.to_datetime(df[col])

print("CLEAN DATA:", df.shape, "\n")

# ---------------------------------------------------------------------
# 3. DELIVERY DELAYS
# Use NumPy to calculate delivery delays.
# ---------------------------------------------------------------------
# Compare calendar days: delivered orders use delivery_date, others use REPORT_DATE
end_date = df["delivery_date"].dt.normalize().fillna(REPORT_DATE)
days_late = (end_date - df["expected_date"]).dt.days

df["delay_days"] = np.maximum(days_late, 0)
df["delayed"] = np.where(df["delay_days"] > 0, 1, 0)

print("PROCESSED ORDERS")
print(df[["order_id", "customer_id", "product_name", "status",
          "delay_days", "delayed", "issue"]].to_string(index=False), "\n")

# ---------------------------------------------------------------------
# 4. INSIGHTS
#  Show top delayed customers and most common delivery issues.
# ---------------------------------------------------------------------
# Top delayed customers
top_customers = (
    df.groupby("customer_id")
    .agg(delayed_orders=("delayed", "sum"), total_delay_days=("delay_days", "sum"))
    .reset_index()
    .merge(customers, on="customer_id")
    .sort_values(["delayed_orders", "total_delay_days"], ascending=False)
)
print("TOP DELAYED CUSTOMERS")
print(top_customers[["customer_name", "region", "delayed_orders", "total_delay_days"]]
      .head(5).to_string(index=False), "\n")

# Most common delivery issues
issue_counts = df.loc[df["delayed"] == 1, "issue"].value_counts()
print("MOST COMMON DELIVERY ISSUES")
print(issue_counts.to_string(), "\n")

# Overall delay rate
delay_rate = np.round(df["delayed"].mean() * 100, 1)
print(f"Overall delay rate: {delay_rate}% ({df['delayed'].sum()} of {len(df)} orders)\n")

# ---------------------------------------------------------------------
# 5. SAVE CLEANED OUTPUT
# ---------------------------------------------------------------------
df.to_csv(BASE / "cleaned_orders.csv", index=False)
top_customers.to_csv(BASE / "top_delayed_customers.csv", index=False)
issue_counts.rename_axis("issue").reset_index(name="count").to_csv(BASE / "delivery_issues.csv", index=False)
print("Saved: cleaned_orders.csv, top_delayed_customers.csv, delivery_issues.csv")
