-- SELECT users.username
-- FROM users
-- WHERE users.username = 'Thalia';


-- SELECT users.id
-- FROM users 
-- WHERE users.id == '5';

SELECT *
FROM lore, champion
WHERE champion.id = lore.champion_id
AND champion.name = 'Nasus';