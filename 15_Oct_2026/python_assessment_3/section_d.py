# Section D - OOP (Q36-46)

"""Create:Event with:
#event_id
#event_name
#capacity
#ticket_price
36. Use __init__() to initialize attributes.
37. Create:display_event()
38. Create:calculate_revenue(tickets_sold)"""

class Event:
    def __init__(self, event_id, event_name, capacity, ticket_price):   # Q36
        self.event_id = event_id
        self.event_name = event_name
        self.capacity = capacity
        self.ticket_price = ticket_price

    def display_event(self):                                            # Q37
        print(f"Event {self.event_id}: {self.event_name} | Capacity: {self.capacity} "
              f"| Ticket price: ₹{self.ticket_price}")

    def calculate_revenue(self, tickets_sold):                          # Q38
        return tickets_sold * self.ticket_price

# 39. Create two Event objects.
e1 = Event("E101", "AI Innovation Summit", 500, 2500)
e2 = Event("E102", "Leadership Forum", 350, 3500)
e1.display_event(); e2.display_event()
print("Revenue e1 (120 tickets):", e1.calculate_revenue(120))

"""Create:OnlineEvent that inherits from Event .
40. Add:platform
41. Use super() .
42. Override display_event() to also display the platform."""

class OnlineEvent(Event):
    def __init__(self, event_id, event_name, capacity, ticket_price, platform):
        super().__init__(event_id, event_name, capacity, ticket_price)  # Q41
        self.platform = platform                                        # Q40

    def display_event(self):                                            # Q42
        print(f"[Online] {self.event_id}: {self.event_name} | Capacity: {self.capacity} "
              f"| Price: ₹{self.ticket_price} | Platform: {self.platform}")

"""Create:PhysicalEvent
43. Add:venue
44. Override display_event() ."""

class PhysicalEvent(Event):                                             # Q43
    def __init__(self, event_id, event_name, capacity, ticket_price, venue):
        super().__init__(event_id, event_name, capacity, ticket_price)
        self.venue = venue

    def display_event(self):                                            # Q44
        print(f"[Physical] {self.event_id}: {self.event_name} | Capacity: {self.capacity} "
              f"| Price: ₹{self.ticket_price} | Venue: {self.venue}")

# 45. Put OnlineEvent and PhysicalEvent objects into a list.
events = [OnlineEvent("E201", "Python Webinar", 1000, 500, "Zoom"),
          PhysicalEvent("E103", "Data Engineering Bootcamp", 200, 3000, "Bangalore Tech Park")]

# 46. Call display_event() for every object to demonstrate polymorphism.
for e in events:
    e.display_event()