delete from issue;
delete from specin;
delete from team;
delete from drug;

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

insert into drug values (1, 'Aspirin', 100);
insert into drug values (2, 'Talidomid', 150);
insert into drug values (3, 'Aldomet', 90);
insert into drug values (4, 'Aldoril', 200);
insert into drug values (5, 'Aldurazyme', 3000);
insert into drug values (6, 'Alecensa', 30);
insert into drug values (7, 'Alectinib', 10);
insert into drug values (8, 'Alefacept', 10000);
insert into drug values (9, 'Alemtuzumab', 5);
insert into drug values (10 ,'Mebaral', 500);

insert into treatment values (1 , 'Treat 1 ', 100);
insert into treatment values (2 , 'Treat 2 ', 200);
insert into treatment values (3 , 'Treat 3 ', 300);
insert into treatment values (4 , 'Treat 4 ', 400);
insert into treatment values (5 , 'Treat 5 ', 500);
insert into treatment values (6 , 'Treat 6 ', 600);
insert into treatment values (7 , 'Treat 7 ', 700);
insert into treatment values (8 , 'Treat 8 ', 800);
insert into treatment values (9 , 'Treat 9 ', 900);
insert into treatment values (10 , 'Treat 10', 1000);
