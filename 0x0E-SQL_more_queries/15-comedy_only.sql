-- This script displays all tv shows whose genre are considered Comedy
-- Just like 14-my_genres.sql, this script requires the genre name, show name, and their ids, so multiple joins
-- are necessary

SELECT tv_shows.title
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
