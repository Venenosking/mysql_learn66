import os
from 调用此函数生成最终语音字符串 import final
file_name = os.path.basename(__file__)[2:-3]

def p_partitions():
    p_partition= {key + ' (' + file_name + ')': value for key, value in {
       "创建List分区表": "create table 表名 () partition by list(字段)(partition 分区名 values in (具体值));",
       "额外添加一个List分区": "alter table 表名 add partition (partition 分区名 values in (具体值));",
       "额外删除一个List分区": "alter table 表名 drop partition 分区名;",
       "重新定义List分区": "alter table 表名 reorganize partition 旧分区名1,旧分区名2 into (partition 新分区名1 values in (具体值1,具体值2));",
       "创建range分区表": "create table 表名 () partition by range (字段)(partition 分区名1 values less than (具体值));",
       "查看分区表的数据分布": "select * from information_schema.partitions where table_schema=schema() and table_name='表名';",
       "额外添加一个range分区": "alter table 表名 add partition (partition 分区名 values less than (具体值));",
       "删除一个range分区": "alter table 表名 drop partition 分区名;",
       "重新定义range分区": "alter table 表名 reorganize partition 旧分区名1 into (partition 新分区名1 values less than (具体值));",
       "创建常规Hash分区": "create table 表名 () partition by hash (字段) partitions 数字;",
       "创建线性Hash分区": "create table 表名 () partition by linear hash (字段) partitions 数字;",
       "额外添加一个Hash/Key分区": "alter table 表名 add partition partitions 数字;",
       "额外减少一个Hash/Key分区": "alter table 表名 coalesce partition 数字;",
       "创建Key分区": "create table 表名 () partition by key(字段) partitions 数字;",

    }.items()}
    return p_partition

if __name__ == "__main__":
    final(p_partitions())



