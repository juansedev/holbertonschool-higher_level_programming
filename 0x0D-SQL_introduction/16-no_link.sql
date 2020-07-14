-- list all records with a name valid
SELECT score, name
FROM second_table
WHERE id IS NOT NULL
ORDER BY DESC
