"""Reusable retail helper functions (Section F, Q56)."""

"""56. Add functions for:
# calculating order total,
# calculating discount,
# checking stock."""

def calculate_order_total(quantity, unit_price):
    return quantity * unit_price


def calculate_discount(amount):
    """10% for amounts >= 50000, otherwise 5%."""
    return amount * (0.10 if amount >= 50000 else 0.05)


def check_stock(stock):
    if stock > 20:
        return "High Stock"
    if stock >= 1:
        return "Low Stock"
    return "Out of Stock"