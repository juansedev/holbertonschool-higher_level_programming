-- coment
SELECT tv_s.title, SUM(tv_sr.rate) rating 
FROM tv_shows tv_s 
INNER JOIN tv_show_ratings tv_sr ON tv_s.id = tv_sr.show_id 
GROUP BY tv_s.title 
ORDER BY rating DESC;
