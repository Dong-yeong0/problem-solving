WITH biggest_single_number AS (
    SELECT
        num
    FROM
        MyNumbers
    GROUP BY
        1
    HAVING
        COUNT(num) = 1
    ORDER BY
        1 DESC
)
SELECT
    MAX(bsn.num) as num
FROM
    biggest_single_number bsn