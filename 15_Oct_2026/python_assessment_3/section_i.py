# Section I - Pandas Basics (Q80-88)
#Using registrations.csv:
import pandas as pd

# 80. Read the file into a DataFrame.
df = pd.read_csv("registrations.csv")

"""81. Display:
#first 5 rows
$last 5 rows
#shape
#columns
#datatypes"""

print(df.head(5))
print(df.tail(5))
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print(df.dtypes)

# 82. Display only:attendee_name,city,status,amount
print(df[["attendee_name", "city", "status", "amount"]])

# 83. Use query() to find Confirmed registrations.
print(df.query("status == 'Confirmed'"))

# 84. Find registrations whose amount exceeds ₹6,000.
print(df[df["amount"] > 6000])

# 85. Find Confirmed registrations from Hyderabad.
print(df.query("status == 'Confirmed' and city == 'Hyderabad'"))

# 86. Count registrations by status.
print(df["status"].value_counts())

# 87. Find total amount by status.
print(df.groupby("status")["amount"].sum())

# 88. Find average amount by city.
print(df.groupby("city")["amount"].mean())