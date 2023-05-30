import os
from 调用此函数生成最终语音字符串 import final
file_name = os.path.basename(__file__)[2:-3]

def p_indexs():
    p_index = {key + ' (' + file_name + ')': value for key, value in {
        "删除索引有2种方式": "drop index 索引名 on 表名; 或者 alter table 表名 drop index 索引名;",
        "删除primary key主键": "alter table 表名 drop primary key;",
        "查看某个表的索引有2种方式": "show index from 表名; 或者 show create table 表名;",
        "更改索引隐藏/可见": "alter table 表名 alter index 索引名 invisible;",
        "创建隐藏索引": "在创建索引的末尾添加invisible",
        "创建主键索引 alter的方式": "alter table 表名 add primary key (字段名);",
        "创建普通索引 alter的方式": "alter table 表名 add index 索引名 (字段名);",
        "创建组合索引 alter的方式": "alter table 表名 add index 索引名 (字段1,字段2);",
        "创建唯一索引 alter的方式": "alter table 表名 add unique index 索引名 (字段名);",
        "创建前缀索引 alter的方式": "alter table 表名 add index 索引名 (字段(前缀长度));",
        "创建降序索引 alter的方式": "alter table 表名 add index 索引名 (字段1 asc,字段2 desc);",
        "创建全文索引 alter的方式": "alter table 表名 add fulltext index 索引名(字段名);",
        "创建主键索引 create的方式": "不能通过create的方式创建主键,只能通过alter table的方式添加",
        "创建普通索引 create的方式": "create index 索引名 on 表名 (字段名);",
        "创建组合索引 create的方式": "create index 索引名 on 表名 (字段1,字段2);",
        "创建唯一索引 create的方式": "create unique index 索引名 on 表名 (字段名);",
        "创建前缀索引 create的方式": "create index 索引名 on 表名 (字段(前缀长度));",
        "创建降序索引 create的方式": "create index 索引名 on 表名 (字段1 asc,字段2 desc);",
        "创建全文索引 create的方式": "create fulltext index 索引名 on 表名 (字段名);",

    }.items()}
    return p_index

if __name__ == "__main__":
    final(p_indexs())



