products = ["Laptop", "Mouse", "Keyboard", "Monitor"]

print(products) #Displays Elements in List

print(products[0])
print(products[1])

print(products[-1])

products[1] = "Wireless Mouse"
print(products)

products.append("Disk")
print(products)

products.insert(1,"Led Monitor")
print(products)

products.remove("Monitor")
print(products)

products.pop() # Removes Last Element
print(products)