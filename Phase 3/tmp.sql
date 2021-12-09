-- SELECT users.username
-- FROM users
-- WHERE users.username = 'Thalia';


-- SELECT users.id
-- FROM users 
-- WHERE users.id == '5';

-- SELECT *
-- FROM lore, champion
-- WHERE champion.id = lore.champion_id
-- AND champion.name = 'Nasus';

-- SELECT DISTINCT champion.name
-- FROM champion, role, champRole
-- WHERE champion.id = champRole.champion_id
-- AND role.id = champRole.role_id
-- AND champion.price IN()
-- AND role.name IN('Top')
-- AND champion.dmgType IN('ad');

SELECT champion.name
FROM champion, role, champRole
WHERE champion.id = champRole.champion_id
AND role.id = champRole.role_id