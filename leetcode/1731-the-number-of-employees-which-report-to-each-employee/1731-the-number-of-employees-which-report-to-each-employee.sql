WITH reports AS (
    SELECT
        reports_to AS manager_id,
        COUNT(reports_to) AS reports_count,
        ROUND(AVG(age)) AS average_age
    FROM
        Employees
    GROUP BY
        1
)
SELECT
    e.employee_id,
    e.name,
    r.reports_count,
    r.average_age
FROM
    Employees e
JOIN
    reports r
ON
    e.employee_id = r.manager_id
ORDER BY
    e.employee_id
