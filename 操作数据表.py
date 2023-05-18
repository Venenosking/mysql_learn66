
import os
file_name = os.path.basename(__file__)[2:-3]

p_table = {key + ' ('+file_name+')': value for key, value in {
    "如何删除数据表":"drop table 表名;",
    "如何删除字段":"alter table 表名 drop 字段名;",
    # "":"",

}.items()}




