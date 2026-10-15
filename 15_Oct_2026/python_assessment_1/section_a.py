# Section A - Python Basics (Q1-9)

# 1. Take product name, unit price and quantity from the user.
product_name = input("Product name: ")
unit_price = float(input("Unit price: "))
quantity = int(input("Quantity: "))

# 2. Calculate total amount.
total = unit_price * quantity

# 3. If total amount is greater than or equal to 50000 , apply 10% discount; otherwise apply 5%.
rate = 0.10 if total >= 50000 else 0.05
discount = total * rate
final_amount = total - discount

# 4. Display original amount, discount and final amount using f-strings.
print(f"Product         : {product_name}")
print(f"Original amount : {total:,.2f}")
print(f"Discount ({rate:.0%}) : {discount:,.2f}")
print(f"Final amount    : {final_amount:,.2f}")

# 5. Ask for stock quantity and display:
# High Stock for stock above 20
# Low Stock for stock between 1 and 20
# Out of Stock for 0

stock = int(input("Stock quantity: "))
if stock > 20:
    print("High Stock")
elif 1 <= stock <= 20:
    print("Low Stock")
elif stock == 0:
    print("Out of Stock")
else:
    print("Invalid stock value")

# 6. Use a for loop to display numbers 1 through 10.
print("\nFor loop 1-10")
for i in range(1, 11):
    print(i, end=" ")

# 7. Use a while loop to reduce stock from 5 to 0.
print("\n\nWhile loop: stock 5 -> 0")
level = 5
while level >= 0:
    print("Stock:", level)
    level -= 1

# 8. Skip number 5 using continue.
# 9. Stop a loop when the value reaches 8 using break
print("\nContinue (skip 5) and break (stop at 8)") 
for i in range(1, 11):
    if i == 5:
        continue
    if i == 8:
        break
    print(i, end=" ")
print()