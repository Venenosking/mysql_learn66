import os
from 调用此函数生成最终语音字符串 import final
file_name = os.path.basename(__file__)[2:-3]

def p_views():
    p_view = {key + ' (' + file_name + ')': value for key, value in {
        "如何删除视图": "drop view 视图名称;",
        "如何修改视图": "alter view 视图名称 as select 语句;",
        "创建视图": "create or replace view 视图名称 (字段别名1,字段别名2) as select 语句 with cascaded/local check option ;",
        "查看视图 6种方式": "show tables; show full tables; desc 视图名称; show table status like '视图名称'; show create view 视图名称; select * from information_schema.views;",

    }.items()}
    return p_view

if __name__ == "__main__":
    final(p_views())



