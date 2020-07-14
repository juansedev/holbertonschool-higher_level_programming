-- list all shows contained in hbtn_0d_tshows
SELECT tv_s.title, tv_g.genre_id FROM tv_shows AS tv_s
LEFT JOIN tv_show_genres AS tv_g
ON tv_g.show_id = tv_s.id
ORDER BY tv_s.title ASC, tv_g.genre_id ASC;
