-- =====================================================================
-- Customer Order Insights & Delivery Tracker --
-- =====================================================================

CREATE DATABASE customer_orders;
USE customer_orders;

# 1.Design MySQL tables for customers, orders, and delivery_status.
-- ---------------------------------------------------------------------
-- 1. TABLES
-- ---------------------------------------------------------------------
CREATE TABLE customers (
    customer_id    INT PRIMARY KEY,
    customer_name  VARCHAR(100),
    email          VARCHAR(100),
    city           VARCHAR(50),
    region         VARCHAR(20)          -- South / North / East / West
);

CREATE TABLE orders (
    order_id       INT PRIMARY KEY AUTO_INCREMENT,
    customer_id    INT,
    product_name   VARCHAR(100),
    quantity       INT,
    amount         DECIMAL(10,2),
    order_date     DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE delivery_status (
    delivery_id    INT PRIMARY KEY AUTO_INCREMENT,
    order_id       INT,
    expected_date  DATE,
    delivery_date  DATE,                -- NULL if not delivered yet
    status         VARCHAR(20),         -- Delivered / Delayed / In Transit
    issue          VARCHAR(50),         -- reason for delay (NULL if none)
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE
);

CREATE INDEX idx_orders_customer ON orders(customer_id);
CREATE INDEX idx_delivery_order  ON delivery_status(order_id);

-- ---------------------------------------------------------------------
-- 2. DATA
-- ---------------------------------------------------------------------
INSERT INTO customers VALUES
(1, 'Arun Kumar',   'arun@example.com',    'Chennai',    'South'),
(2, 'Priya Sharma', 'priya@example.com',   'Delhi',      'North'),
(3, 'Karthik Raj',  'karthik@example.com', 'Coimbatore', 'South'),
(4, 'Sneha Patel',  'sneha@example.com',   'Mumbai',     'West'),
(5, 'Rahul Das',    'rahul@example.com',   'Kolkata',    'East'),
(6, 'Meena Iyer',   'meena@example.com',   'Madurai',    'South'),
(7, 'Amit Verma',   'amit@example.com',    'Lucknow',    'North'),
(8, 'Divya Nair',   'divya@example.com',   'Pune',       'West');

INSERT INTO orders (order_id, customer_id, product_name, quantity, amount, order_date) VALUES
(1,  1, 'Wireless Mouse',     1,  799.00, '2026-09-01'),
(2,  1, 'Laptop Bag',         1, 1499.00, '2026-09-10'),
(3,  1, 'USB Cable',          3,  450.00, '2026-09-25'),
(4,  2, 'Bluetooth Speaker',  1, 2499.00, '2026-09-02'),
(5,  2, 'Phone Case',         2,  598.00, '2026-09-15'),
(6,  3, 'Keyboard',           1, 1299.00, '2026-09-03'),
(7,  3, 'Monitor Stand',      1, 1899.00, '2026-09-18'),
(8,  3, 'Power Bank',         1, 1599.00, '2026-10-01'),
(9,  4, 'Headphones',         1, 2999.00, '2026-09-05'),
(10, 4, 'Smart Watch',        1, 4999.00, '2026-09-20'),
(11, 5, 'Backpack',           1, 1799.00, '2026-09-07'),
(12, 5, 'Water Bottle',       2,  700.00, '2026-09-22'),
(13, 6, 'Desk Lamp',          1,  999.00, '2026-09-09'),
(14, 6, 'Webcam',             1, 2199.00, '2026-09-28'),
(15, 7, 'Tablet Cover',       1,  899.00, '2026-09-12'),
(16, 7, 'Memory Card',        2, 1100.00, '2026-10-02'),
(17, 8, 'Yoga Mat',           1, 1250.00, '2026-09-14'),
(18, 8, 'Running Shoes',      1, 3499.00, '2026-09-30'),
(19, 2, 'Router',             1, 2799.00, '2026-10-04'),
(20, 1, 'Earbuds',            1, 1999.00, '2026-10-06');

INSERT INTO delivery_status (order_id, expected_date, delivery_date, status, issue) VALUES
(1,  '2026-09-06', '2026-09-05', 'Delivered',  NULL),
(2,  '2026-09-15', '2026-09-18', 'Delayed',    'Courier delay'),
(3,  '2026-09-30', NULL,         'Delayed',    'Courier delay'),
(4,  '2026-09-07', '2026-09-07', 'Delivered',  NULL),
(5,  '2026-09-20', '2026-09-24', 'Delayed',    'Weather'),
(6,  '2026-09-08', '2026-09-08', 'Delivered',  NULL),
(7,  '2026-09-23', '2026-09-23', 'Delivered',  NULL),
(8,  '2026-10-06', NULL,         'Delayed',    'Address not found'),
(9,  '2026-09-10', '2026-09-09', 'Delivered',  NULL),
(10, '2026-09-25', '2026-09-30', 'Delayed',    'Courier delay'),
(11, '2026-09-12', '2026-09-14', 'Delayed',    'Weather'),
(12, '2026-09-27', '2026-09-27', 'Delivered',  NULL),
(13, '2026-09-14', '2026-09-13', 'Delivered',  NULL),
(14, '2026-10-03', NULL,         'Delayed',    'Stock shortage'),
(15, '2026-09-17', '2026-09-17', 'Delivered',  NULL),
(16, '2026-10-07', '2026-10-09', 'Delayed',    'Address not found'),
(17, '2026-09-19', '2026-09-18', 'Delivered',  NULL),
(18, '2026-10-05', '2026-10-05', 'Delivered',  NULL),
(19, '2026-10-12', NULL,         'In Transit', NULL),
(20, '2026-10-14', NULL,         'In Transit', NULL);

# 2.Perform basic CRUD operations on orders
-- CREATE: a new order for Meena (customer 6) + its delivery record
INSERT INTO orders (customer_id, product_name, quantity, amount, order_date)
VALUES (6, 'Gaming Chair', 1, 8999.00, '2026-10-10');

INSERT INTO delivery_status (order_id, expected_date, delivery_date, status, issue)
VALUES (LAST_INSERT_ID(), '2026-10-17', NULL, 'In Transit', NULL);

-- READ
SELECT * FROM orders;
SELECT * FROM orders WHERE customer_id = 1;

SELECT o.order_id, c.customer_name, o.product_name, o.amount, d.status, d.expected_date
FROM orders o
JOIN customers c       ON c.customer_id = o.customer_id
JOIN delivery_status d ON d.order_id    = o.order_id
ORDER BY o.order_id;

-- UPDATE
UPDATE orders SET quantity = 2, amount = 17998.00 WHERE order_id = 21;             -- change quantity
UPDATE delivery_status
SET status = 'Delivered', delivery_date = '2026-10-10'
WHERE order_id = 19; 

-- DELETE (delivery_status row is removed automatically via ON DELETE CASCADE)
DELETE FROM orders WHERE order_id = 21;

# 3.Write a stored procedure to fetch all delayed deliveries for a customer.
DELIMITER $$

CREATE PROCEDURE get_delayed_deliveries(IN p_customer_id INT)
BEGIN
    SELECT c.customer_name,
           o.order_id,
           o.product_name,
           d.expected_date,
           d.delivery_date,
           d.issue,
           DATEDIFF(COALESCE(d.delivery_date, CURDATE()), d.expected_date) AS days_late
    FROM customers c
    JOIN orders o          ON o.customer_id = c.customer_id
    JOIN delivery_status d ON d.order_id    = o.order_id
    WHERE c.customer_id = p_customer_id
      AND d.status = 'Delayed'
    ORDER BY d.expected_date;
END$$

DELIMITER ;

-- Test it
CALL get_delayed_deliveries(1);    -- Arun: orders 2 and 3
CALL get_delayed_deliveries(3);    -- Karthik: order 8
CALL get_delayed_deliveries(8);    -- Divya: no delays (empty result)
