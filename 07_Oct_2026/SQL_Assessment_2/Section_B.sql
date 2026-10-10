# 6.Find average ticket price by airline.
SELECT airline, AVG(ticket_price) AS average_ticket_price
FROM flights
GROUP BY airline;

# 7.Find total number of seats booked on each flight.
SELECT flight_id, SUM(seats) AS total_seats_booked
FROM bookings
GROUP BY flight_id;

# 8.Find airlines whose average ticket price exceeds ₹8,000.
SELECT airline, AVG(ticket_price) AS average_ticket_price
FROM flights
GROUP BY airline
HAVING AVG(ticket_price) > 8000;

# 9.Find total booking value per airline using: seats * ticket_price.
SELECT f.airline, SUM(b.seats * f.ticket_price) AS total_booking_value
FROM bookings b
JOIN flights f ON b.flight_id = f.flight_id
GROUP BY f.airline;



