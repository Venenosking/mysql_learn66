
import os
file_name = os.path.basename(__file__)[2:-3]

p_partition = {key + ' ('+file_name+')': value for key, value in {
    
   "创建List分区表":"create table 表名 () partition by list(字段)(partition 分区名 values in (具体值1,具体值2),partition 分区名 values in (具体值1,具体值2,具体值3));",
   "额外添加一个List分区":"alter table 表名 add partition (partition 分区名 values in (具体值1,具体值2,...));",
   "额外删除一个List分区":"alter table 表名 drop partition 分区名;",
   "重新定义List分区":"alter table 表名 reorganize partition 旧分区名1,旧分区名2 into (partition 新分区名1 values in (具体值1,具体值2),partition 新分区名2 values in (具体值3,具体值4));",

}.items()}
