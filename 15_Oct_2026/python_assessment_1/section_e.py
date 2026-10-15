# Section E - Text, CSV and JSON files (Q40-55)

import csv
import json

"""40. Create activity.txt .
41. Write three processing messages to it.
42. Append one additional message.
43. Read and display the complete file."""

with open("activity.txt", "w") as f:
    f.write("Order processing started\n")
    f.write("Orders validated\n")
    f.write("Inventory updated\n")
with open("activity.txt", "a") as f:
    f.write("Order processing completed\n")
with open("activity.txt", "r") as f:
    print(f.read())

"""Using customers.csv :
44. Read the CSV using the csv module.
45. Store the records in a Python list.
46. Display only active customers.
47. Display only Hyderabad customers"""

with open("customers.csv", newline="") as f:
    customers = list(csv.DictReader(f))  # Q44, Q45
print("Active customers:")
for c in customers:
    if c["active"] == "True":                              # Q46
        print(" ", c["customer_id"], c["customer_name"])
print("Hyderabad customers:")
for c in customers:
    if c["city"] == "Hyderabad":                           # Q47
        print(" ", c["customer_id"], c["customer_name"])

# Using products.json:
# 48. Read the JSON file.
with open("products.json") as f:
    products = json.load(f)

# 49. Display all product names.
print("Product names:", [p["product_name"] for p in products])

# 50. Display products costing above 10000.
print("Price > 10000:", [p["product_name"] for p in products if p["price"] > 10000])

# 51. Display supplier name and supplier city for every product.
for p in products:
    print(f'{p["product_name"]}: {p["supplier"]["name"]} ({p["supplier"]["city"]})')

# 52. Extract all colors into one list.
all_colors = [c for p in products for c in p["colors"]]
print("All colors:", all_colors)

# 53. Display unique colors.
print("Unique colors:", set(all_colors))

#54. Increase stock of product ID 202 .
#55. Write the modified data back to a new file:products_updated.json

for p in products:                                         # Q54
    if p["product_id"] == 202:
        p["stock"] += 10
with open("products_updated.json", "w") as f:              # Q55
    json.dump(products, f, indent=2)
print("Saved products_updated.json")

