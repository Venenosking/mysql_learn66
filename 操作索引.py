
import os
file_name = os.path.basename(__file__)[2:-3]

p_index = {key + ' ('+file_name+')': value for key, value in {
    "删除索引(2种方式)":"drop index 索引名 on 表名; alter table 表名 drop index 索引名;",
    "删除primary key主键":"alter table 表名 drop primary key;",
    "查看某个表的索引 2种方式":"show index from 表名; show create table 表名;",
    "更改索引隐藏/可见":"alter table 表名 alter index 索引名 invisible;",
    "创建隐藏索引":"在创建索引的末尾添加invisible",
    "主键索引":"alter table 表名 add primary key (字段名);",
    "普通索引":"alter table 表名 add index 索引名 (字段名);",
    "组合索引":"alter table 表名 add index 索引名 (字段1,字段2,...);",
    "唯一索引":"alter table 表名 add unique index 索引名 (字段名);",
    "前缀索引":"alter table 表名 add index 索引名 (字段(长度));",
    "降序索引":"alter table 表名 add index 索引名 (字段1 asc,字段2 desc);",
    "全文索引":"alter table 表名 add fulltext index 索引名(字段名);",
    "主键索引 create":"只能通过alter table的方式添加",
    "普通索引 create":"create index 索引名 on 表名 (字段名);",
    "组合索引 create":"create index 索引名 on 表名 (字段1,字段2,...);",
    "唯一索引 create":"create unique index 索引名 on 表名 (字段名);",
    "前缀索引 create":"create index 索引名 on 表名 (字段(长度));",
    "降序索引 create":"create index 索引名 on 表名 (字段1 asc,字段2 desc); ",
    "全文索引 create":"create fulltext index 索引名 on 表名 (字段名);",


}.items()}

