'''class Product:
    name = "Laptop"
    price = 65000
p1 = Product() #Creates an object -- Product product = new Product()
print(p1.name)
print(p1.price)'''

################################
'''class Product:
    name = ""
    price = 0

p1 = Product()
p1.name = "Laptop"
p1.price = 65000

p2 = Product()
p2.name = "Mouse"
p2.price = 1500

print(p1.name, p1.price)
print(p2.name, p2.price)'''

################################

'''class Product:
    name = ""
    price = 0

    def display(self):
        print(f"Product:{self.name}")
        print(f"Price:{self.price}")

#outside the class
p1 = Product()
p1.name = "Monitor"
p1.price = 18000
p1.display()'''

################################

'''class Product:
    name = ""
    price = 0
    quantity = 0

    def total_amount(self):
        return self.price * self.quantity

p1 = Product()

p1.name = "Laptop"
p1.price = 65000
p1.quantity = 2

print(p1.total_amount())'''

################################

'''class Employee:
    _department = "IT" #Protected Variable

e1 = Employee()
print(e1._department)'''

################################

'''class Employee:
    __bonus = 10000 #Private Variable

e1 = Employee()
print(e1.__bonus)'''

################################

'''class Product:

    def __init__(self): #Constructor
        print("Product object created")

p1 = Product()'''

################################

class Employee:

    def __init__(self, emp_id, name, department, salary): #Parameterized Constructor
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

e1 = Employee(101, "Aman", "IT", 75000)
e2 = Employee(102, "Sara", "HR", 65000)

