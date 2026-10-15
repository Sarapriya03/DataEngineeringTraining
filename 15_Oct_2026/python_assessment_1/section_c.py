# Section C - Functions and Lambda (Q21-29)

# 21. Create a function calculate_total(price, quantity)
def calculate_total(price, quantity):
    return price * quantity

# 22. Create a function calculate_discount(amount) that returns the discount.
def calculate_discount(amount):
    return amount * (0.10 if amount >= 50000 else 0.05)

# 23. Create a function accepting a list of sales and returning total sales.
def total_sales(sales):
    return sum(sales)

# 24. Create a function accepting a product dictionary and returning "Available" or "Out of
# Stock".
def check_availability(product):
    return "Available" if product.get("stock", 0) > 0 else "Out of Stock"

print(calculate_total(65000, 2))
print(calculate_discount(130000), calculate_discount(10000))
sales = [65000, 4500, 36000, 12000, 18000, 72000, 9000]
print(total_sales(sales))
print(check_availability({"name": "Laptop", "stock": 12}))
print(check_availability({"name": "Desk", "stock": 0}))

# 25. Use a lambda function to calculate the square of a number.
square = lambda n: n ** 2
print(square(7))

# 26. Use filter() with lambda to select sales greater than 20000.
print(list(filter(lambda s: s > 20000, sales)))

# 27. Use map() to extract customer cities from a list of dictionaries.
customers = [
    {"name": "North Star Retail", "city": "Hyderabad"},
    {"name": "Blue Mart", "city": "Mumbai"},
    {"name": "Prime Stores", "city": "Hyderabad"},
]
city_list = list(map(lambda c: c["city"], customers))
print(city_list)

# 28. Use set() to get unique cities.
print(set(city_list))

# 29. Sort a list of product dictionaries by price using key= .
products = [
    {"name": "Laptop", "price": 65000},
    {"name": "Mouse", "price": 1500},
    {"name": "Monitor", "price": 18000},
]
print(sorted(products, key=lambda p: p["price"]))
