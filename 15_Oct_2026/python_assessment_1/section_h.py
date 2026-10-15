# Section H - Join and Aggregation (Q75-81)

import pandas as pd

# Read:customers.csv, orders.csv
customers = pd.read_csv("customers.csv")
orders = pd.read_csv("orders.csv")
orders["order_value"] = orders["quantity"] * orders["unit_price"]

"""75. Perform an inner join using customer_id .
76. Display:
#order ID
#customer name
#city
#product
#status
#order value"""

merged = pd.merge(orders, customers, on="customer_id", how="inner")   # Q75
print(merged[["order_id", "customer_name", "city", "product",
              "status", "order_value"]])                              # Q76

# 77. Display only Delivered orders from Hyderabad.
print(merged.query("status == 'Delivered' and city == 'Hyderabad'")
      [["order_id", "customer_name", "city", "product", "order_value"]])

"""78. Calculate by city:
#total orders
#total sales
#average order value
79. Sort city results by total sales descending."""

summary = (merged.groupby("city")                                     # Q78
           .agg(total_orders=("order_id", "count"),
                total_sales=("order_value", "sum"),
                average_order_value=("order_value", "mean"))
           .reset_index())
summary = summary.sort_values("total_sales", ascending=False)         # Q79
print(summary)

# 80. Write the result to:city_sales_summary.csv
summary.to_csv("city_sales_summary.csv", index=False)

# 81. Write the same result to:city_sales_summary.json using record-oriented JSON.
summary.to_json("city_sales_summary.json", orient="records", indent=2) 