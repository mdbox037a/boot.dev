SELECT
  MAX(age) AS age
FROM
  users
WHERE
  is_admin IS true;
