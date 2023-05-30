import os
from 调用此函数生成最终语音字符串 import final
file_name = os.path.basename(__file__)[2:-3]

def p_procedures():
    p_procedure= {key + ' (' + file_name + ')': value for key, value in {
        "创建存储过程": "create procedure 存储过程名称 (in|out|inout 参数1 数据类型,in|out|inout 参数2 数据类型,...) begin declare 变量1 数据类型 default '默认值'; declare 变量2 数据类型 default '默认值'; set 变量1=具体值1; set 变量2=具体值2;   end;",
        "使用游标": "declare 游标名称 cursor for select 语句; declare exit handle for not found close 游标名称; open 游标名称; fetch 游标名称 into 变量1; close 游标名称;",
        "loop循环": "标签名:loop 语句; leave 标签名;相当于break iterate 标签名; 相当于continue  end loop 标签名;",
        "repeat循环": "repeat 语句; until 条件 end repeat;",
        "while循环": "while 条件 do  语句; end while;",
        "if条件判断": "if 条件 then 语句; elseif 条件 then 语句; else 语句; end if;",
        "case条件判断": "case when 条件 then 语句; when 条件 then 语句; else 语句; end case;",

    }.items()}
    return p_procedure

if __name__ == "__main__":
    final(p_procedures())



