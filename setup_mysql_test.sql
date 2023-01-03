-- create new database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- create new user
CREATE USER IF NOT EXISTS hbnb_test@localhost IDENTIFIED BY 'hbnb_test_pwd';

-- grant all priviledges to user
GRANT ALL ON hbnb_test_db.* TO hbnb_test@localhost;

-- grant select priviledge on performance schema
GRANT SELECT ON performance_schema.* TO hbnb_test@localhost;
