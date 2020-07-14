-- script that displays the average temperature
select city, AVG(value) as avg_temp from temperatures group by city order by avg_temp desc;
