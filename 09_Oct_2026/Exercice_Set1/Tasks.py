# --- Task 1: Read shipments.csv using Python's csv module ---

import csv

with open("shipments.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)

# --- Task 2: Store all records inside a Python list ---

import csv

shipments = []

with open("shipments.csv", "r", newline = "") as file:

    reader = csv.DictReader(file)

    for row in reader:
        shipments.append(row)

# --- Task 3: Display the complete list ---
        
print("Task 3: Complete Shipment List:")
for s in shipments:
    print(s)

# --- Task 4: Display only shipment ID, customer, and status ---

print("\nTask 4: Selective Fields (ID, Customer, Status):")
for s in shipments:
    print(f"ID: {s['shipment_id']}, Customer: {s['customer']}, Status: {s['status']}")

# --- Task 5: Convert weight and cost from strings to numeric values ---

for s in shipments:
    s['weight'] = float(s['weight'])
    s['cost'] = float(s['cost'])

# --- Task 6: Calculate the total shipping cost ---

total_cost = sum(float(s['cost']) for s in shipments)
print(f"\nTask 6: Total Shipping Cost: {total_cost}")

# --- Task 7: Find shipments whose cost is greater than 700 ---

print("\nTask 7: Shipments with cost > 700:")
high_cost_shipments = [s for s in shipments if float(s['cost']) > 700]
for s in high_cost_shipments:
    print(f"ID: {s['shipment_id']}, Cost: {s['cost']}")

# --- Task 8: Use filter() and lambda to display only Delivered shipments ---

print("\nTask 8: Delivered Shipments (Using filter & lambda):")
delivered = list(filter(lambda s: s['status'] == "Delivered", shipments))
for s in delivered:
    print(f"ID: {s['shipment_id']}, Status: {s['status']}")

# --- Task 9: Use filter() and lambda to find shipments weighing more than 10 ---

print("\nTask 9: Shipments weighing more than 10 (Using filter & lambda):")
heavy_shipments = list(filter(lambda s: float(s['weight']) > 10, shipments))
for s in heavy_shipments:
    print(f"ID: {s['shipment_id']}, Weight: {s['weight']}")

# --- Task 10: Use map() to extract all city names ---

print("\nTask 10: All City Names (Using map):")
all_cities = list(map(lambda s: s['city'], shipments))
print(all_cities)

# --- Task 11: Use map() + set() to get the unique cities ---

print("\nTask 11: Unique Cities:")
unique_cities = set(map(lambda s: s['city'], shipments))
print(unique_cities)

# --- Task 12: Sort the shipment list by cost from lowest to highest using key ---

print("\nTask 12: Sorted by Cost (Lowest to Highest):")
sorted_by_cost = sorted(shipments, key=lambda s: float(s['cost']))
for s in sorted_by_cost:
    print(f"ID: {s['shipment_id']}, Cost: {s['cost']}")

# --- Task 13: Sort by weight from highest to lowest ---

print("\nTask 13: Sorted by Weight (Highest to Lowest):")
sorted_by_weight = sorted(shipments, key=lambda s: float(s['weight']), reverse=True)
for s in sorted_by_weight:
    print(f"ID: {s['shipment_id']}, Weight: {s['weight']}")

# --- Task 14: Sort alphabetically by customer name ---

print("\nTask 14: Sorted Alphabetically by Customer:")
sorted_by_customer = sorted(shipments, key=lambda s: s['customer'])
for s in sorted_by_customer:
    print(f"Customer: {s['customer']}, ID: {s['shipment_id']}")

# --- Task 15: Lambda function to calculate cost per kg and display ---

cost_per_kg = lambda s: float(s['cost']) / float(s['weight'])

print("\nTask 15: Cost per KG for every shipment:")
for s in shipments:
    cpk = cost_per_kg(s)
    print(f"ID: {s['shipment_id']}, Cost per KG: {cpk:.2f}")