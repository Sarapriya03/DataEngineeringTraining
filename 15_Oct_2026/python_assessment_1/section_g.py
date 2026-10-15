# Section G - Pandas Data Processing (Q61-74)

import pandas as pd

# Using orders.csv :
# 61. Read the CSV into a Pandas DataFrame.
df = pd.read_csv("orders.csv")

# 62. Display first 5 rows.
print(df.head(5))

# 63. Display column names and datatypes.
print(df.columns.tolist()); print(df.dtypes)

# 64. Display shape of the DataFrame.
print("Shape:", df.shape)

# 65. Filter only Delivered orders using query().
print(df.query("status == 'Delivered'"))

# 66. Filter orders where quantity is greater than 2.
print(df[df["quantity"] > 2])

# 67. Calculate a new column:order_value = quantity × unit_price
df["order_value"] = df["quantity"] * df["unit_price"]

# 68. Count orders by status.
print(df["status"].value_counts())

# 69. Convert order_date to datetime.
df["order_date"] = pd.to_datetime(df["order_date"])

# 70. Create a month column.
df["month"] = df["order_date"].dt.strftime("%Y-%m")

# 71. Find order count by month and status.
print(df.groupby(["month", "status"]).size().unstack(fill_value=0))

# 72. Find total order value by category.
print(df.groupby("category")["order_value"].sum())

# 73. Find average order value by category.
print(df.groupby("category")["order_value"].mean())

# 74. Sort orders by order value descending.
print(df.sort_values("order_value", ascending=False))