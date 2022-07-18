-- Muestra la temperatura por ciudad  ordenadad por la misma.
SELECT city, AVG(value) AS 'avg_temp' FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
