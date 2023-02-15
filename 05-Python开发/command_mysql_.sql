/*
 sql脚本的使用
 file：command_linux_shell.sh
 author：LBL
 date：2023-2-15
 
 执行sql文件需在目录能找到文件，或者写绝对路径：
     cmd控制台:     mysql -u用户名 -p密码 -D数据库 < ***.sql       如果在文件中写了use数据库，可以不带-D选项
     myslq控制台：  source  ***.sql ;
 登录mysql：
     mysql -u root -p123456 -P3306 -h127.0.0.1
 退出：
 exit; \quit; /q; \ctrl+d
*/
-- 单行注释（必须有个空格）
# mysql独有的单行注释方式



--查看数据库版本
select version();
--查看当前时间
select now();
--查看数据库
show databases;
--使用数据库
use python41;
--新增数据库
create database python42 charset=utf8;
create datablase if not exists python43;
--查看当前使用的数据库
select database();
--删除数据库
drop database python42;
drop database if exists python43;

--查看所有表
show tables;
--查看表结构
desc students;
--查看创建表语句
show create table students;

--创建表
create table if not exists students (
    id int primary key auto_increment,
    name varchar(20),		//变长最大20字符
    gender char(1),		//定长1字符
    c_id char(2),		//班级号
    birthday date
);
--删除表
drop table students;
drop table if exists students;

--更改表名
alter table students rename to students2;
--添加一列
alter table students add status int;
--修改数据类型
alter table students modify status tinyint not null;
--修改列名和数据类型
alter table students change status status2 tinyint;
--删除列
alter table students drop status;


--新增数据
insert into students (id,name,gender,c_id,birthday) values(1,"小式",'女','12',"2022-2-2");
--删除数据
delete from students where id =1;
--修改数据
update students set age = 15 where id =4;



--去重查询
select distinct  age from students ;


--条件
and  or  
--范围查询  连续范围between and   不连续in
age in (1,5,7);
age not in  (1,5,7);
between 1 and 10; 


--模糊查询,like	%任意位任意字符，_一位任意字符
select name from students where name like '黄%' ;
select name from students where name like '黄_' 

--判断空
is  null  
is not null

--排序 asc 升序，desc降序
select * from students order by age asc, height desc;

--聚合函数
avg()  sum()  min() max() count()  group_content()  
--分组和聚合函数，查询内容只能是分组内容和聚合函数
sleect gender from students group by gender;
select gender ,group_content(name)  from students group by gender;
select gender ,avg(age) from students group by gender 
 --分组后筛选。按性别分组求平均分(60分以上才统计)，分组统计后显示平均分数大于90的组
select avg(score),gender from students where score>60 group by gender having acg(score)>90;

--分页,每页m个，从第几页开始显示m个
select * from students limit  (n-1)m,m；
--分页查询limit是mysql的方言。每种数据库都不一样
select * from students where score > 60 limit 0,15;
select * from students where score > 60 limit 15,15;

--约束constraint
非空 not null    唯一 unique    主键 primary key   外键 foreign key
检查约束check（mysql不支持） 

-- 主键，唯一标识表中数据的属性，非空且唯一。
-- 外键，外键用来维护两个表的关联关系，只能填主表关联列有的值，主键外键都会自动加上索引，查询更快
-- 为已存在的表添加外键
-- alter table studfents add foreign key (cls_id) references classes(id);
-- 创建表时添加外键
-- create table students (id int unsigned not null primary key auto increment,
		       name  varchar(10),
		       cls_id int not null,
		      foreign key(cls_id) references classses(id));
--删除外键
--alter table students drop foreign key  cls_id;



==========================多表查询===============
--内连接分显示内连接和隐式内连接，查询结果为两个表的笛卡尔积
--隐式内连接
select s.id,s.gender,c.id from students s,classes c where s.c_id=c.id; 
--显示内连接查询，两个表的交集
select * from students  s  inner join classes c on s.c_id =c.id;
--自联结就是内连接，两张表都是自己，别名不同

--外连接分为左右外连接
--左连接，以左表为主左表都显示，没匹配到右表的部分用null代替;学生表中班级id没有在班级表的也会显示
select * from students s left join classes  c on s.c_id =c.id;
--右连接，右表为主，类似左连接
select * from students s right join classes c on s.c_id = c.id;
--多表内连接a,b,c
select a.name,b.id,c.salary from a,b,c where a.bid=b.id and a.cid=c.id;
select  a.name,b.id,c.salary from a inner join b on a.bid=b.id inner join c on a.cid=c.id; 

--子查询，将查询结果作为临时表
select * from students where age > (select avg(age) from students );



--索引：增加查询速度，主键外键都会自动加索引
--增加索引(给name添加索引，前面的name是索引名，不写index(name)的话默认索引名就是name)
alter table classes add index name(name);

--删除索引
alter table classes drop index(name);


-- 事务transaction
-- 一套sql语句要么都执行要么都不执行，都成功提交，有失败就回滚
-- mysql中平时执行语句事务等级select @@autocommit;为1  每条语句都会默认自动提交，oracle得自己手动提交
-- 事务的四大特性ACID原子性、一致性、隔离性、持久性

 -- 开启事务
begin;	-- 或者start transaction
update account set money = money-500 where name="张三";
-- 模拟发生错误
update account set money = monet+500 where name="李四";

-- 成功提交事务
commit;
-- 失败回滚
ROLLBACK;




--将查询结果插入到其他表
--从商品表查询商品品牌插入到品牌表
insert into goods_cate(name)  selectc cate_name from goods group by cate_name;

/* 连接查询 更改表的一列信息，将cate_name 换成左表id值			
id    name        	id    cate_name   name
1     苹果   	1        苹果           苹果13s
2     小米		2        小米           红米12 
*/
select * from goods g inner join goods_cate gc on g.cate_name = gc.name;
update  goods g inner join goods_cate gc on g.cate_name = gc.name set g.cate_name = gc.id ;

-- 创建表时插入查询到别的表的某列信息
create table brand_name(
id int primary key auto increment ,
name varchar(30) not null select brand_name as name from goods group by brand_name);		          );


-- 数据库备份与恢复
-- 备份：navicate中鼠标右击某个数据库，点击转储SQL文件->结构与数据
-- navicate恢复：新建一个仓库，字符集与要恢复的一致，navicate右击数据库，运行SQL文件，打开保存的sql文件，点开始，恢复成功。
-- cmd恢复：新建一个仓库，字符集与要恢复的一致，使用该数据库后source C:/Users/WJ/Documents/test.sql  。注意navicate不支持source命令



