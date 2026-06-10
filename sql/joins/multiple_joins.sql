SELECT
  users.id,
  users.name,
  users.age,
  users.username,
  countries.name AS country_name,
  SUM(transactions.amount) AS balance
FROM
  users
  INNER JOIN countries ON users.country_code = countries.country_code
  LEFT JOIN transactions ON users.id = transactions.user_id
WHERE
  users.id = 6
  AND transactions.was_successful = true;
