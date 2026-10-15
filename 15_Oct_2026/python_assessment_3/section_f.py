# Section F - CSV Processing Without Pandas (Q53-60)
# Using registrations.csv
import csv

"""53. Read the file using the csv module.
54. Store records in a Python list."""

with open("registrations.csv", newline="") as f:
    records = list(csv.DictReader(f))

# 55. Display only Confirmed registrations.
print("Confirmed registrations:")
for r in records:
    if r["status"] == "Confirmed":
        print(" ", r["registration_id"], r["attendee_name"])

# 56. Display registrations from Hyderabad.
print("Hyderabad registrations:")
for r in records:
    if r["city"] == "Hyderabad":
        print(" ", r["registration_id"], r["attendee_name"])

# 57. Convert amount into a numeric datatype.
for r in records:
    r["amount"] = float(r["amount"])
    r["tickets"] = int(r["tickets"])

# 58. Find registrations where amount exceeds ₹7,000.
print("Amount > 7000:")
for r in records:
    if r["amount"] > 7000:
        print(" ", r["registration_id"], r["attendee_name"], r["amount"])

# 59. Calculate total registration amount.
print("Total amount:", sum(r["amount"] for r in records))

# 60. Extract all cities and display unique cities.
all_cities = [r["city"] for r in records]
print("All cities   :", all_cities)
print("Unique cities:", set(all_cities))