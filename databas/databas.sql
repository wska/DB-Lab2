CREATE OR REPLACE FUNCTION team(int) RETURNS int LANGUAGE SQL as
$$ select teamID from team where teamID = $1; $$;

DROP TABLE IF EXISTS Patient CASCADE;
DROP TABLE IF EXISTS InQueue CASCADE;
DROP TABLE IF EXISTS Issue CASCADE;
DROP TABLE IF EXISTS Team CASCADE;
DROP TABLE IF EXISTS SpecIn CASCADE;
DROP TABLE IF EXISTS Drug CASCADE;

CREATE TABLE Patient (
Name varchar(255) not null,
pnum varchar(13) primary key,
gender int,
age int
);

CREATE TABLE Issue (
id int primary key,
name varchar(255)
);

CREATE TABLE Team (
teamID int primary key
);

CREATE TABLE InQueue (
patID varchar(13) references Patient(pnum),
arrival timestamp not null default now(),
issue int references Issue(id),
prio int,
teamID int references Team(teamID)
);

CREATE TABLE SpecIn (
teamID int references team(teamid),
issue int references issue(id)
);

CREATE TABLE Drug (
name varchar(255),
cost int
);


