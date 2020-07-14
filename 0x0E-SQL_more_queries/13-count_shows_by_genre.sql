-- list all shows contained in hbtn_0d_tshows
SELECT tv_g.name, COUNT(*) AS c 
FROM tv_genres AS tv_g 
LEFT JOIN tv_show_genres AS tv_s ON tv_g.id = tv_s.genre_id 
GROUP BY tv_g.name
ORDER BY c DESC;

