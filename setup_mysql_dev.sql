-- create new database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- create new user
CREATE USER IF NOT EXISTS hbnb_dev@localhost IDENTIFIED BY 'hbnb_dev_pwd';

-- grant all priviledges to user
GRANT ALL ON hbnb_dev_db.* TO hbnb_dev@localhost;

-- grant select priviledge on performance schema
GRANT SELECT ON performance_schema.* TO hbnb_dev@localhost;
