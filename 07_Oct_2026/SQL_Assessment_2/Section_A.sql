# 1.Display flights originating from Hyderabad.
SELECT * FROM flights 
WHERE source_city = 'Hyderabad';

# 2.Display flights priced between ₹6,000 and 20,000.
SELECT * FROM flights 
WHERE ticket_price BETWEEN 6000 AND 20000;

# 3.Display international-looking routes where ticket price exceeds ₹15,000.
SELECT * FROM flights 
WHERE ticket_price > 15000;

# 4.Increase the ticket price of all SkyJet flights by 5%.
SET SQL_SAFE_UPDATES = 0;

UPDATE flights SET ticket_price = ticket_price * 1.05 
WHERE airline = 'SkyJet';

# 5.Display the three most expensive flights.
SELECT * FROM flights 
ORDER BY ticket_price DESC LIMIT 3;
