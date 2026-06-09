SELECT
  *,
  IIF(
    (
      age > 55
      OR country_code = 'CA'
    ),
    10,
    0
  ) AS discount_percent
FROM
  users;
