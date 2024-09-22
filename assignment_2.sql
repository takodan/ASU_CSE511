CREATE TABLE query1 (
    name TEXT,
    moviecount INTEGER
);

INSERT INTO query1 (name, moviecount)
SELECT g.name, COUNT(h.movieid)
FROM genres g
JOIN hasagenre h ON g.genreid = h.genreid
GROUP BY g.genreid;


SELECT * FROM query1;


CREATE TABLE query2 (
    name TEXT,
    rating NUMERIC
);

INSERT INTO query2 (name, rating)
SELECT g.name, AVG(r.rating)
FROM genres g
JOIN hasagenre h ON g.genreid = h.genreid
JOIN ratings r ON h.movieid = r.movieid
GROUP BY g.genreid;

SELECT * FROM query2;


CREATE TABLE query3 (
    title TEXT,
    CountOfRatings INTEGER
);

INSERT INTO query3 (title, CountOfRatings)
SELECT m.title, COUNT(r.rating)
FROM movies m
JOIN ratings r ON m.movieid = r.movieid
GROUP BY m.title
HAVING COUNT(r.rating) >= 10;

SELECT * FROM query3;


CREATE TABLE query4 (
    movieid INTEGER,
    title TEXT
);

INSERT INTO query4 (movieid, title)
SELECT m.movieid, m.title
FROM movies m
JOIN hasagenre h ON m.movieid = h.movieid
JOIN genres g ON h.genreid = g.genreid
WHERE g.name = 'Comedy';

SELECT * FROM query4;

CREATE TABLE query5 (
    title TEXT,
    average NUMERIC
);


INSERT INTO query5 (title, average)
SELECT m.title, AVG(r.rating)
FROM movies m
JOIN ratings r ON m.movieid = r.movieid
GROUP BY m.title;

SELECT * FROM query5;


CREATE TABLE query6 (
    average NUMERIC
);

INSERT INTO query6 (average)
SELECT AVG(r.rating)
FROM movies m
JOIN hasagenre h ON m.movieid = h.movieid
JOIN genres g ON h.genreid = g.genreid
JOIN ratings r ON m.movieid = r.movieid
WHERE g.name = 'Comedy';

SELECT * FROM query6;

CREATE TABLE query7 (
    average NUMERIC
);


INSERT INTO query7 (average)
SELECT AVG(r.rating)
FROM movies m
JOIN ratings r ON m.movieid = r.movieid
WHERE m.movieid IN (
    -- IN Comedy movies
    SELECT m.movieid
    FROM movies m
    JOIN hasagenre h ON m.movieid = h.movieid
    JOIN genres g ON h.genreid = g.genreid
    WHERE g.name = 'Comedy'
)
AND m.movieid IN (
    -- IN Romance movies
    SELECT m.movieid
    FROM movies m
    JOIN hasagenre h ON m.movieid = h.movieid
    JOIN genres g ON h.genreid = g.genreid
    WHERE g.name = 'Romance'
);


SELECT * FROM query7;


CREATE TABLE query8 (
    average NUMERIC
);


INSERT INTO query8 (average)
SELECT AVG(r.rating)
FROM movies m
JOIN ratings r ON m.movieid = r.movieid
WHERE m.movieid IN (
    -- IN Romance movies
    SELECT m.movieid
    FROM movies m
    JOIN hasagenre h ON m.movieid = h.movieid
    JOIN genres g ON h.genreid = g.genreid
    WHERE g.name = 'Romance'
)
AND m.movieid NOT IN (
    -- NOT IN Comedy movies
    SELECT m.movieid
    FROM movies m
    JOIN hasagenre h ON m.movieid = h.movieid
    JOIN genres g ON h.genreid = g.genreid
    WHERE g.name = 'Comedy'
);

SELECT * FROM query8;

CREATE TABLE query9 (
    movieid INTEGER,
    rating NUMERIC
);

INSERT INTO query9 (movieid, rating)
SELECT r.movieid, r.rating
FROM ratings r
WHERE r.userid = :v1;

SELECT * FROM query9;