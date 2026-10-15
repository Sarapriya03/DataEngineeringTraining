# Section B - Lists, Tuples, Sets, Dictionaries (Q10-20)

sales = [65000, 4500, 36000, 12000, 18000, 72000, 9000]

# 10. Find total sales.
print("Total sales:", sum(sales))

# 11. Find highest and lowest sale.
print("Highest:", max(sales), "| Lowest:", min(sales))

# 12. Display sales greater than 20000.
print("Sales > 20000:", [s for s in sales if s > 20000])

# 13. Sort sales from highest to lowest.
print("Sorted high->low:", sorted(sales, reverse=True))

# 14. Create a set from:
# cities = [
# "Hyderabad",
# "Mumbai",
# "Delhi",
# "Hyderabad",
# "Pune",
# "Mumbai"
# ] and display unique cities.
cities = ["Hyderabad", "Mumbai", "Delhi", "Hyderabad", "Pune", "Mumbai"]
unique_cities = set(cities)
print("Unique cities:", unique_cities)

# 15. Create a tuple containing:
# Product ID
# Product Name
# Category
# Price
# and unpack it into individual variables.
product = (201, "Laptop", "Electronics", 65000)
product_id, product_name, category, price = product
print(product_id, product_name, category, price)

# 16. Create a dictionary representing a customer with:
# ID
# Name
# City
# Orders
# Active status
customer = {"id": "C101", "name": "North Star Retail",
            "city": "Hyderabad", "orders": 3, "active": True}

# 17. Update the customer's city.
customer["city"] = "Chennai"

# 18. Increase order count by 1.
customer["orders"] += 1

# 19. Add an email field.
customer["email"] = "contact@northstar.com"

# 20. Loop through all keys and values.
for key, value in customer.items():
    print(f"{key}: {value}")