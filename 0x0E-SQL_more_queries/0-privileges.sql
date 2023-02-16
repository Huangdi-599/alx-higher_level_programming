-- This script lists all privileges user_0d_1 and user_0d_2 has
-- If localhost is not included, the error message will occur as the script attempts to access the % database(?)

SHOW GRANTS IF NOT EXISTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS IF NOT EXISTS FOR 'user_0d_2'@'localhost';
