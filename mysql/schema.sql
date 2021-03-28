-- This file is used to create target database
-- Target database: dash_db

create database kpmg default character set utf8 collate utf8_general_ci;

use kpmg;

CREATE TABLE IF NOT EXISTS wordCount (
words VARCHAR(255),
count VARCHAR(255)
);

