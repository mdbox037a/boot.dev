SELECT
  *
FROM
  users
WHERE
  age_in_days > (
    SELECT
      40 * 365
  );
