
import os
file_name = os.path.basename(__file__)[2:-3]

p_index = {key + ' ('+file_name+')': value for key, value in {
    "如何删除索引(2种方式)":"drop index 索引名 on 表名; alter table 表名 drop index 索引名;",
    "如何删除主键":"alter table 表名 drop primary key;",
    "如何删除外键":"alter table 表名 drop foreign key 外键名;",
    # "":"",

}.items()}

