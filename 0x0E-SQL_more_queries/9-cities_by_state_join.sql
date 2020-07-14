-- Use the cartesian product to join two tables
SELECT c.id, c.name, s.name
FROM cities AS c
INNER JOIN states AS s
WHERE c.state_id = s.id
ORDER BY c.id;
