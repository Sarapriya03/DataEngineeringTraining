# Section I - NumPy/Pandas Enrichment (Q82-84)

import numpy as np
import pandas as pd

customers = pd.read_csv("customers.csv")
orders = pd.read_csv("orders.csv")
orders["order_value"] = orders["quantity"] * orders["unit_price"]
merged = pd.merge(orders, customers, on="customer_id", how="inner")

"""82. Create a column order_size using NumPy:
#order_value >= 50000 → High
#order_value >= 15000 → Medium
#otherwise            → Low"""
merged["order_size"] = np.select(
    [merged["order_value"] >= 50000, merged["order_value"] >= 15000],
    ["High", "Medium"], default="Low")

# 83. Create a new column:priority_customer where Corporate customers are marked Priority , others Normal.
merged["priority_customer"] = np.where(
    merged["segment"] == "Corporate", "Priority", "Normal")

# 84. Save the enriched dataset as:enriched_orders.csv
merged.to_csv("enriched_orders.csv", index=False)
print(merged[["order_id", "customer_name", "segment", "order_value",
              "order_size", "priority_customer"]])