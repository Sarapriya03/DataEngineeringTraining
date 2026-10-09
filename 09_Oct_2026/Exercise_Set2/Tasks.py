sales = [
    ("North", 12000),
    ("South", 18000),
    ("West", 9500),
    ("North", 22000),
    ("East", 15000),
    ("South", 11000)
]

# --- Task 1: Display all tuples ---

print("Task 1: All Tuples:")
for item in sales:
    print(item)

# --- Task 2: Display only the region from every tuple ---

print("\nTask 2: Regions Only:")
for region, amount in sales:
    print(region)

# --- Task 3: Display only the sales amount ---

print("\nTask 3: Sales Amounts Only:")
for region, amount in sales:
    print(amount)

# --- Task 4: Find sales greater than 12000 ---

print("\nTask 4: Sales greater than 12000:")
high_sales = []
for item in sales:
    if item[1] > 12000:
        high_sales.append(item)

for item in high_sales:
    print(item)

# --- Task 5: Calculate total sales ---

print("\nTask 5: Total Sales:")
total_sales = 0
for item in sales:
    total_sales += item[1]  # Adds the sales amount to the running total

print(f"Total Sales: {total_sales}")

# --- Task 6: Find the highest and lowest sales amount ---

print("\nTask 6: Highest and Lowest Sales Amount:")
# Initialize with the very first sale amount to start comparing
highest_sales = sales[0][1]
lowest_sales = sales[0][1]

for item in sales:
    amount = item[1]
    if amount > highest_sales:
        highest_sales = amount
    if amount < lowest_sales:
        lowest_sales = amount

print(f"Highest Sales: {highest_sales}, Lowest Sales: {lowest_sales}")

# --- Task 7: Create a list containing only sales amounts ---

print("\nTask 7: List of Sales Amounts:")
sales_amounts = []
for item in sales:
    sales_amounts.append(item[1])

print(f"List of Sales Amounts: {sales_amounts}")

# --- Task 8: Find unique regions using a set ---

print("\nTask 8: Unique Regions:")
unique_regions = set()  # Initializes an empty set
for item in sales:
    unique_regions.add(item[0])  # .add() automatically skips duplicates

print(f"Unique Regions: {unique_regions}")
# --- Task 9: Sort the tuples based on sales amount ---

print("\nTask 9: Sorted by Sales Amount (Lowest to Highest):")
sorted_by_amount = sorted(sales, key=lambda item: item[1])
for item in sorted_by_amount:
    print(item)

# --- Task 10: Sort the tuples based on region name ---

print("\nTask 10: Sorted Alphabetically by Region Name:")
sorted_by_region = sorted(sales, key=lambda item: item[0])
for item in sorted_by_region:
    print(item)
