-- =====================================================================
-- Supply Chain Monitoring and Optimization Platform --
-- =====================================================================

CREATE DATABASE supply_chain;
USE supply_chain;

# 1.Create MySQL tables for orders, suppliers, inventory
-- ---------------------------------------------------------------------
-- 1. TABLES
-- ---------------------------------------------------------------------
CREATE TABLE suppliers (
    supplier_id    INT PRIMARY KEY,
    supplier_name  VARCHAR(100),
    city           VARCHAR(50),
    phone          VARCHAR(15)
);

CREATE TABLE inventory (
    product_id     INT PRIMARY KEY,
    product_name   VARCHAR(100),
    supplier_id    INT,
    stock_qty      INT,
    reorder_level  INT,
    unit_price     DECIMAL(10,2),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);

CREATE TABLE orders (
    order_id       INT PRIMARY KEY AUTO_INCREMENT,
    supplier_id    INT,
    product_id     INT,
    quantity       INT,
    order_date     DATE,
    expected_date  DATE,
    delivery_date  DATE,          -- NULL until delivered
    status         VARCHAR(20),   -- Delivered / Delayed / Shipped / Pending
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id),
    FOREIGN KEY (product_id)  REFERENCES inventory(product_id)
);

-- Indexes
CREATE INDEX idx_orders_supplier ON orders(supplier_id);
CREATE INDEX idx_orders_status   ON orders(status);

-- ---------------------------------------------------------------------
-- 2. DATA
-- ---------------------------------------------------------------------
INSERT INTO suppliers VALUES
(1, 'Tamil Nadu Textiles',  'Coimbatore', '9840011122'),
(2, 'Bharat Electronics',   'Bengaluru',  '9845022233'),
(3, 'Sagar Packaging',      'Chennai',    '9841033344'),
(4, 'Deccan Auto Parts',    'Pune',       '9822044455'),
(5, 'Konkan Steel Works',   'Mumbai',     '9820066677');

INSERT INTO inventory VALUES
(1,  'Cotton Fabric Roll',     1, 120,  50,  850.00),
(2,  'Polyester Thread Spool', 1,  40, 100,   45.00),
(3,  'Microcontroller Board',  2,  75,  40,  320.00),
(4,  'Lithium Battery Pack',   2,  30,  60, 1450.00),
(5,  'Corrugated Box',         3, 500, 200,   28.00),
(6,  'Bubble Wrap Roll',       3,  90, 100,  210.00),
(7,  'Brake Pad Set',          4, 150,  80,  650.00),
(8,  'Steel Rod 12mm',         5, 800, 300,   72.00),
(9,  'Steel Sheet 2mm',        5, 250, 100,  560.00),
(10, 'Engine Oil Filter',      4,  60,  70,  180.00);

INSERT INTO orders (order_id, supplier_id, product_id, quantity, order_date, expected_date, delivery_date, status) VALUES
(1,  1, 1,  200, '2026-09-01', '2026-09-08', '2026-09-07', 'Delivered'),
(2,  1, 2,  300, '2026-09-02', '2026-09-09', '2026-09-12', 'Delivered'),
(3,  2, 3,  150, '2026-09-03', '2026-09-13', '2026-09-13', 'Delivered'),
(4,  2, 4,  100, '2026-09-05', '2026-09-15', '2026-09-20', 'Delivered'),
(5,  3, 5, 1000, '2026-09-06', '2026-09-10', '2026-09-10', 'Delivered'),
(6,  3, 6,  200, '2026-09-08', '2026-09-13', '2026-09-16', 'Delivered'),
(7,  4, 7,  200, '2026-09-10', '2026-09-20', '2026-09-19', 'Delivered'),
(8,  4, 10, 250, '2026-09-12', '2026-09-22', '2026-09-28', 'Delivered'),
(9,  5, 8, 1000, '2026-09-15', '2026-09-25', '2026-09-25', 'Delivered'),
(10, 5, 9,  300, '2026-09-18', '2026-09-28', '2026-10-02', 'Delivered'),
(11, 3, 5,  800, '2026-09-25', '2026-09-30', NULL,         'Delayed'),
(12, 2, 4,  100, '2026-09-28', '2026-10-05', NULL,         'Delayed'),
(13, 4, 10, 200, '2026-10-02', '2026-10-12', NULL,         'Shipped'),
(14, 1, 1,  250, '2026-10-05', '2026-10-15', NULL,         'Shipped'),
(15, 5, 8,  200, '2026-10-07', '2026-10-17', NULL,         'Pending');

# 2.Perform basic CRUD operations
-- CREATE
INSERT INTO suppliers VALUES (6, 'Test Supplier', 'Madurai', '9000000000');
INSERT INTO orders (supplier_id, product_id, quantity, order_date, expected_date, status)
VALUES (3, 5, 500, '2026-10-10', '2026-10-15', 'Pending');

-- READ
SELECT * FROM suppliers;
SELECT * FROM inventory WHERE stock_qty <= reorder_level;      -- low stock
SELECT * FROM orders WHERE status = 'Delayed';                 -- delayed orders

SELECT o.order_id, s.supplier_name, i.product_name, o.quantity, o.status
FROM orders o
JOIN suppliers s ON s.supplier_id = o.supplier_id
JOIN inventory i ON i.product_id  = o.product_id;

-- UPDATE
UPDATE orders SET status = 'Delivered', delivery_date = '2026-10-10' WHERE order_id = 11;
UPDATE inventory SET stock_qty = stock_qty + 800 WHERE product_id = 5;

-- DELETE
DELETE FROM orders    WHERE order_id = 16;      -- the test order added above
DELETE FROM suppliers WHERE supplier_id = 6;    -- the test supplier

# 3.Write stored procedures (e.g., auto reorder trigger)
--    Creates a Pending order (2 x reorder level) for every product whose stock is at/below its reorder level and has no open order.
DELIMITER $$

CREATE PROCEDURE auto_reorder()
BEGIN
    INSERT INTO orders (supplier_id, product_id, quantity, order_date, expected_date, status)
    SELECT i.supplier_id, i.product_id, i.reorder_level * 2,
           CURDATE(), DATE_ADD(CURDATE(), INTERVAL 7 DAY), 'Pending'
    FROM inventory i
    WHERE i.stock_qty <= i.reorder_level
      AND NOT EXISTS (SELECT 1 FROM orders o
                      WHERE o.product_id = i.product_id
                        AND o.status IN ('Pending', 'Shipped', 'Delayed'));

    SELECT ROW_COUNT() AS orders_created;
END$$

DELIMITER ;

-- Test it: products 2 (Thread) and 6 (Bubble Wrap) are low with no open order
CALL auto_reorder();
SELECT * FROM orders ORDER BY order_id DESC LIMIT 5;

