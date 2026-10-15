"""33. Create:shipment_utils.py
containing reusable shipment functions"""

def calculate_cost_per_kg(cost, weight):
    return round(cost / weight, 2)


def classify_weight(weight):
    if weight > 20:
        return "Heavy"
    if weight >= 10:
        return "Medium"
    return "Light"


def calculate_shipping_cost(weight, rate_per_kg=60, base_fee=100):
    return base_fee + weight * rate_per_kg