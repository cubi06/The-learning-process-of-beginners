show databases;

create database class;

drop database if exists class;

use class;
create table stu(
    id int auto_increment primary key ,
    name varchar(50) not null unique ,
    age tinyint,
    sex char(1),
    score float default 0,
    city varchar(20) default '北京',
    birthday date
);
show tables ;
drop table stu;
desc stu;
show create table stu;

insert into stu values
(1,'张三',19,'男',77,'北京','2001-01-02'),
(2,'李四',18,'男',87,'成都','2001-01-09'),
(3,'王五',20,'男',87,'长沙','2001-06-01');

insert into stu(name,age,sex,score,city,birthday) values
('赵六',19,'男',70,'成都','2003-04-14'),
('小明',21,'男',68,'重庆','2003-06-24'),
('小红',20,'女',88,'杭州','2003-11-14');

insert into stu(name,age,score,city,birthday) values
('小帅',19,70,'成都','2003-09-14'),
('小浩',21,68,'重庆','2003-08-24'),
('小强',20,88,'杭州','2003-2-14');

select * from stu;
select name,sex from stu;
select * from stu where name='张三';
select * from stu where sex!='男';
select * from stu where score>70;
select * from stu where score between 75 and 90;
select * from stu where city in('北京','成都');
select * from stu where city not in('北京','成都');
select * from stu where sex is null;
select * from stu where sex is not null;
select * from stu where city='成都' and score>75;
select * from stu where city='成都' or score>75;

update stu set sex='男' where sex is null;
update stu set age=21,score=99 where name='小帅';

delete from stu where name='王五';

select * from stu where name like '小%';
select * from stu where name like '张__';

select name as 姓名 , sex as 性别 from stu;

select * from stu order by score;
select * from stu order by score desc ;

select * from stu order by score desc limit 2;
select * from stu order by score desc limit 2,2;

select * from stu where city in('北京','成都') union select * from stu where score between 75 and 90;
select * from stu where city in('北京','成都') union all select * from stu where score between 75 and 90;

select * from (select * from stu where score>80) as m where name like'小%';
select * from stu where city=(select city from stu where name='小帅');
select * from stu where city in (select city from stu where name='小帅' or name='张三');

