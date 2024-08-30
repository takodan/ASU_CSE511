CREATE TABLE users ( 
    userid INTEGER,
    name TEXT,
    PRIMARY KEY (userid)
);

CREATE TABLE movies ( 
    movieid INTEGER,
    title TEXT,
    PRIMARY KEY (movieid)
);

CREATE TABLE taginfo ( 
    tagid INTEGER,
    content TEXT,
    PRIMARY KEY (tagid)
);

CREATE TABLE genres ( 
    genreid INTEGER,
    name TEXT,
    PRIMARY KEY (genreid)
);

CREATE TABLE ratings ( 
    userid INTEGER,
    movieid INTEGER,
    rating NUMERIC CONSTRAINT rating_five CHECK (rating > 0 AND rating < 6),
    timestamp BIGINT,
    PRIMARY KEY (userid, movieid),
    FOREIGN KEY (userid) REFERENCES users (userid),
    FOREIGN KEY (movieid) REFERENCES movies (movieid)
);

CREATE TABLE tags ( 
    userid INTEGER,
    movieid INTEGER,
    tagid INTEGER,
    timestamp BIGINT,
    PRIMARY KEY (userid, movieid, tagid),
    FOREIGN KEY (userid) REFERENCES users (userid),
    FOREIGN KEY (movieid) REFERENCES movies (movieid),
    FOREIGN KEY (tagid) REFERENCES taginfo (tagid)
);

CREATE TABLE hasagenre ( 
    movieid INTEGER,
    genreid INTEGER,
    PRIMARY KEY (movieid, genreid),
    FOREIGN KEY (movieid) REFERENCES movies (movieid),
    FOREIGN KEY (genreid) REFERENCES genres (genreid)
);


-- \copy hasagenre FROM '.\assignment1_example\hasagenre.dat' WITH (FORMAT csv, DELIMITER '%');
-- SELECT * FROM users LIMIT 6;
