-- script that uses the hbtn_0d_tvshows database to lists all shows
SELECT tv_s.title AS title, tv_ge.name AS name
FROM tv_shows AS tv_s
LEFT JOIN tv_show_genres AS tv_g ON tv_s.id = tv_g.show_id 
LEFT JOIN tv_genres AS tv_ge ON tv_ge.id = tv_g.genre_id 
ORDER BY title ASC, name ASC;

