drop table if exists label;
create table label (
    id INTEGER PRIMARY KEY AUTOINCREMENT
    , created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    , commentText TEXT 
    , labelML TEXT
    , labelUser TEXT
);