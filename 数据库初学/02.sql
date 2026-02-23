
use class;
create table sanguo(
    id int primary key auto_increment,
    name varchar(30),
    sex char(1),
    country char(1),
    attack smallint,
    defense smallint);
insert into sanguo values
(1, '曹操', '男', '魏', 256, 63),
(2, '张辽', '男', '魏', 328, 69),
(3, '甄姬', '女', '魏', 168, 34),
(4, '夏侯渊', '男', '魏', 366, 83),
(5, '刘备', '男', '蜀', 220, 59),
(6, '诸葛亮', '男', '蜀', 170, 54),
(7, '赵云', '男', '蜀', 377, 66),
(8, '张飞', '男', '蜀', 370, 80),
(9, '孙尚香', '女', '蜀', 249, 62),
(10, '大乔', '女', '吴', 190, 44),
(11, '小乔', '女', '吴', 188, 39),
(12, '周瑜', '男', '吴', 303, 60),
(13, '吕蒙', '男', '吴', 330, 71);

select avg(attack) from sanguo;
select max(attack) from sanguo;
select min(attack) from sanguo;
select count(id) from sanguo;
select sum(attack) from sanguo;

select country,avg(attack) from sanguo group by country;
select country as 国家,sex as 性别,avg(attack) as 平均攻击力 from sanguo group by country,sex;
select country,count(id) from sanguo where sex='男' group by country order by count(id) desc limit 2;

select country,count(id) from sanguo group by country having avg(attack)>255;


create table index_test(
    id int,
    name varchar(30),
    sex char(1),
    index index_sex(sex),
    unique unique_name(name),
    primary key(id)
);
desc index_test;
show index from index_test;
drop index index_sex on index_test;
alter table index_test drop primary key ;

create table users(
    user_id int primary key  auto_increment,
    username varchar(50) not null ,
    email varchar(100) not null
);
create table user_profiles(
    profile_id int primary key  auto_increment,
    full_name varchar(100),
    phone varchar(20),
    address text,
    user_id int ,
    foreign key (user_id) references users(user_id)
);
INSERT INTO users (username, email) VALUES
('张三', 'zhangsan@email.com'),
('李四', 'lisi@email.com'),
('王五', 'wangwu@email.com'),
('赵六', 'zhaoliu@email.com'),
('钱七', 'qianqi@email.com'),
('孙八', 'sunba@email.com'),
('周九', 'zhoujiu@email.com'),
('吴十', 'wushi@email.com');
INSERT INTO user_profiles (full_name, phone, address, user_id) VALUES
('张三丰', '13800138001', '北京市朝阳区三里屯街道1号', 1),
('李四海', '13800138002', '上海市浦东新区陆家嘴金融中心2号', 2),
('王五洋', '13800138003', '广州市天河区珠江新城CBD核心区3号', 3),
('赵六顺', '13800138004', '深圳市南山区科技园高新技术产业园4号', 4),
('钱七宝', '13800138005', '杭州市西湖区文三路互联网创业大厦5号', 5),
('孙八方', '13800138006', '成都市高新区天府软件园6号楼', 6),
('周九州', '13800138007', '武汉市洪山区光谷步行街7号', 7),
('吴十全', '13800138008', '西安市雁塔区高新技术开发区8号', 8);

delete from user_profiles where full_name='张三丰';
delete from users where username='张三';

select * from users,user_profiles where users.username='张三' and user_profiles.user_id=users.user_id;
select * from users inner join user_profiles on users.user_id=user_profiles.user_id;

select * from users left join user_profiles on users.user_id=user_profiles.user_id;
select * from users right join user_profiles on users.user_id=user_profiles.user_id;

create table person(
    id varchar(32) primary key ,
    name varchar(30),
    age int
);

create table car(
    id varchar(32) primary key ,
    brand varchar(30),
    price decimal(10,2),
    pid varchar(32),
    foreign key(pid) references person(id)
);

INSERT INTO person (id, name, age) VALUES
('1', '张三', 35),
('2', '李四', 42),
('3', '王五', 28),
('4', '赵六', 38),
('5', '钱七', 45),
('6', '孙八', 33),
('7', '周九', 29),
('8', '吴十', 41);

INSERT INTO car (id, brand, price, pid) VALUES
('1', '奔驰E300', 450000.00, '1'),
('2', '宝马X3', 380000.00, '1'),

('3', '奥迪A6', 420000.00, '2'),
('4', '保时捷911', 1200000.00, '2'),
('5', '特斯拉Model S', 780000.00, '2'),

('6', '丰田凯美瑞', 180000.00, '3'),

('7', '本田雅阁', 165000.00, '4'),
('8', '大众帕萨特', 195000.00, '4'),

('9', '法拉利488', 3500000.00, '5'),
('10', '兰博基尼Huracan', 2800000.00, '5'),
('11', '玛莎拉蒂Ghibli', 880000.00, '5'),
('12', '阿斯顿马丁DB11', 2200000.00, '5'),

('13', '比亚迪唐', 280000.00, '6'),

('14', '小鹏P7', 250000.00, '7'),
('15', '蔚来ES6', 360000.00, '7');

select  brand from person,car where person.name='张三' and car.pid=person.id;

select brand from person inner join car on person.id=car.pid where person.name='张三';

create table people(
    id int primary key auto_increment,
    name varchar(30),
    age tinyint not null ,
    country varchar(30) not null
);

create table sports(
    id int primary key auto_increment,
    sports varchar(30) not null
);

create table people_sports(
    id int primary key auto_increment,
    aid int not null ,
    sid int not null ,
    foreign key (aid) references people(id),
    foreign key (sid) references sports(id)
);


insert into people ( name, age, country)values
('张三',29,'中国'),
('李四',24,'中国'),
('王五',25,'中国'),
('赵六',28,'中国'),
('john smith',27,'usa'),
('jake',30,'uk'),
('maka',28,'usa'),
('cubi',24,'usa'),
('mise',26,'uk'),
('emma',29,'uk');

insert into sports (sports)values
('篮球'),
('足球'),
('网球'),
('游泳'),
('跑步'),
('羽毛球'),
('乒乓球'),
('高尔夫'),
('瑜伽'),
('健身'),
('滑雪'),
('攀岩');

insert into people_sports(aid, sid) VALUES
(1,1),(1,4),(1,5),
(2,1),(2,7),(2,2),
(3,3),(3,8),(3,6),
(4,8),(4,11),(4,12),
(5,1),(7,4),(5,11),
(6,4),(6,9),(6,3),
(7,3),(7,6),(7,9),
(8,5),(8,8),(8,10),
(9,6),(9,8),(9,11),
(10,1),(10,7),(10,9);

select * from people_sports;

select sports from people,sports,people_sports
where people.name='张三'
and people_sports.aid=people.id
and sports.id=people_sports.sid;

select sports from people
inner join people_sports on people.id = people_sports.aid
inner join sports on people_sports.sid = sports.id
where people.name='张三';

select name from people,sports,people_sports where sports='足球' and sports.id=people_sports.sid and people.id=people_sports.aid;

select name from sports
inner join people_sports ps on sports.id = ps.sid
inner join people p on ps.aid = p.id
where sports='足球';