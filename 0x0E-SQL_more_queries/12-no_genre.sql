-- This script displays all tv shows in the passed in database argument
-- This is the exact opposite to 10-genre_id_by_show.sql. Instead of displaying all shows and their genres,
-- display only shows with no genre
-- This is achieved simply by adding the where conditional

SELECT tv_shows.title, tv_show_genres.genre_id
from tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.show_id IS NULL
ORDER BY title, genre_id ASC;
