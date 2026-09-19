WITH daily AS (
    SELECT visited_on, SUM(amount) AS day_amount
    FROM Customer
    GROUP BY visited_on
),
rolling AS (
    SELECT visited_on,
           SUM(day_amount) OVER w AS amount,
           ROUND(AVG(day_amount) OVER w, 2) AS average_amount
    FROM daily
    WINDOW w AS (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW)
)
SELECT visited_on, amount, average_amount
FROM rolling
WHERE visited_on >= (SELECT MIN(visited_on) + INTERVAL 6 DAY FROM daily)
ORDER BY visited_on;
