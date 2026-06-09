SELECT
  user_id,
  SUM(amount) AS balance
FROM
  transactions
WHERE
  was_successful IS true
GROUP BY
  user_id;
