-- script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT tv_genres.name
FROM tv_genres INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows ON tv_genres.show_id = tv_shows.id
WHERE tv_show_genres.show_id IS NOT (SELECT tv_shows.id FROM tv_shows WHERE tv_shows.name = "Dexter")
ORDER BY tv_genres.name ASC;
