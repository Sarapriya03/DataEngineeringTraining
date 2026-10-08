a = 20
b = 6

print(a + b) #Addition
print(a - b) #Subtraction
print(a * b) #Multiplication
print(a / b) #Division
print(a // b) #Floor division
print(a % b) #Remainder
print(a ** b) #Power

#Print Even or Odd

numbers = list(range(1, 21))
for num in numbers:
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")