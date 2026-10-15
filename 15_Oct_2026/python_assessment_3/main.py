# Section H - using the user-defined module (Q76-79)

# 76. Import the entire module.
import event_utils

# 78. Import one function directly.
from event_utils import calculate_discount

# 79. Import the module using an alias.
import event_utils as eu

# 77. Call all three functions.
amount = event_utils.calculate_booking_amount(2500, 4)
print("Booking amount:", amount)
print("Discount      :", event_utils.calculate_discount(amount))
print("Capacity check:", event_utils.check_event_capacity(500, 320))

print("Direct import :", calculate_discount(5000))
print("Alias import  :", eu.check_event_capacity(100, 100))