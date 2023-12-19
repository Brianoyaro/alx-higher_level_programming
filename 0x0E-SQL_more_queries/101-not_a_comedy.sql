-- script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT tv_show.title
FROM tv_genres INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows ON tv_genres.show_id = tv_shows.id
WHERE tv_show_genres.genre_id != (SELECT tv_genres.name FROM tv_genres WHERE tv_genres.name = "Comedy")
GROUP BY tv_show_genres.genre_id
ORDER BY tv_genres.name ASC;
