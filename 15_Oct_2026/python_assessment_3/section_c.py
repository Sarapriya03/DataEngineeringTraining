# Section C - Functions, Lambda, Filter, Map (Q26-35)

# 26. Create a function:calculate_booking(ticket_price, tickets)
def calculate_booking(ticket_price, tickets):
    return ticket_price * tickets

# 27. Create a function that accepts booking amount and returns the discount amount.
def calculate_discount(amount):
    return amount * (0.10 if amount >= 10000 else 0.05)

# 28. Create a function that accepts registration status and returns whether the registration is active.
def is_active(status):
    return status == "Confirmed"

# 29. Create a function accepting a list of booking amounts and returning the total.
def total_bookings(amounts):
    return sum(amounts)

print(calculate_booking(2500, 4))
print(calculate_discount(10000), calculate_discount(5000))
print(is_active("Confirmed"), is_active("Cancelled"))
amounts = [5000, 3500, 7500, 6000, 4000, 7000, 3000, 10000]
print(total_bookings(amounts))

# 30. Write a lambda function that increases an amount by 10%.
increase = lambda a: a * 1.10
print(increase(5000))

# 31. Use filter() and lambda to select amounts greater than 6000.
print(list(filter(lambda a: a > 6000, amounts)))

# 32. Create a list of registration dictionaries and use filter() to return Confirmed registrations.
registrations = [                                         # Q32
    {"registration_id": "R1001", "attendee_name": "Aarav Shah", "city": "Hyderabad", "status": "Confirmed", "amount": 5000},
    {"registration_id": "R1002", "attendee_name": "Simran Kaur", "city": "Mumbai", "status": "Confirmed", "amount": 3500},
    {"registration_id": "R1003", "attendee_name": "Faiz Ahmed", "city": "Pune", "status": "Pending", "amount": 7500},
    {"registration_id": "R1005", "attendee_name": "Mohit Kapoor", "city": "Delhi", "status": "Cancelled", "amount": 4000},
    {"registration_id": "R1008", "attendee_name": "Sonal Mehta", "city": "Delhi", "status": "Confirmed", "amount": 10000},
]
confirmed = list(filter(lambda r: r["status"] == "Confirmed", registrations))
print([r["attendee_name"] for r in confirmed])

# 33. Use map() to extract attendee cities.
city_list = list(map(lambda r: r["city"], registrations))
print(city_list)

# 34. Use map() and set() to obtain unique cities.
print(set(map(lambda r: r["city"], registrations)))

# 35. Sort a list of registration dictionaries using:key=.based on amount.
for r in sorted(registrations, key=lambda r: r["amount"]):
    print(r["registration_id"], r["amount"])
