-- Con el right asumes que las coincidencias esta en la segunda tabla.
SELECT genero.name AS genre, COUNT(tv.genre_id) AS number_of_shows FROM tv_genres AS genero RIGHT JOIN tv_show_genres AS tv ON genero.id = tv.genre_id GROUP BY genre ORDER BY number_of_shows DESC;
