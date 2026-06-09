SELECT
  *
FROM
  transactions
WHERE
  amount BETWEEN 10 AND 80
LIMIT
  4
ORDER BY
  amount DESC;
