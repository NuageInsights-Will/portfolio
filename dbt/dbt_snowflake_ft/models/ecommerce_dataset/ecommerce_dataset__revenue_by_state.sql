/* 
A query to determine which states are providing the most business.
This will create a view named 'ecommerce_dataset__revenue_by_state'.
As per best practices, the sql is written with CTEs followed by a SELECT statement.
*/

{{ config(materialized='view') }}

WITH purchase_data AS (
    SELECT  
        oi.order_id AS Order_ID, 
        c.customer_id AS Customer_ID,
        c.customer_state AS Customer_State,
        oi.price AS Order_Total  
    FROM 
        {{ source('ecommerce_dataset', 'ORDERS') }} o
    INNER JOIN
        {{ source('ecommerce_dataset', 'ORDER_ITEMS') }} oi
    ON      
        o.order_id = oi.order_id
    INNER JOIN 
        {{ source('ecommerce_dataset', 'CUSTOMERS') }} c
    ON 
        o.customer_id = c.customer_id
    ORDER BY 
        c.customer_id
),

customer_purchase_aggregate AS (
    SELECT DISTINCT
        Customer_ID,
        Customer_State,
        SUM(Order_Total) AS Total_Spent_Per_Customer
    FROM purchase_data
    GROUP BY
        1, 2
),

revenue_by_state AS (
    SELECT
        CASE
            WHEN Customer_State = 'SP' THEN 'São Paulo'
            WHEN Customer_State = 'RJ' THEN 'Rio de Janeiro'
            WHEN Customer_State = 'MG' THEN 'Minas Gerais'
            WHEN Customer_State = 'RS' THEN 'Rio Grande do Sul'
            WHEN Customer_State = 'PR' THEN 'Paraná'
            WHEN Customer_State = 'SC' THEN 'Santa Catarina'
            WHEN Customer_State = 'BA' THEN 'Bahia'
            WHEN Customer_State = 'DF' THEN 'Distrito Federal'
            WHEN Customer_State = 'GO' THEN 'Goiás'
            WHEN Customer_State = 'ES' THEN 'Espírito Santo'
            WHEN Customer_State = 'PE' THEN 'Pernambuco'
            WHEN Customer_State = 'CE' THEN 'Ceará'
            WHEN Customer_State = 'PA' THEN 'Pará'
            WHEN Customer_State = 'MT' THEN 'Mato Grosso'
            WHEN Customer_State = 'MA' THEN 'Maranhão'
            WHEN Customer_State = 'MS' THEN 'Mato Grosso do Sul'
            WHEN Customer_State = 'PB' THEN 'Paraíba'
            WHEN Customer_State = 'PI' THEN 'Piauí'
            WHEN Customer_State = 'RN' THEN 'Rio Grande do Norte'
            WHEN Customer_State = 'AL' THEN 'Alagoas'
            WHEN Customer_State = 'SE' THEN 'Sergipe'
            WHEN Customer_State = 'TO' THEN 'Tocantins'
            WHEN Customer_State = 'RO' THEN 'Rondônia'
            WHEN Customer_State = 'AM' THEN 'Amazonas'
            WHEN Customer_State = 'AC' THEN 'Acre'
            WHEN Customer_State = 'AP' THEN 'Amapá'
            WHEN Customer_State = 'RR' THEN 'Roraima'
            ELSE NULL
        END AS State_Name,
        Customer_State AS State_Code,
        CASE
            WHEN Customer_State = 'AC' THEN 'North'
            WHEN Customer_State = 'AP' THEN 'North'
            WHEN Customer_State = 'AM' THEN 'North'
            WHEN Customer_State = 'PA' THEN 'North'
            WHEN Customer_State = 'RO' THEN 'North'
            WHEN Customer_State = 'RR' THEN 'North'
            WHEN Customer_State = 'TO' THEN 'North'
            --
            WHEN Customer_State = 'AL' THEN 'North-East'
            WHEN Customer_State = 'BA' THEN 'North-East'
            WHEN Customer_State = 'CE' THEN 'North-East'
            WHEN Customer_State = 'MA' THEN 'North-East'
            WHEN Customer_State = 'PB' THEN 'North-East'
            WHEN Customer_State = 'PE' THEN 'North-East'
            WHEN Customer_State = 'PI' THEN 'North-East'
            WHEN Customer_State = 'RN' THEN 'North-East'
            WHEN Customer_State = 'SE' THEN 'North-East'
            --
            WHEN Customer_State = 'GO' THEN 'Central-West'
            WHEN Customer_State = 'MT' THEN 'Central-West'
            WHEN Customer_State = 'MS' THEN 'Central-West'
            WHEN Customer_State = 'DF' THEN 'Central-West'
            --
            WHEN Customer_State = 'ES' THEN 'South-East'
            WHEN Customer_State = 'MG' THEN 'South-East'
            WHEN Customer_State = 'RJ' THEN 'South-East'
            WHEN Customer_State = 'SP' THEN 'South-East'
            --
            WHEN Customer_State = 'PR' THEN 'South'
            WHEN Customer_State = 'RS' THEN 'South'
            WHEN Customer_State = 'SC' THEN 'South'
            ELSE NULL
        END AS Region,
        SUM(Total_Spent_Per_Customer) AS State_Revenue
    FROM
        customer_purchase_aggregate
    GROUP BY
        1, 2, 3
    ORDER BY 
        4 DESC
),

results AS(
    SELECT 
        *
    FROM 
        revenue_by_state
)

SELECT
    *
FROM
    results