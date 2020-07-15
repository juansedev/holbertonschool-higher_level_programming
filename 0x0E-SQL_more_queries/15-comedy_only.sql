-- script that uses the hbtn_0d_tvshows database to lists all shows
SELECT tv_s.title AS title
FROM tv_shows AS tv_s
INNER JOIN tv_show_genres AS tv_g ON tv_s.id = tv_g.show_id 
INNER JOIN tv_genres AS tv_ge ON tv_ge.id = tv_g.genre_id 
WHERE tv_ge.name="Comedy" 
ORDER BY title;
