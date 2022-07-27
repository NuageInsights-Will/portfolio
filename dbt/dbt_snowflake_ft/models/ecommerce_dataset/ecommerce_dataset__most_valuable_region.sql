/* 
A query to determine which geographical region holds the most value.
This will create a view named 'ecommerce_dataset__most_valueable_region'.
As per best practices, the sql is written with CTEs followed by a SELECT statement.
*/

{{ config(materialized='view') }}

WITH revenue_by_region AS (
    SELECT
        Region,
        SUM(State_Revenue) AS Gross_Revenue
    FROM 
        {{ ref('ecommerce_dataset__revenue_by_state') }}
    GROUP BY 
        1
    ORDER BY 
        2 DESC
),

results AS(
    SELECT 
        *
    FROM 
        revenue_by_region
)

SELECT
    *
FROM
    results