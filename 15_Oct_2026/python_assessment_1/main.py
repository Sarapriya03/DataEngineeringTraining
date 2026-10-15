# Section F - using the user-defined module (Q57-60)

# 57. Import the module.
import retail_utils

# 59. Import one function directly and call it without the module name.
from retail_utils import calculate_discount

# 60. Import the module using an alias.
import retail_utils as ru

# 58. Call all three functions.
total = retail_utils.calculate_order_total(2, 30000)
print("Order total :", total)
print("Discount    :", retail_utils.calculate_discount(total))
print("Stock status:", retail_utils.check_stock(12))

print("Direct import discount:", calculate_discount(10000))
print("Alias import total    :", ru.calculate_order_total(3, 1500))
