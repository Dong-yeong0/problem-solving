SELECT
    user_id,
    COUNT(DISTINCT follower_id) AS followers_count
FROM
    Followers
GROUP BY
    1
ORDER BY
    user_id