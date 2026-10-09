class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Developer(Employee):

    def __init__(self, name, salary, language):
        super().__init__(name, salary) # super() automatically triggers the parent (Employee) constructor
        self.language = language # new attribute unique to Developer

d1 = Developer("Neha", 85000, "Python")
print(d1.name)
print(d1.salary)
print(d1.language)