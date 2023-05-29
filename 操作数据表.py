import os, re
from 生成语音 import ai_reader_value
file_name = os.path.basename(__file__)[2:-3]

def p_tables():
    p_table = {key + ' (' + file_name + ')': value for key, value in {

        "删除数据表": "drop table 表名;",
        "删除某个字段": "alter table 表名 drop 字段名;",
        "删除check约束": "先用show create table 表名;查看约束名 然后 alter table 表名 drop check 约束名;",
        "删除unique约束": "先用show create table 表名; 查看unique名称 然后 alter table 表名 drop index unique名称;",
        "删除default默认值": "alter table 表名 alter 字段名称 drop default ;",
        "删除foreign key外键": "alter table 表名 drop foreign key 外键名称;",
        "创建表有3种方式": "第一种 create table 表名(); 第二种 create table 新表名 like 旧表名; 第三种 create table 表名 select 语句;",
        "查看所有表": "show tables ;",
        "查看表结构": "desc 表名;",
        "查看表创建信息": "show create table 表名;",
        "查看可用的存储引擎": "show engines ;",
        "查看所有字段的注释": "show full columns from 表名;",
        "修改表名": "alter table 旧的表名 rename to 新的表名;",
        "修改表的存储引擎": "alter table 表名称 engine =存储引擎;",
        "添加新字段": "alter table 表名称 add 新字段名称 新数据类型 not null unique ... first(after 字段2);",
        "修改字段名和字段类型有2种方式(字段位置,自增)": "alter table 表名称 change 旧的字段名 新的字段名 新的数据类型; 或者 alter table 表名称 modify 字段名 新的数据类型;",
        "添加check约束": "alter table 表名称 add constraint 约束名称 check (约束条件);",
        "添加unique": "alter table 表名称 add constraint 唯一约束名称 unique (字段名称);",
        "添加字段默认值": "alter table 表名称 alter 字段名 set default 默认值;",
        "添加foreign key外键": "alter table 表名 add constraint 外键名称 foreign key (字段名称) references 父表名称(父表的主键名称);",
        "添加表注释": "alter table 表名 comment '注释文字';",
        "添加字段注释": "alter table 表名称 modify column 字段名 字段类型 comment '注释文字';",

    }.items()}
    return p_table


if __name__ == "__main__":
    # -------------------------------生成AI语音字符串-------------------------------------------------
    # 去掉key中的()
    a_part = {re.sub(r'\([^)]*\)', '', key): value for key, value in p_tables().items()}
    # 遍历字典,生成AI语音字符串
    for key, value in a_part.items():
        value = ai_reader_value(value)
        if "/" in key:
            key = key.replace("/", "或者")  # 把/替换成 或者
        key = '((⏱️=1500))' + key
        print('\n', key, value)
    print('\n一共有 ' + str(len(a_part)) + ' 个'+' '+str(len(p_tables())))



