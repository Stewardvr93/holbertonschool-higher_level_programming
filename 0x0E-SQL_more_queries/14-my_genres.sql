-- Usamos dos left join para poder traer los datos correspondientes.
SELECT genero.name FROM tv_genres AS genero LEFT JOIN tv_show_genres AS tv ON genero.id = tv.genre_id LEFT JOIN tv_shows AS tvt ON tv.show_id = tvt.id WHERE tvt.title = 'Dexter' GROUP BY name ORDER BY name ASC;
