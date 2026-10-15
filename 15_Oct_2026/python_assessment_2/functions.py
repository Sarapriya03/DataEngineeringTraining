#  Functions/Lambda (Q13-17)

# 13. Create a function calculating shipping cost.
def calculate_shipping_cost(weight, rate_per_kg=60, base_fee=100):
    return base_fee + weight * rate_per_kg
print(calculate_shipping_cost(12.5))

# 14. Create a function returning shipment category based on weight.
def classify_weight(weight):
    if weight > 20:
        return "Heavy"
    if weight >= 10:
        return "Medium"
    return "Light"
print(classify_weight(18.5))

shipments = [                                                              # Q11
    {"shipment_id": "S1001", "destination": "Hyderabad", "weight": 12.5, "status": "Delivered", "cost": 850},
    {"shipment_id": "S1002", "destination": "Mumbai", "weight": 8.0, "status": "In Transit", "cost": 620},
    {"shipment_id": "S1003", "destination": "Bangalore", "weight": 18.5, "status": "Delivered", "cost": 1250},
    {"shipment_id": "S1004", "destination": "Delhi", "weight": 5.5, "status": "Pending", "cost": 480},
    {"shipment_id": "S1005", "destination": "Pune", "weight": 22.0, "status": "Delivered", "cost": 1600},
]

# 15. Use lambda/filter to select Delivered shipments.
delivered = list(filter(lambda s: s["status"] == "Delivered", shipments))
print([s["shipment_id"] for s in delivered])

# 16. Use map to obtain all destinations.
print(list(map(lambda s: s["destination"], shipments)))

# 17. Sort shipment dictionaries by cost.
for s in sorted(shipments, key=lambda s: s["cost"]):
    print(s["shipment_id"], s["cost"])