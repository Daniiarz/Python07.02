create table students2 (
    id integer PRIMARY KEY unique, name text, surname text, age integer,
     level integer,
     course_id integer, foreign key (course_id) references course(id));

create table course (
  id integer PRIMARY KEY unique, name text, direction text
);

insert into course values (1, 'GeekTech', 'Python');
insert into course values (2, 'GeekTech', 'FrontEnd');

insert into students2 values (1,'Kadyr', 'Umarov', 24,  2,1);
insert into students2 values (2, 'Sher', 'K', 27, 3, 2);
insert into students2 values (3, 'Vladimir', 'Putin', 60, 1, 1);
insert into students2 values (4, 'Adelya', 'Kojomuratova', 20, 1, 2);
insert into students2 values (5, 'Daniiar', 'm', 20, 2, 1);

select * from students2 where course_id = 2;
