# 10.Display passenger name, airline, source, destination and booking status.
SELECT p.passenger_name, f.airline, f.source_city, f.destination_city, b.status
FROM bookings b
JOIN passengers p ON b.passenger_id = p.passenger_id
JOIN flights f ON b.flight_id = f.flight_id;

# 11.Display all passengers including passengers who have never booked a flight.
SELECT p.passenger_id, p.passenger_name, p.city, b.booking_id, b.status
FROM passengers p
LEFT JOIN bookings b ON p.passenger_id = b.passenger_id;

# 12.Find bookings having either no valid passenger, or no valid flight.
SELECT b.* FROM bookings b
LEFT JOIN passengers p ON b.passenger_id = p.passenger_id
LEFT JOIN flights f ON b.flight_id = f.flight_id
WHERE p.passenger_id IS NULL OR f.flight_id IS NULL;


