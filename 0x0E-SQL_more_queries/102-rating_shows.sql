-- Con sum hacemos la suma de clasificacion.
SELECT tv.title, SUM(rat.rate) AS rating FROM tv_shows AS tv LEFT JOIN tv_show_ratings AS rat ON rat.show_id = tv.id GROUP BY tv.title ORDER BY rating DESC;
