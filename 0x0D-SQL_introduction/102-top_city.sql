-- Muestra la temperatu de las 3 ciudades top durante julio y agosto. donde
-- limitamos el resultado a 3.
SELECT city, AVG(value) AS 'avg_temp' FROM temperatures WHERE month IN (7, 8) GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
