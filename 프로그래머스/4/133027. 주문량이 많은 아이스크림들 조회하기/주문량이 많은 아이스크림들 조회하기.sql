WITH JULY_TOTAL AS (
    SELECT 
        FLAVOR, 
        SUM(TOTAL_ORDER) AS JULY_SUM 
    FROM 
        JULY 
    GROUP BY 
        FLAVOR
)

SELECT 
    FH.FLAVOR 
FROM 
    FIRST_HALF FH
JOIN
    JULY_TOTAL JT
ON
    FH.FLAVOR = JT.FLAVOR
ORDER BY 
    (FH.TOTAL_ORDER + COALESCE(JT.JULY_SUM, 0)) DESC
LIMIT 
    3