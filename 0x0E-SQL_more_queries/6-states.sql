-- This script creates a table in the server
-- The id will be unique, will automatically increment, is a primary key, and will never be null
-- The line USE <database> is needed, as this task requires us to create the database and table in the same script
-- Otherwise, an error message will appear stating no database was found.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT UNIQUE AUTO_INCREMENT PRIMARY KEY NOT NULL,
    name VARCHAR(256) NOT NULL
);
