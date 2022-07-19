-- Me dio pereza poner apodos entonces simplemente traemos las coincidencias entre
-- las dos tablas con el ineer join y las ordernamos de forma ascendente.
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;