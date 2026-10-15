# Collections (Q7-12)

# 7. Create a list of shipment costs.
costs = [850, 620, 1250, 480, 1600, 740, 590, 1100, 920, 1750, 520, 1050]

# 8. Calculate total, average, minimum and maximum.
print("Total:", sum(costs), "| Average:", round(sum(costs) / len(costs), 2),
      "| Min:", min(costs), "| Max:", max(costs))

# 9. Remove duplicate destination cities using a set.
destinations = ["Hyderabad", "Mumbai", "Bangalore", "Delhi", "Pune", "Hyderabad",
                "Mumbai", "Delhi", "Bangalore", "Pune", "Hyderabad", "Mumbai"]
print("Unique destinations:", set(destinations))

# 10. Store one shipment using a dictionary.
shipment = {"shipment_id": "S1001", "destination": "Hyderabad",            # Q10
            "weight": 12.5, "status": "Delivered", "cost": 850}
print(shipment)

# 11. Store multiple shipments using a list of dictionaries.
shipments = [                                                              # Q11
    {"shipment_id": "S1001", "destination": "Hyderabad", "weight": 12.5, "status": "Delivered", "cost": 850},
    {"shipment_id": "S1002", "destination": "Mumbai", "weight": 8.0, "status": "In Transit", "cost": 620},
    {"shipment_id": "S1003", "destination": "Bangalore", "weight": 18.5, "status": "Delivered", "cost": 1250},
    {"shipment_id": "S1004", "destination": "Delhi", "weight": 5.5, "status": "Pending", "cost": 480},
    {"shipment_id": "S1005", "destination": "Pune", "weight": 22.0, "status": "Delivered", "cost": 1600},
]

# 12. Filter list records by status.
print([s["shipment_id"] for s in shipments if s["status"] == "Pending"])