-- Enumera todos los registro de la tabla second.
-- sin contar con los name que no contengan un valor.
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
