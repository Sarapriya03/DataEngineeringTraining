# Modules (Q34-35)

import shipment_utils                            # normal import
from shipment_utils import classify_weight       # specific-function import

print("Cost per kg  :", shipment_utils.calculate_cost_per_kg(850, 12.5))
print("Shipping cost:", shipment_utils.calculate_shipping_cost(12.5))
print("Category     :", classify_weight(22))