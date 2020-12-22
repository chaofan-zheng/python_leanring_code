## 索引



- 创建表的时候同时创建索引

```mysql
create table index_test(id int auto_increment,name varchar(30),primary key(id),index Name(name));
```

- 在已有表中创建索引

  ```mysql
  create unique index indexName on class(name);
      # 主键添加索引有一些不一样
      alter table class add primary key(id);
  ```

```mysql
# 查看索引
desc class;
show index from class;
# 删除索引
drop index name on index_test;
```

使用程序插入200万

```mysql
# 运行insert_data.py
select * from index_test;
select * from index_test where name='Tom123456';
set profiling =1; 
show profiles;
set profiling=0;
show index from index_test;  # 查看索引名
drop index Name on index_test;
select * from index_test where name='Tom123456';
show profiles;
set profiling =0;
```

员工部门

```
insert into dept values(1,'技术部'),(2,'教学部'),(3,'财务部'); 
insert into person values(1,'小阿giao',22,'m',1000,'2020-12-20',2),(2,'小刚',21,'w',5000,'2020-10-21',2),(3,'润玉大肥龙',22,'w',1000,'2020-11-20',1),(4,'东北酱',22,'m',1000,'2020-11-20',3);
```

## 外键约束

- 创建表之间添加外键

  ```mysql
  CREATE TABLE person ( 
      id int PRIMARY KEY AUTO_INCREMENT,  
      name varchar(32) NOT NULL, 
      age tinyint DEFAULT 0, 
      sex enum('m','w','o') DEFAULT 'o',  
      salary decimal(8,2) DEFAULT 250.00,  
      hire_date date NOT NULL, 
      dept_id int),
      constraint dept_fk foreign key(dept_id) references dept(id);
  ```

  

- 建立表后增加外键

  ```mysql
  alter table person add constraint dept_fk foreign key(dept_id) references dept(id);
  ```

- 通过外键名称解除外键约束（删除外键）

  ```mysql
  alter table person drop foreign key dept_fk; # 这样索引不会彻底删除 需要手动删除索引
  # 索引名称一般与外键名称相同
  drop index dept_fk on person;
  ```

- 查看外键名称和索引名称

  ```mysql
  # 查看外键名称
  show create table person;
  # 查看索引名称
  desc person;
  show index from person;
  ```

- 级联动作

  - cascade

  ```mysql
  # 先删除
  alter table person drop foreign key dept_fk;
  # 原先的
  | person | CREATE TABLE `person` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `name` varchar(32) NOT NULL,
    `age` tinyint(4) DEFAULT '0',
    `sex` enum('m','w','o') DEFAULT 'o',
    `salary` decimal(8,2) DEFAULT '250.00',
    `hire_date` date NOT NULL,
    `dept_id` int(11) DEFAULT NULL,
    PRIMARY KEY (`id`),
    KEY `dept_fk` (`dept_id`),
    CONSTRAINT `dept_fk` FOREIGN KEY (`dept_id`) REFERENCES `dept` (`id`)
  ) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 |
  # 后面的
  | person | CREATE TABLE `person` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `name` varchar(32) NOT NULL,
    `age` tinyint(4) DEFAULT '0',
    `sex` enum('m','w','o') DEFAULT 'o',
    `salary` decimal(8,2) DEFAULT '250.00',
    `hire_date` date NOT NULL,
    `dept_id` int(11) DEFAULT NULL,
    PRIMARY KEY (`id`),
    KEY `dept_fk` (`dept_id`)
  ) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 |
  # 然后加上
  alter table person add foreign key(dept_id) references dept(id) on delete cascade on update cascade;
  show create table person;、
  
  update dept set id = 7 where id =3;# 两个表会一起改
  
  mysql> select * from dept;
  +----+-----------+
  | id | dname     |
  +----+-----------+
  |  1 | 技术部    |
  |  2 | 教学部    |
  |  7 | 财务部    |
  +----+-----------+
  3 rows in set (0.00 sec)
  
  mysql> select * from person;
  +----+-----------------+------+------+---------+------------+---------+
  | id | name            | age  | sex  | salary  | hire_date  | dept_id |
  +----+-----------------+------+------+---------+------------+---------+
  |  1 | 小阿giao        |   22 | m    | 1000.00 | 2020-12-20 |       2 |
  |  2 | 小刚            |   21 | w    | 5000.00 | 2020-10-21 |       2 |
  |  3 | 润玉大肥龙      |   22 | w    | 1000.00 | 2020-11-20 |       1 |
  |  4 | 东北酱          |   22 | m    | 1000.00 | 2020-11-20 |       7 |
  +----+-----------------+------+------+---------+------------+---------+
  4 rows in set (0.01 sec)
  
  ```

  - set null	

  ```mysql
  # 先删除，然后set null 就可以了
  foreign key (`person_ibfk_1`)
  alter table person add foreign key(dept_id) references dept(id) on delete set null on update set null;
  update dept set id = 3 where id =7;
  
  mysql> select * from dept;
  +----+-----------+
  | id | dname     |
  +----+-----------+
  |  1 | 技术部    |
  |  2 | 教学部    |
  |  3 | 财务部    |
  +----+-----------+
  3 rows in set (0.00 sec)
  
  mysql> select * from person;
  +----+-----------------+------+------+---------+------------+---------+
  | id | name            | age  | sex  | salary  | hire_date  | dept_id |
  +----+-----------------+------+------+---------+------------+---------+
  |  1 | 小阿giao        |   22 | m    | 1000.00 | 2020-12-20 |       2 |
  |  2 | 小刚            |   21 | w    | 5000.00 | 2020-10-21 |       2 |
  |  3 | 润玉大肥龙      |   22 | w    | 1000.00 | 2020-11-20 |       1 |
  |  4 | 东北酱          |   22 | m    | 1000.00 | 2020-11-20 |    NULL |
  +----+-----------------+------+------+---------+------------+---------+
  4 rows in set (0.00 sec)
  ```

