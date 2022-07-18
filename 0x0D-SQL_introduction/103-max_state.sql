-- Muestra la temperatura maxima de cada estado ordenada por su nombre.
-- y en orden ascendente 
SELECT state, MAX(value) AS 'max_temp' FROM temperatures GROUP BY state ORDER BY state ASC;
