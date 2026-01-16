SELECT
    customer_id,
    SUM(amount) AS total_sales
FROM stg_orders
GROUP BY customer_id;
