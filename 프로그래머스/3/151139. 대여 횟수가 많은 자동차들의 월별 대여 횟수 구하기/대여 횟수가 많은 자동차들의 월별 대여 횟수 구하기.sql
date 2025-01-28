WITH FREQUENT_CARS AS (
    SELECT 
        CAR_ID
    FROM 
        CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE 
        START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
    GROUP BY 
        CAR_ID
    HAVING 
        COUNT(*) >= 5
),
MONTHLY_RENTALS AS (
    SELECT
        EXTRACT(MONTH FROM START_DATE) AS MONTH,
        CAR_ID,
        COUNT(*) AS RECORDS
    FROM
        CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE
        CAR_ID IN (
            SELECT
                CAR_ID
            FROM
                FREQUENT_CARS
        )
    AND
        START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
    GROUP BY
        EXTRACT(MONTH FROM START_DATE),
        CAR_ID
    HAVING
        COUNT(*) > 0
)
SELECT
    MONTH,
    CAR_ID,
    RECORDS
FROM
    MONTHLY_RENTALS
ORDER BY
    MONTH,
    CAR_ID DESC