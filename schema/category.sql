drop table if exists category;
create table category (
    id INTEGER PRIMARY KEY AUTOINCREMENT
    , created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    , categoryText VARCHAR(100)
);