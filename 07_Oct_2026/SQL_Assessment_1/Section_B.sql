# 8.Find the total number of payments and total amount collected.
SELECT 
    COUNT(payment_id) AS total_number_of_payments, 
    SUM(amount) AS total_amount_collected
FROM payments;

# 9.Calculate total payment amount for each customer.
SELECT customer_id, SUM(amount) AS total_payment_amount
FROM payments
GROUP BY customer_id;

# 10.Display customers whose total payments exceed ₹2,000.
SELECT c.customer_id, c.customer_name, SUM(p.amount) AS total_payments
FROM customers c
JOIN payments p ON c.customer_id = p.customer_id
GROUP BY c.customer_id, c.customer_name
HAVING SUM(p.amount) > 2000;

# 11.Find the average payment amount made by each customer.
SELECT customer_id, AVG(amount) AS average_payment_amount
FROM payments
GROUP BY customer_id;
