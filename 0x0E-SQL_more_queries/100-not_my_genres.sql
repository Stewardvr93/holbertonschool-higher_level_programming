-- Usamos una consulta anidada para como condicional de la primera.
SELECT genero.name FROM tv_genres AS genero WHERE genero.name NOT IN (SELECT gen.name FROM tv_genres AS gen LEFT JOIN tv_show_genres AS uni ON uni.genre_id = gen.id LEFT JOIN tv_shows AS tv ON tv.id = uni.show_id WHERE tv.title = 'Dexter') GROUP BY name ORDER BY name ASC;
