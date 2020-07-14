-- Use the cartesian product to join two tables
SELECT c.id, c.name FROM cities AS c, states AS s
WHERE s.id = c.state_id AND s.name = "California"
ORDER BY c.id;
