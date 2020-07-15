-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT DISTINCT tv_ge.name
FROM tv_shows AS tv_s
INNER JOIN tv_show_genres AS tv_g ON tv_s.id = tv_g.show_id 
INNER JOIN tv_genres AS tv_ge ON tv_ge.id = tv_g.genre_id 
WHERE tv_s.title="Dexter" ORDER BY name;
