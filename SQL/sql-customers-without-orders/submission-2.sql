-- Write your query below
SELECT name
FROM customers c
LEFT JOIN orders
ON c.id = customer_id
WHERE customer_id IS NULL;