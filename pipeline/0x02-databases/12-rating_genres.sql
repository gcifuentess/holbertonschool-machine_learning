-- comment

SELECT tv_genres.name, SUM(tv_show_ratings.rate) AS rating FROM tv_genres RIGHT JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id LEFT JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_show_genres.show_id GROUP BY tv_genres.name ORDER BY rating DESC;
