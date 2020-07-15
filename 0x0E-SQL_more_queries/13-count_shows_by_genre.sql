-- list all shows contained in hbtn_0d_tshows
SELECT tv_g.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres AS tv_g 
LEFT JOIN tv_show_genres AS tv_s ON tv_g.id = tv_s.genre_id 
GROUP BY genre
ORDER BY number_of_shows DESC;

