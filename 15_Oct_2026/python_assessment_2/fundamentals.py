# Python Fundamentals (Q1-6)

# 1. Accept shipment weight and cost from the user.
weight = float(input("Shipment weight (kg): "))
cost = float(input("Shipment cost: "))

# 2. Calculate cost per kg.
print(f"Cost per kg: {cost / weight:.2f}")

"""3. Classify:
weight above 20 → Heavy
10–20 → Medium
below 10 → Light"""

if weight > 20:
    category = "Heavy"
elif weight >= 10:
    category = "Medium"
else:
    category = "Light"
print("Category:", category)

# 4. Use loops to display shipment numbers from 1–20.
print("Shipment numbers 1-20:")
for n in range(1, 21):
    print(n, end=" ")

# 5. Display only even shipment numbers.
print("\nEven shipment numbers:")
for n in range(1, 21):
    if n % 2 == 0:
        print(n, end=" ")

# 6. Use a while loop to simulate five processing attempts.
print("\n\nProcessing attempts:")
attempt = 1
while attempt <= 5:
    print(f"Processing attempt {attempt} of 5")
    attempt += 1