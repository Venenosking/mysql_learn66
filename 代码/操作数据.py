import os
from 调用此函数生成最终语音字符串 import final
file_name = os.path.basename(__file__)[2:-3]

def p_datas():
    p_data = {key + ' (' + file_name + ')': value for key, value in {
        "插入单条数据 指定字段": "insert into 表名 (字段1,字段2) values (具体值1,具体值2);",
        "插入多条数据 指定字段": "insert into 表名 (字段1,字段2) values (具体值1,具体值2),(具体值3,具体值4);",
        "插入多条数据 不指定字段": "insert into 表名 values (具体值1,具体值2),(具体值3,具体值4);",
        "插入单条数据 不指定字段": "insert into 表名 values (具体值1,具体值2);",
        "将查询结果插入另一个表中": "insert into 表名 (字段1,字段2) select 语句;",
        "删除表中全部数据": "delete from 表名 ;",
        "删除表中指定数据 用=号的方式": "delete from 表名 where 字段名 = 具体数值 ;",
        "删除表中指定数据用between and的方式": "delete from 表名 where 字段名 between 具体数值1 and 具体数值2 ;",
        "删除表中指定数据用> >= < <=的方式": "delete from 表名 where 字段名 这里写>=或者> 具体数值1 and 字段名 这里写<=或者< 具体数值2 ;",
        "删除表中指定数据用in/not in的方式": "delete from 表名 where 字段名 in (具体值1,具体值2);",
        "删除表中指定数据用like的方式": "delete from 表名 where 字段名 like '具体的值'; ",
        "删除表中指定数据用regexp正则表达式": "delete from 表名 where 字段名 regexp '具体的值';",
        "更新表中全部数据": "update 表名/视图名 set 字段名=具体的值;",
        "更新指定数据用=号的方式": "update 表名/视图名 set 字段名=具体的值 where 字段名 = 具体的值 ; ",
        "更新指定数据用between and的方式": "update 表名/视图名 set 字段名=具体的值 where 字段名 between 具体的值1 and 具体的值2 ;",
        "更新指定数据> >= < <=": "update 表名/视图名 set 字段名=具体的值 where 字段名 这里写>=或者> 具体的值1 and 字段名 这里写<=或者< 具体的值2 ; ",
        "更新指定数据用in或者not in的方式": "update 表名/视图名 set 字段名=具体的值 where 字段名 这里写in或者not in (具体的值);",
        "更新指定数据用like的方式": "update 表名/视图名 set 字段名=具体的值 where 字段名 like '具体的值' ; ",
        "更新指定数据用regexp的方式": "update 表名/视图名 set 字段名=具体的值 where 字段名 regexp '具体的值' ; ",

    }.items()}
    return p_data

if __name__ == "__main__":
    final(p_datas())



