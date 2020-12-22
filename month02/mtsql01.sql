
练习1，创建爱好表格
create table hobby(id int primary key auto_increment,name varchar(30) not null,
hobby set('dance','sing','draw') comment "选择爱好",level char,
price decimal(7,2),remark text);

练习2 插入hobby数据
insert into hobby(name,hobby,level,price,remark)
values
('Lily','sing,dance','A',43800.88,"jksa"),
('Joshua','draw','A',888.888,"test"),
('Aiden','sing,dance,draw','B',5.5,'test');

练习3 创建一个数据库：books
在该数据库中创建一个数据表 book
字段：id 书名 作者 出版社 价格 备注
在该表中插入若干数据记录 >=8
作者：老舍 沈从文 鲁迅 冰心
出版社： 中国文学 人民教育 机械工业
价格30-120
--create database books charset=utf8;
--create table book(
--id int primary key auto_increment,
--name varchar(30) not null,
--author enum('老舍','沈从文','鲁迅','冰心'),
--press enum('中国文学出版社','人民教育出版社','机械工业出版社'),
--price decimal(4,1) unsigned default 0,
--remark text
--);


create database books charset=utf8;
use books;
create table book(
id int primary key auto_increment,
name varchar(50) not null,
author varchar(30) not null,
press varchar(50),
price decimal(4,1) unsigned default 0,
remark text
);

insert into book(name,author,press,price)values
("《骆驼祥子》","老舍","中国文学出版社",45),
("《韭菜的自我修养》","冰心","人民教育出版社",120),
("《这些话我未曾说过》","鲁迅","中国文学出版社",99),
("《花手修炼手册》","沈从文","机械工业出版社",100),
("《一给我里giaogiao》","冰心","机械工业出版社",77),
("《葵花宝典》","老舍","中国文学出版社",30),
("《想不出书名了》","老舍","机械工业出版社",45),
("《骆驼祥子》","老舍","中国文学出版社",45),
("《取名字真难》","冰心","中国文学出版社",66);

# 数据库查询
select name,score from class;
select score,name from class; # 先看score，再看name
select * from class where score>80;
select * from class where age%2=0;
select * from class where age>18;
select * from class where 80>score>70; # 没有支持这种写法
select * from class where score between 70 and 80;
select * from class where score>80 and score<90;
select * from class where score in (90,89);
select * from class where sex=null; # 不可以
select * from class where sex is null;


# homework
# 查找30多元的图书
select * from book where price>30 and price<=40;
# 查找人民教育出版社的图书
select * from book where press='人民教育出版社';
# 查找老舍写的，中国文学出版社出版的图书
select * from book where author='老舍' and press='中国文学出版社';
# 查找备注不为空的图书
select * from book where remark is not null;
# 查找价格超过60，只显示名字，价格
select name,price from book where price>60;
# 查找鲁迅写的，或者矛盾写的书
select * from book where author ="鲁迅" or author="茅盾";
select * from book where author in ('鲁迅','茅盾')

- 更新表记录update
update class set score=89 where name ='Alex';
# 将性别为null的改为o
update class set sex='o' where sex is null;  # 要注意null不能用等于。
update class set sex='o' where sex = 'f';
# 普改
update class set age=age-1;

- 删除表记录delete
delete from class where name = 'Abby';

- 表字段的操作(alter)
alter table hobby add phone char(11) after price; # 增加字段
alter table hobby drop level; # 删除字段
alter table hobby modify price float; # 修改字段数据类型
alter table hobby change phone telephone char(16); # 修改字段名（要加上数据类型）
alter table class rename cls;


# 马拉松表
create table marathon(id int primary key auto_increment,athlete varchar(30),birthday date,registration datetime,performance time);
insert into marathon values(1,"小阿giao",'1990-10-1','2020-12-3 11:22:00','2:56:49');
insert into marathon (athlete,birthday,registration,performance) values('郭氏','1988-2-31','2020-12-3 10:22:22','5:23:55');
# 报错 检查了日期，2月没有31号
insert into marathon (athlete,birthday,registration,performance) values('郭氏','1988-2-29','2020-12-3 10:22:22','5:23:55');

select athlete,performance from marathon where performance between '02:00:00' and '03:00:00';
alter table marathon modify registration datetime default now();
insert into marathon (athlete,birthday,performance) values('曹操','2020-8-23','5:23:55');
insert into marathon (athlete,birthday,performance) values('奥特曼','2021-1-19','5:23:55');

# 练习
练习 使用book表
1. 将呐喊的价格修改为45元
update book set price = '30' where name = '呐喊';
2. 增加一个字段出版时间 类型为 date 放在价格后面
alter table book add publish_time date after price;
3. 修改所有老舍的作品出版时间为 2018-10-1
update book set publish_time = '2018-10-01' where author = '老舍';
4. 修改所有中国文学出版社出版的但是不是老舍的作品出版时间为 2020-1-1
update book set publish_time = '2020-1-1' where author != '老舍' and press = '中国文学出版社';
5. 修改所有出版时间为Null的图书 出版时间为 2019-10-1
update book set publish_time = '2019-10-1' where publish_time is null;
6. 所有鲁迅的图书价格增加5元
update book set price = price +1 where author ='鲁迅';
7. 删除所有价格超过70元或者不到40元的图书
delete from book where price>70 or price <40;
# 或者
delete from book where price not between 40 and 70;


