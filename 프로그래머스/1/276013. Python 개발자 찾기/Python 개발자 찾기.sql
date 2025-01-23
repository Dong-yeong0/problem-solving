SELECT
	ID,
    EMAIL,
    FIRST_NAME,
    LAST_NAME
FROM
	DEVELOPER_INFOS
WHERE
	(
    	LOWER(SKILL_1) = 'python'
        OR LOWER(SKILL_2) = 'python'
        OR LOWER(SKILL_3) = 'python'
    )
ORDER BY
	ID