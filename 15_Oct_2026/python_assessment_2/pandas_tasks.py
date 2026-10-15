# Pandas (Q36-50) and Enrichment (Q51-54)

import numpy as np
import pandas as pd

# 36. Read shipments.csv.
df = pd.read_csv("shipments.csv")

# 37. Filter Delivered shipments.
print(df[df["status"] == "Delivered"])

# 38. Count records by status.
print(df["status"].value_counts())

# 39. Convert shipment date to datetime.
df["shipment_date"] = pd.to_datetime(df["shipment_date"])

# 40. Count shipments by month and status.
df["month"] = df["shipment_date"].dt.strftime("%Y-%m")
print(df.groupby(["month", "status"]).size().unstack(fill_value=0))

# 41. Calculate average cost by destination.
print(df.groupby("destination")["cost"].mean())

# 42. Calculate total weight by destination.
print(df.groupby("destination")["weight"].sum())

# 43. Read only selected columns using a dynamic usecols list.
cols = ["shipment_id", "hub_id", "destination", "cost"]
subset = pd.read_csv("shipments.csv", usecols=lambda c: c in cols)
print(subset.head())

# 44. Read hubs.csv.
hubs = pd.read_csv("hubs.csv")

# 45. Inner join shipments and hubs using hub_id.
merged = pd.merge(df, hubs, on="hub_id", how="inner")

"""46. Find total shipment cost handled by each hub.
47. Find total number of shipments handled by each hub.
48. Sort hubs by total shipment cost."""

hub_summary = (merged.groupby(["hub_id", "hub_name"])              # Q46, Q47
               .agg(total_cost=("cost", "sum"), total_shipments=("shipment_id", "count"))
               .reset_index()
               .sort_values("total_cost", ascending=False))        # Q48
print(hub_summary)

# 49. Save results to CSV.
hub_summary.to_csv("hub_summary.csv", index=False)

# 50. Save results to JSON.
hub_summary.to_json("hub_summary.json", orient="records", indent=2)

# Enrichment
# 51. Add:cost_per_kg = cost / weight
df["cost_per_kg"] = (df["cost"] / df["weight"]).round(2)

"""52. Use NumPy to classify:
# cost >= 1200 → Expensive
# otherwise    → Normal"""

df["cost_class"] = np.where(df["cost"] >= 1200, "Expensive", "Normal")

# 53. Add a shipment performance category based on both status and cost.
conditions = [
    (df["status"] == "Delivered") & (df["cost_class"] == "Expensive"),
    (df["status"] == "Delivered") & (df["cost_class"] == "Normal"),
    (df["status"] != "Delivered") & (df["cost_class"] == "Expensive"),
]
labels = ["High Value Completed", "Standard Completed", "High Value At Risk"]
df["performance_category"] = np.select(conditions, labels, default="In Progress")

# 54. Save the final enriched dataset as:shipment_analysis.csv
df.to_csv("shipment_analysis.csv", index=False)                    # Q54
print(df)
