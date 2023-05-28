
import os,re
file_name = os.path.basename(__file__)[2:-3]


def AI_reader(string):
   new_string = ""
   # 替换左右括号
   for char in string:
      if char == "(":
         new_string += " 左括号 "
      elif char == ")":
         new_string += " 右括号 "
      else:
         new_string += char
   # 合并多个空格
   new_string = re.sub(r'\s+', ' ', new_string)
   # 字符末尾是  s的替换成寺 t替换成忑 d替换成的  
   new_string = new_string.replace("s ", "s寺 ")
   new_string = new_string.replace("t ", "t忑 ")
   new_string = new_string.replace("d ", "d的 ")
   # 句中加400ms间隔时间 
   new_string = new_string.replace(" ", "((⏱️=400))")
   # 开头加2s间隔时间
   new_string = '((⏱️=2000))' + new_string

   # print("替换后的字符串为：", new_string)
   return new_string


p_partition = {key + ' ('+file_name+')': value for key, value in {
    
   "创建List分区表":"create table 表名 () partition by list(字段)(partition 分区名 values in (具体值));",
   "额外添加一个List分区":"alter table 表名 add partition (partition 分区名 values in (具体值));",
   "额外删除一个List分区":"alter table 表名 drop partition 分区名;",
   "重新定义List分区":"alter table 表名 reorganize partition 旧分区名1,旧分区名2 into (partition 新分区名1 values in (具体值1,具体值2));",
   "创建range分区表":"create table 表名 () partition by range (字段)(partition 分区名1 values less than (具体值));",
   "查看分区表的数据分布":"select * from information_schema.partitions where table_schema=schema() and table_name='表名';",
   "额外添加一个range分区":"alter table 表名 add partition (partition 分区名 values less than (具体值));",
   "删除一个range分区":"alter table 表名 drop partition 分区名;",
   "重新定义range分区":"alter table 表名 reorganize partition 旧分区名1 into (partition 新分区名1 values less than (具体值));",
   "创建常规Hash分区":"create table 表名 () partition by hash (字段) partitions 数字;",
   "创建线性Hash分区":"create table 表名 () partition by linear hash (字段) partitions 数字;",
   "额外添加一个Hash/Key分区":"alter table 表名 add partition partitions 数字;",
   "额外减少一个Hash/Key分区":"alter table 表名 coalesce partition 数字;",
   "创建Key分区":"create table 表名 () partition by key(字段) partitions 数字;",

}.items()}

# AI_reader()
# 去掉key中的()
a_partition={re.sub(r'\([^)]*\)', '', key): value for key, value in p_partition.items()}
for key, value in a_partition.items():
    print(key, value)
# print(a_partition)

v_test={
   "额外添加一个Hash/Key分区 +":'alter table 表名1 add partition partitions 数字;',
   "额外减少一个Hash/Key分区 -":"alter table 表名2 coalesce partition 数字;",
   "创建Key分区 +":"create table 表名 () partition by key(字段) partitions 数字;",
   "删除一个range分区 -":"alter table 表名 drop partition 分区名;",
}

