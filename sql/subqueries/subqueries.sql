SELECT
  *
FROM
  transactions
WHERE
  user_id = (
    SELECT
      id
    FROM
      users
    WHERE
      name = 'David'
  );
