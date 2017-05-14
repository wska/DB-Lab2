insert into patient values('asdf1', 1 ,1 ,2);
insert into patient values('asdf2', 2 ,1 ,5);
insert into patient values('asdf3', 3 ,2 ,6);
insert into patient values('asdf4', 4 ,2 ,7);
insert into patient values('asdf5', 5 ,1 ,8);
insert into patient values('asdf6', 6 ,1 ,9);
insert into patient values('asdf7', 7 ,1 ,10);
insert into patient values('asdf8', 8 ,1 ,11);

insert into inQueue values(1, now(), 1, 2, 1); 
insert into inQueue values(2, now(), 1, 4, 1); 
insert into inQueue values(3, now(), 1, 4, 3); 
insert into inQueue values(4, now(), 1, 5, 1); 
insert into inQueue values(5, now(), 1, 3, 2); 
insert into inQueue values(6, now(), 1, 5, 1); 
insert into inQueue values(7, now(), 2, 5, 2);
insert into inQueue values(8, now(), 2, 3, 1);

insert into issue values (1, 'fracture');
insert into issue values (2, 'impact trauma');
insert into issue values (3, 'chest pains');
insert into issue values (4, 'seizures');
insert into issue values (5, 'allergic reaction');
insert into issue values (6, 'cold');
insert into issue values (7, 'head ache');
insert into issue values (8, 'burn damage');
insert into issue values (9, 'cancer');
insert into issue values (10, 'dead');

insert into team values (1);
insert into team values (2);
insert into team values (3);
insert into team values (4);
insert into team values (5);

insert into SpecIn values (1, 1);
insert into SpecIn values (1, 2);
insert into SpecIn values (1, 3);

insert into SpecIn values (2, 5);
insert into SpecIn values (2, 6);
insert into SpecIn values (2, 7);

insert into SpecIn values (3, 4);
insert into SpecIn values (3, 5);
insert into SpecIn values (3, 8);

insert into SpecIn values (4, 1);
insert into SpecIn values (4, 7);
insert into SpecIn values (4, 8);

insert into SpecIn values (5, 9);
insert into SpecIn values (5, 10);
insert into SpecIn values (5, 4);

