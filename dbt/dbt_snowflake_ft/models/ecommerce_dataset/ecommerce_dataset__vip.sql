/* 
A query to determine the most valuable customers.
This will create a view named 'ecommerce_dataset__vip'.
As per best practices, the sql is written with a CTE followed by a SELECT statement.
*/

{{ config(materialized='view') }}

WITH vip AS (
    SELECT 
        o.CUSTOMER_ID AS Customer_ID,
        SUM(oi.PRICE) AS Total_Spent
    FROM 
        {{ source('ecommerce_dataset', 'ORDERS')}} o
    INNER JOIN
        {{ source('ecommerce_dataset', 'ORDER_ITEMS')}} oi
    ON
        o.ORDER_ID = oi.ORDER_ID
    --WHERE 
    --    oi.PRICE IS NOT NULL
    GROUP BY
        1
    ORDER BY
        2 DESC
),

results AS (
    SELECT
        *
    FROM
        vip
)

SELECT
    *
FROM
    results