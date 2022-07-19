-- Lo mismo que en el ejercicio pasado solo que con left join con la cual
-- mostramos null si no hya coincidencia entre tablas
SELECT tv.title, genero.genre_id FROM tv_shows AS tv LEFT JOIN tv_show_genres AS genero ON tv.id = genero.show_id ORDER BY tv.title, genero.genre_id ASC;