## 表关联设计

- 一对一关系

  foreign key  , unique

  而且两个数据内容其实是可以放在一张表里。为什么放在两张表里？1. 这两个表在描述两个不同的事例，相对比较独立。2. 一张表过于庞大 3.为了使用方便

  ```mysql
  # 重新创建一个数据库,用于放关系模型
  create database relations;
  use relations;
  create table student(id int primary key auto_increment,name varchar(50) not null);
  create table record(id int primary key auto_increment,
  comment text not null,
  st_id int unique,
  foreign key(st_id) references student(id) on delete cascade on update cascade);
  # 一对一对应
  ```

- 一对多关系

  - 在从表这边建立外键关联

  ```mysql
  create table person(
  	id varchar(32) primary key,
  	name varchar(30),
  	sex char(1),
  	age int);  # 主键
  
  create table car(
  	id varchar(32) primary key,
    	name varchar(30),
      price decimal(10,2),
      pid varchar(32),
      foreign key(pid) references person(id)
  );
  ```

- 多对多

  - 创立多对多需要关系表

  ```mysql
  create table athlete(
      id int primary key auto_increment,
      name varchar(30)
  );
  create table item(
  	id int primary key auto_increment,
      item_name varchar(30)
  );
  create table athlete_item(
  	id int primary key auto_increment,
      athlete_id int,
      item_id int,
      score varchar(50),
      foreign key(athlete_id) references athlete(id),
      foreign key(item_id) references item(id)
  );
  ```

  

### 朋友圈练习

```mysql
create table users(
	id int primary key auto_increment,
    user_name varchar(30),
    pw varchar(16),
    telephone int(11)
);

create table moments(
	id int primary key auto_increment,
    picture varchar(30),
    content text,
    publish_time datetime,
    user_id int,
    foreign key(user_id) references users(id)
);

create table users_moments(
	id int primary key auto_increment,
    user_id int,
    moment_id int,
    er_comment text,
    er_like bit,
    foreign key(user_id) references users(id),
    foreign key(moment_id) references moments(id)
);

insert into users values
(1,'马云','123456',188588),
(2,'王建林','qwertyui',138383),
(3,'撒贝宁','123456',188588);
insert into moments values
(1,'picture','我不喜欢钱','2020-12-13 12:12:12',1),
(2,'picture','先定他个小目标','2020-12-13 12:12:12',2),
(3,'picture','挣他个一个亿','2020-12-13 12:12:12',2);
insert into users_moments values
(1,1,2,'装啥呢',1),
(1,3,1,'我也不喜欢北大',1);
```



## 表链接（表关联查询）

