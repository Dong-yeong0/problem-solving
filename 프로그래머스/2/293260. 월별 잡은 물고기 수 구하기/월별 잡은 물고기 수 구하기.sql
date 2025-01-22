SELECT
    COUNT(ID) AS FISH_COUNT,
    MONTH(TIME) AS MONTH
FROM
    FISH_INFO
GROUP BY
    MONTH(TIME)
HAVING
    COUNT(ID) IS NOT NULL
ORDER BY
    MONTH(TIME)