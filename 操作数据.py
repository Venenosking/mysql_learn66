
import os
file_name = os.path.basename(__file__)[2:-3]

p_data = {key + ' ('+file_name+')': value for key, value in {

   "插入单条数据 指定字段":"insert into 表名 (字段1,字段2) values (具体值1,具体值2);",
   "插入多条数据 指定字段":"insert into 表名 (字段1,字段2) values (具体值1,具体值2),(具体值1,具体值2);",
   "插入多条数据 不指定字段":"insert into 表名 values (具体值1,具体值2),(具体值1,具体值2);",
   "插入单条数据 不指定字段":"insert into 表名 values (具体值1,具体值2);",
   "将查询结果插入另一个表中":"insert into 表名 (字段1,字段2) select 语句;",
   "删除全部数据":"delete from 表名 ;",
   "删除表中指定数据(=)":"delete from 表名 where 字段名 = 具体数值 ;",
   "删除表中指定数据(between and)":"delete from 表名 where 字段名 between 具体数值1 and 具体数值2 ;",
   "删除表中指定数据(> >= < <=)":"delete from 表名 where 字段名 这里写>=或者> 具体数值1 这里写<=或者< 具体数值2 ;",
   "删除表中指定数据(in,not in)":"delete from 表名 where 字段名 in (具体值1 , 具体值2);",
   "删除表中指定数据(like)":"delete from 表名 where 字段名 like '具体的值'; ",
   "删除表中指定数据(regexp)正则表达式":"delete from 表名 where 字段名 regexp '具体的值';",
   "更新全部数据":"update 表名/视图名 set 字段名=具体的值;",
   "更新指定数据(=)":"update 表名/视图名 set 字段名=具体的值 where 字段名 = 具体的值 ; ",
   "更新指定数据(between and)":"update 表名/视图名 set 字段名=具体的值 where 字段名 between 具体的值1 and 具体的值2 ;",
   "更新指定数据(> >= < <=)":"update 表名/视图名 set 字段名=具体的值 where 字段名 这里写>=或者> 具体的值1 这里写<=或者< 具体的值2 ;",
   "更新指定数据(in/not in)":"update 表名/视图名 set 字段名=具体的值 where 字段名 这里写in或者not in (具体的值);",
   "更新指定数据(like)":"update 表名/视图名 set 字段名=具体的值 where 字段名 like '具体的值' ; ",
   "更新指定数据(regexp)":"update 表名/视图名 set 字段名=具体的值 where 字段名 regexp '具体的值' ; ",

}.items()}