```mysql
# 地卡尔及现象（得到相乘）
mysql> select * from dept;
+----+-----------+
| id | dname     |
+----+-----------+
|  1 | 技术部    |
|  2 | 教学部    |
|  3 | 财务部    |
+----+-----------+
3 rows in set (0.00 sec)

mysql> select * from dept,person;
+----+-----------+----+-----------------+------+------+---------+------------+---------+
| id | dname     | id | name            | age  | sex  | salary  | hire_date  | dept_id |
+----+-----------+----+-----------------+------+------+---------+------------+---------+
|  1 | 技术部    |  1 | 小阿giao        |   22 | m    | 1000.00 | 2020-12-20 |       2 |
|  2 | 教学部    |  1 | 小阿giao        |   22 | m    | 1000.00 | 2020-12-20 |       2 |
|  3 | 财务部    |  1 | 小阿giao        |   22 | m    | 1000.00 | 2020-12-20 |       2 |
|  1 | 技术部    |  2 | 小刚            |   21 | w    | 5000.00 | 2020-10-21 |       2 |
|  2 | 教学部    |  2 | 小刚            |   21 | w    | 5000.00 | 2020-10-21 |       2 |
|  3 | 财务部    |  2 | 小刚            |   21 | w    | 5000.00 | 2020-10-21 |       2 |
|  1 | 技术部    |  3 | 润玉大肥龙      |   22 | w    | 1000.00 | 2020-11-20 |       1 |
|  2 | 教学部    |  3 | 润玉大肥龙      |   22 | w    | 1000.00 | 2020-11-20 |       1 |
|  3 | 财务部    |  3 | 润玉大肥龙      |   22 | w    | 1000.00 | 2020-11-20 |       1 |
|  1 | 技术部    |  4 | 东北酱          |   22 | m    | 1000.00 | 2020-11-20 |    NULL |
|  2 | 教学部    |  4 | 东北酱          |   22 | m    | 1000.00 | 2020-11-20 |    NULL |
|  3 | 财务部    |  4 | 东北酱          |   22 | m    | 1000.00 | 2020-11-20 |    NULL |
+----+-----------+----+-----------------+------+------+---------+------------+---------+
12 rows in set (0.00 sec)


select person.id,dept.dname,person.name from dept,person where dept.id=person.dept_id;
+----+-----------+-----------------+
| id | dname     | name            |
+----+-----------+-----------------+
|  1 | 教学部    | 小阿giao        |
|  2 | 教学部    | 小刚            |
|  3 | 技术部    | 润玉大肥龙      |
+----+-----------+-----------------+

# 优化 表重命名
select p.id,d.dname,p.name from dept as d,person as p where d.id=p.dept_id;

# 练习 查询技术部的员工
select p.id,d.dname,p.name,p.salary from dept as d,person as p where d.id=p.dept_id and d.dname='技术部';
# 这种写法已经不太被推崇，所以就有了表的链接。
# 练习 查询 分数在80分以上的哪些同学报了哪些兴趣爱好班
select c.name,h.hobby from hobby as h,class as c where c.score>80 and h.name = c.name;
# 多表查询不一定在有外键的情况下，没有外键也可以
```

不爽在于，不得不把匹配关系和筛选条件放在一起

- 内连接

  ```mysql
  select p.id,d.dname,p.name from dept as d inner join person as p on d.id=p.dept_id where d.dname = '教学部';
  +----+-----------+-----------------+
  | id | dname     | name            |
  +----+-----------+-----------------+
  |  1 | 教学部    | 小阿giao        |
  |  2 | 教学部    | 小刚            |
  |  3 | 技术部    | 润玉大肥龙      |
  +----+-----------+-----------------+
  select p.id,d.dname,p.name from dept as d inner join person as p on d.id=p.dept_id ;
  ```

- 外联接

  ```mysql
  # 左(右)链接
  select p.id,d.dname,p.name from dept as d right join person as p on d.id=p.dept_id ;
  +----+-----------+-----------------+
  | id | dname     | name            |
  +----+-----------+-----------------+
  |  3 | 技术部    | 润玉大肥龙      |
  |  1 | 教学部    | 小阿giao        |
  |  2 | 教学部    | 小刚            |
  |  4 | NULL      | 东北酱          |
  +----+-----------+-----------------+
  # 等同于
  select p.id,d.dname,p.name from person as p left join dept as d on d.id=p.dept_id ;
  +----+-----------+-----------------+
  | id | dname     | name            |
  +----+-----------+-----------------+
  |  3 | 技术部    | 润玉大肥龙      |
  |  1 | 教学部    | 小阿giao        |
  |  2 | 教学部    | 小刚            |
  |  4 | NULL      | 东北酱          |
  +----+-----------+-----------------+
  # 虽然相等，但是应该尽量把数据量大的表放在左边，数据量小的表放在右表，这样查询速度比较快。
  ```

  

