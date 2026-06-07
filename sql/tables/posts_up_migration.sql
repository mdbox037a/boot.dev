ALTER TABLE posts
RENAME COLUMN author_id TO poster_id;


ALTER TABLE posts
ADD COLUMN is_edited BOOLEAN;


ALTER TABLE posts
DROP COLUMN is_sponsored;
