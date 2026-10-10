# 12.Display customer name, plan name, monthly charge and subscription status.
SELECT c.customer_name, p.plan_name, p.monthly_charge, s.status
FROM subscriptions s
JOIN customers c ON s.customer_id = c.customer_id
JOIN plans p ON s.plan_id = p.plan_id;

# 13.Display all customers, including customers who have no subscription.
SELECT c.customer_id, c.customer_name, c.city, s.subscription_id, s.status
FROM customers c
LEFT JOIN subscriptions s ON c.customer_id = s.customer_id;

# 14.Identify subscriptions having no valid customer or plan.
SELECT s.* FROM subscriptions s
LEFT JOIN customers c ON s.customer_id = c.customer_id
LEFT JOIN plans p ON s.plan_id = p.plan_id
WHERE c.customer_id IS NULL OR p.plan_id IS NULL;




