-- list all records with a name valid
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY DESC