模糊查询
select * from class where name like'J%';  # J开头的
select * from class where name like'%a%'; # 不区分字母大小写
select * from class where name like'___'; # 找有三个字符的
select name,hobby from hobby where hobby like '%sing%';# 集合查询

as 用法 -> 可以用于重命名
select name as 姓名,age as 年龄 from class;
select name as 姓名,age as 年龄 from class where 年龄>19; # 会报错
as也可以去掉，新的版本支持。

order by 排序
select * from class where sex='m' order by score desc;
select * from class oder by score desc,age desc; # score 和 age 都是降序排序
select * from class oder by score desc,age; # age 降序

limit
select * from class limit 3;
update class set sex = 'o' where sex = 'f' limit 2;
# 查询班级男生成绩前三名
select * class  where sex = 'm' order by score desc limit 3;
# 查询班级男生成绩第三名
select * class  where sex = 'm' order by score desc limit 3 offset 2;

Union 联合查询
select * from class where score>80 union select * from class where sex = 'f';
select * from class where score>80 union all select * from class where sex = 'f';
# union
select name,sex,score from class union select name,hobby,telephone from hobby;
# 子查询（嵌套查询）
select name,age from (select * from class where sex='m') as men where score > 80;
# 查询分数比tony分数高的同学信息;
select * from class where score > (select score from class where name = 'Tony');


高级查询练习

在stu下创建数据报表 sanguo

字段：id  name  gender  country  attack  defense

create table sanguo(
id int primary key auto_increment,
name varchar(30),
gender enum('男','女'),
country enum('魏','蜀','吴'),
attack smallint,
defense tinyint
);


insert into sanguo
values (1, '曹操', '男', '魏', 256, 63),
       (2, '张辽', '男', '魏', 328, 69),
       (3, '甄姬', '女', '魏', 168, 34),
       (4, '夏侯渊', '男', '魏', 366, 83),
       (5de, '刘备', '男', '蜀', 220, 59),
       (6, '诸葛亮', '男', '蜀', 170, 54),
       (7, '赵云', '男', '蜀', 377, 66),
       (8, '张飞', '男', '蜀', 370, 80),
       (9, '孙尚香', '女', '蜀', 249, 62),
       (10, '大乔', '女', '吴', 190, 44),
       (11, '小乔', '女', '吴', 188, 39),
       (12, '周瑜', '男', '吴', 303, 60),
       (13, '吕蒙', '男', '吴', 330, 71);

查找练习
1. 查找所有蜀国人信息，按照攻击力排名
select * from sanguo where country='蜀' order by attack;
2. 将赵云攻击力设置为360，防御设置为70
update sanguo set attack = 360, defense =70 where name = '赵云';
3. 吴国英雄攻击力超过300的改为300，最多改2个
update sanguo set attack = 300 where attack >300 and country = '吴' limit 2;
4. 查找攻击力超过200的魏国英雄名字和攻击力并显示为姓名， 攻击力
select name,attack from sanguo where country = '魏' and attack >200;
5. 所有英雄按照攻击力降序排序，如果相同则按照防御生序排序
select * from sanguo order by attack desc,defense;
6. 查找名字为3字的
select * from sanguo where name like '___';
7. 查找攻击力比魏国最高攻击力的人还要高的蜀国英雄
select * from sanguo where country = '蜀' and
attack > (select attack from sanguo where country = '魏' order by attack desc limit 1);
8. 找到魏国防御力排名2-3名的英雄
select * from sanguo where country = '魏' order by defense desc limit 2 offset 1;
9. 查找所有女性角色中攻击力大于180的和男性中攻击力小于250的
select * from sanguo where gender = '女' and attack > 180 union select * from sanguo where gender = '男' and attack <250;

# 聚合函数
select avg(attack) from sanguo where country = '蜀';
select max(attack),name from sanguo where country ='魏';# 用了聚合函数不可以加字段名了，除了这个字段的值全都一样。
select country,max(attack) from sanguo where country =' 魏';
# 可以写 多个聚合函数
select country,min(attack),max(attack),sum(attack),count(attack),avg(attack) from sanguo where country ='魏';
# group by
select country from sanguo group by country; # 魏蜀吴
select country,count(*) from sanguo group by country;
select country,count(*),avg(attack),max(defense) from sanguo group by country;
select country,gender,count(*) from sanguo group by country,gender;
# 男英雄数量最多的国家
select country,count(*) from sanguo where gender = '男' group by country,gender order by count(*) desc limit 1;
# 男英雄数量最多的国家
select country,count(*) from sanguo where gender ='男' group by country order by count(*) desc limit 1;
# 筛选出最大攻击力大于350 的国家和攻击力
select country,max(attack) from sanguo group by country having max(attack)>350;
# distinct
select distinct country from sanguo
select count(distinct country) from sanguo;
select name,attack*2 from sanguo; # 简单的聚合运算


聚合练习

1. 统计每位作家出版图书的平均价格
select author,avg(price) from book group by author;
2. 统计每个出版社出版图书数量
select press,count(*) from book group by press;
3. 查看总共有多少个出版社
select count(distinct press) from book;
4. 筛选出那些出版过超过50元图书的出版社，并按照其出版图书的平均价格降序排序
# 方法一
select press,avg(price)
from book
where press in (select press from book where price > 50 group by press)
group by press
order by avg(price) desc;
# 方法二
select press,avg(price)
from book
group by press
having max(price)>50
order by avg(price) desc;
5. 统计同一时间出版图书的最高价格和最低价格
select publish_time,max(price),min(price) from book group by publish_time;

