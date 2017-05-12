CREATE OR REPLACE FUNCTION team(int) RETURNS int LANGUAGE SQL as
$$ select teamID from team where teamID = $1; $$;

DROP TABLE IF EXISTS Patient;
CREATE TABLE Patient (
Name varchar(255) not null,
pnum varchar(13),
gender int,
age int
);

DROP TABLE IF EXISTS InQueue;
create table InQueue (
patID int,
arrival timestamp not null default now(),
issue int,
prio int,
teamID int
);


DROP TABLE IF EXISTS Issue;
CREATE TABLE Issue (
id int primary key,
name varchar(255)
);

DROP TABLE IF EXISTS Team;
create table Team (
teamID int primary key
);

DROP TABLE IF EXISTS SpecIn;
create table SpecIn (
teamID int,
issue int
);


DROP TABLE IF EXISTS Drug;
create table Drug (
name varchar(255),
cost int
);


