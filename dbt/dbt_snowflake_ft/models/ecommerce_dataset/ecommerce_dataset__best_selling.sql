/* 
A query to determine the best selling product.
This will create a view named 'ecommerce_dataset__best_selling'.
As per best practices, the sql is written with a CTE followed by a SELECT statement.
*/

{{ config(materialized='view') }}

WITH best_selling AS (
    SELECT 
        oi.PRODUCT_ID AS Product_ID,
        t.PRODUCT_CATEGORY_NAME_ENGLISH AS Product_Category,
        COUNT(oi.ORDER_ID) AS Number_Of_Orders
    FROM 
        {{ source('ecommerce_dataset', 'ORDER_ITEMS')}} oi
    LEFT JOIN
        {{ source('ecommerce_dataset', 'PRODUCTS')}} p
    ON
        oi.PRODUCT_ID = p.PRODUCT_ID
    LEFT JOIN
        {{ source('ecommerce_dataset', 'PRODUCT_CATEGORY_NAME_TRANSLATIONS')}} t
    ON
        p.PRODUCT_CATEGORY_NAME = t.PRODUCT_CATEGORY_NAME
    GROUP BY
        1, 2
    ORDER BY
        3 DESC
),

results AS (
    SELECT
        *
    FROM
        best_selling
)

SELECT
    *
FROM
    results