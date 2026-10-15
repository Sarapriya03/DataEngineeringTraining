# Section D - OOP (Q30-39)

"""Create a class:Product
with:
product_id
product_name
price
stock"""

# 30. Initialize the values using __init__().
class Product:
    def __init__(self, product_id, product_name, price, stock):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.stock = stock

# 31. Add a method display_product().
    def display_product(self):
        print(f"[Product] {self.product_id} | {self.product_name} | "
              f"Price: {self.price} | Stock: {self.stock}")

# 32. Add a method calculate_value() returning:price × stock
    def calculate_value(self):
        return self.price * self.stock

# Create a child class:DiscountedProduct

# 34. Inherit from Product .
# 35. Add discount_percent .
# 36. Use super() to initialize parent values.

class DiscountedProduct(Product):                                 # Q34
    def __init__(self, product_id, product_name, price, stock, discount_percent):
        super().__init__(product_id, product_name, price, stock)  # Q36
        self.discount_percent = discount_percent                  # Q35

# 37. Override display_product() so the discounted product also displays its discount.
    def display_product(self):
        print(f"[Discounted] {self.product_id} | {self.product_name} | "
              f"Price: {self.price} | Stock: {self.stock} | Discount: {self.discount_percent}%")

# Create another class:PremiumProduct

# 38. Give it its own version of display_product().
class PremiumProduct(Product):
    def display_product(self):
        print(f"[Premium] {self.product_name} - premium item, price {self.price}, "
              f"stock {self.stock}")

# 33. Create two product objects.
p1 = Product(201, "Laptop", 65000, 12)
p2 = Product(202, "Monitor", 18000, 8)
p1.display_product(); p2.display_product()
print("Value p1:", p1.calculate_value(), "| Value p2:", p2.calculate_value())

# 39. Put Product , DiscountedProduct and PremiumProduct objects into a list and call
# display_product() for each to demonstrate polymorphism.
items = [p1,
         DiscountedProduct(203, "Office Chair", 9000, 15, 10),
         PremiumProduct(204, "Gaming Laptop", 120000, 3)]
for item in items:
    item.display_product()

