-- This file is used to set username and password when log into datasbase
-- Username: root
-- Password: 123456


use mysql;

select host, user from user;

GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '123456' WITH GRANT OPTION;

flush privileges;

SET @@global.sql_mode= '';
