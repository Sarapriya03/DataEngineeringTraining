# 15.Produce a cleaned customer output according to rules:
# • Names have leading/trailing spaces removed.
# • Emails are lowercase.
# • Blank emails become NULL.
# • Mobile numbers contain only numeric characters.
SELECT 
    customer_id,
    TRIM(customer_name) AS cleaned_customer_name,
    city,
    REGEXP_REPLACE(mobile, '[^0-9]', '') AS cleaned_mobile,
    CASE 
        WHEN TRIM(email) = '' THEN NULL 
        ELSE LOWER(TRIM(email)) 
    END AS cleaned_email
FROM customers;

# 16.Using RegEx, identify mobile numbers containing alphabetic characters.
SELECT * FROM customers 
WHERE mobile REGEXP '[a-zA-Z]';

