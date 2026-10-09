import pandas as pd

df = pd.read_csv("orders.csv")

#print(df)

# Extract --- Transform --- Load --- ETL process

#print(df.head())

#print(df.tail())

#print(df.columns)

#print(df.shape)

#print(df.dtypes)

#print(df.info)

# Select
'''print(df["product"])

print(
    df[
        ["order_id", "product", "amount"]
    ]
)'''

# Filter
'''delivered = df.query("status == 'Delivered'")
print(delivered)

result = df.query("amount > 20000")
print(result)'''

# Value_counts
'''print(
    df["status"].value_counts()
)'''

# Groupby
'''result = (
    df.groupby("status").size()
)
print(result)'''

# String to Date
'''df["order_date"] = pd.to_datetime(df["order_date"])
df["month"] = df["order_date"].dt.month
print(df)'''


