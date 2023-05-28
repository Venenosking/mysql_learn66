import os, re
from 生成语音 import ai_reader_value
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
    # -------------------------------生成AI语音字符串-------------------------------------------------
    # 去掉key中的()
    a_part = {re.sub(r'\([^)]*\)', '', key): value for key, value in p_indexs().items()}
    # 遍历字典,生成AI语音字符串
    for key, value in a_part.items():
        value = ai_reader_value(value)
        if "/" in key:
            key = key.replace("/", "或者")  # 把/替换成 或者
        key = '((⏱️=1500))' + key
        print('\n', key, value)
    print('\n一共有 ' + str(len(a_part)) + ' 个')



