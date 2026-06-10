SELECT
  users.name AS name,
  SUM(transactions.amount) AS transaction_sum,
  COUNT(transactions.was_successful) AS transaction_count
FROM
  users
  LEFT JOIN transactions ON users.id = transactions.user_id
GROUP BY
  users.id
ORDER BY
  transaction_sum DESC;
