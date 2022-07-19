-- Usamos la condicional donde comparamos el id encontrado en la consulta interna con el state_id que
-- la llave foranea.
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = "California") ORDER BY id ASC;
