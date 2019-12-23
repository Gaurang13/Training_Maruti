create database inventory;

create table inventory_data(inventory_id int NOT NULL AUTO_INCREMENT PRIMARY KEY ,Name varchar(30) NOT NULL,Category varchar(30) NOT NULL,expire_time date NOT NULL,Quantity varchar(3) NOT NULL,manufacturing_date date NOT NULL);