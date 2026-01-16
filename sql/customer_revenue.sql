SELECT
    c.id AS customer_id,
    c.name AS customer_name,
    s.total_sales
FROM customers c
JOIN agg_sales s
    ON c.id = s.customer_id;
