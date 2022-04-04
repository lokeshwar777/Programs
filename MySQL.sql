create table empl
(name varchar(10) not null primary key, 
designation varchar(20), 
salary int(5) default(50000), 
id int(10) not null unique, 
no_of_working_days int(3) not null);
