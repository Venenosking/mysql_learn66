import os, re
from 生成语音 import ai_reader_value
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
    # -------------------------------生成AI语音字符串-------------------------------------------------
    # 去掉key中的()
    a_part = {re.sub(r'\([^)]*\)', '', key): value for key, value in p_views().items()}
    # 遍历字典,生成AI语音字符串
    for key, value in a_part.items():
        value = ai_reader_value(value)
        if "/" in key:
            key = key.replace("/", "或者")  # 把/替换成 或者
        key = '((⏱️=1500))' + key
        print('\n', key, value)
    print('\n一共有 ' + str(len(a_part)) + ' 个')



