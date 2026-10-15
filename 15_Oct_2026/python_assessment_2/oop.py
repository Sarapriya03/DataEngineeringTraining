# OOP (Q18-23)

"""18. Create a Shipment class.
19. Add constructor values for shipment ID, destination, weight and cost.
20. Add a display method."""

class Shipment:                                                # Q18
    def __init__(self, shipment_id, destination, weight, cost):    # Q19
        self.shipment_id = shipment_id
        self.destination = destination
        self.weight = weight
        self.cost = cost

    def total_cost(self):
        return self.cost

    def display(self):                                         # Q20
        print(f"Shipment {self.shipment_id} -> {self.destination} | "
              f"{self.weight} kg | Total cost: {self.total_cost()}")

"""21. Create ExpressShipment inheriting from Shipment .
22. Override a method to add an express surcharge.
23. Demonstrate polymorphism using normal and express shipment objects."""

class ExpressShipment(Shipment):                               # Q21
    SURCHARGE = 0.25

    def total_cost(self):                                      # Q22 (override)
        return self.cost + self.cost * self.SURCHARGE

    def display(self):
        print(f"EXPRESS Shipment {self.shipment_id} -> {self.destination} | "
              f"{self.weight} kg | Total cost (with surcharge): {self.total_cost()}")


for s in [Shipment("S1001", "Hyderabad", 12.5, 850),           # Q23 polymorphism
          ExpressShipment("S1002", "Mumbai", 8.0, 620)]:
    s.display()