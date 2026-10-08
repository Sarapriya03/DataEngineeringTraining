product = {
    "product_id": 101,
    "product_name": "Laptop",
    "category": "Electronics",
    "price": 65000
}

print(product)

#Access
print(product["product_name"])

#Get without error
print(product.get("brand"))

product["price"] = 70000

#Add a new key-value pair
product["stock"] = 20
print(product)

#Remove
product.pop("category")
del product["price"]

print(product)