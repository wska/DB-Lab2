CREATE OR REPLACE FUNCTION team(int) RETURNS int LANGUAGE SQL as
$$ select teamID from team where teamID = $1; $$;

DROP TABLE IF EXISTS Patient CASCADE;
DROP TABLE IF EXISTS InQueue CASCADE;
DROP TABLE IF EXISTS Issue CASCADE;
DROP TABLE IF EXISTS Team CASCADE;
DROP TABLE IF EXISTS SpecIn CASCADE;
DROP TABLE IF EXISTS Drug CASCADE;
DROP TABLE IF EXISTS Treatment CASCADE;
DROP TABLE IF EXISTS PatientLog CASCADE;
DROP TABLE IF EXISTS usedDrug CASCADE;
DROP TABLE IF EXISTS usedTreatment CASCADE;

CREATE TABLE Patient (
Name varchar(255) not null,
pnum varchar(13) primary key,
gender varchar(1),
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
did int primary key,
name varchar(255),
cost int
);

CREATE TABLE Treatment (
tid int primary key,
name varchar(255),
cost int
);

CREATE TABLE PatientLog (
Name varchar(255) not null,
pnum varchar(13) primary key,
gender varchar(1),
age int,
arrival timestamp,
departure timestamp,
sentHome int
);

CREATE TABLE usedDrug (
did int references Drug(did),
patient varchar(13) references Patient(pnum)
);

CREATE TABLE usedTreatment (
tid int references Treatment(tid),
patient varchar(13) references Patient(pnum)
);




