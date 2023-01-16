# Interacting with SQLite

```sh
# Create an empty table schema from a file
sqlite3 data.db < schema/label.sql
# Enter into SQLite interactive CLI
sqlite3 data.db 
```

```log
SQLite version 3.31.1 2020-01-27 19:55:54
Enter ".help" for usage hints.
sqlite> select * from label;
sqlite> insert into label values (1, 'test','test','test');
sqlite> select * from label;
1|test|test|test
```

## TODO:

Move the DB to /u01 when AD group permissions are approved.