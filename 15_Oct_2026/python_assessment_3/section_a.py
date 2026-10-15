# Section A - Python Basics (Q1-10)

# 1. Take attendee name, number of tickets and ticket price from the user.
name = input("Attendee name: ")
tickets = int(input("Number of tickets: "))
ticket_price = float(input("Ticket price: "))

# 2. Calculate total booking amount.
amount = tickets * ticket_price

"""3. Apply:
#10% discount when amount is ₹10,000 or more
#5% otherwise"""
rate = 0.10 if amount >= 10000 else 0.05
discount = amount * rate
final_amount = amount - discount

# 4. Display all results using f-strings.
print(f"Attendee      : {name}")
print(f"Tickets       : {tickets}")
print(f"Total amount  : ₹{amount:,.2f}")
print(f"Discount ({rate:.0%}): ₹{discount:,.2f}")
print(f"Final amount  : ₹{final_amount:,.2f}")

# 5. Ask the user for event capacity and registered participants.
capacity = int(input("Event capacity: "))
registered = int(input("Registered participants: "))

"""6. Display:
#Full if registrations equal capacity
#Seats Available if below capacity
#Invalid Data if registrations exceed capacity"""

if registered == capacity:
    print("Full")
elif registered < capacity:
    print("Seats Available")
else:
    print("Invalid Data")

# 7. Print numbers 1–15 using a for loop.
print("Numbers 1-15:")
for i in range(1, 16):
    print(i, end=" ")

# 8. Display only numbers divisible by 3.
print("\nDivisible by 3:")
for i in range(1, 16):
    if i % 3 == 0:
        print(i, end=" ")

# 9. Use a while loop to count down from 10 to 1.
print("\nCountdown:")
n = 10
while n >= 1:
    print(n, end=" ")
    n -= 1

# 10. Use break and continue in suitable examples.
print("\n\nBreak and continue:")
for i in range(1, 16):
    if i % 2 == 0:
        continue          # skip even numbers
    if i > 11:
        break             # stop after 11
    print(i, end=" ")
print()


