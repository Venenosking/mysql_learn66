import os, re
from 生成语音 import ai_reader_value
file_name = os.path.basename(__file__)[2:-3]

def p_indexs():
    p_index = {key + ' (' + file_name + ')': value for key, value in {
        "删除索引(2种方式)": "drop index 索引名 on 表名; alter table 表名 drop index 索引名;",
        "删除primary key主键": "alter table 表名 drop primary key;",
        "查看某个表的索引 2种方式": "show index from 表名; show create table 表名;",
        "更改索引隐藏/可见": "alter table 表名 alter index 索引名 invisible;",
        "创建隐藏索引": "在创建索引的末尾添加invisible",
        "主键索引": "alter table 表名 add primary key (字段名);",
        "普通索引": "alter table 表名 add index 索引名 (字段名);",
        "组合索引": "alter table 表名 add index 索引名 (字段1,字段2,...);",
        "唯一索引": "alter table 表名 add unique index 索引名 (字段名);",
        "前缀索引": "alter table 表名 add index 索引名 (字段(长度));",
        "降序索引": "alter table 表名 add index 索引名 (字段1 asc,字段2 desc);",
        "全文索引": "alter table 表名 add fulltext index 索引名(字段名);",
        "主键索引 create": "只能通过alter table的方式添加",
        "普通索引 create": "create index 索引名 on 表名 (字段名);",
        "组合索引 create": "create index 索引名 on 表名 (字段1,字段2,...);",
        "唯一索引 create": "create unique index 索引名 on 表名 (字段名);",
        "前缀索引 create": "create index 索引名 on 表名 (字段(长度));",
        "降序索引 create": "create index 索引名 on 表名 (字段1 asc,字段2 desc); ",
        "全文索引 create": "create fulltext index 索引名 on 表名 (字段名);",

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



