-- This script displays all tv shows in the passed in database argument
-- This is similar to 9-cities_by_state_join.sql. The only difference is that this list is also ordered
-- by title, then genre_id

SELECT tv_shows.title, tv_show_genres.genre_id
from tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY title, genre_id ASC;
