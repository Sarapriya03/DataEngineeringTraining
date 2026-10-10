# 1.Display customer name, city and email for all customers.
SELECT customer_name, city, email FROM customers;

# 2.Display customers belonging to Hyderabad or Mumbai.
SELECT * FROM customers 
WHERE city IN ('Hyderabad', 'Mumbai');

# 3.Display customers whose names contain the letter 'a'.
SELECT * FROM customers 
WHERE customer_name LIKE '%a%';

# 4.Insert one new customer of your choice.
INSERT INTO customers (customer_id, customer_name, city, mobile, email)
VALUES (8, 'Amit Sharma', 'Chennai', '9840012345', 'amit@gmail.com');

# 5.Update the city of customer ID 6.
UPDATE customers SET city = 'Kochi' 
WHERE customer_id = 6;

# 6.Delete the customer inserted in Question 4.
DELETE FROM customers 
WHERE customer_id = 8;

# 7.Display customers ordered alphabetically by customer name.
SELECT * FROM customers 
ORDER BY customer_name ASC;


