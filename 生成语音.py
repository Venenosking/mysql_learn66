# https://ttsmaker.com/zh-cn
# 语速 0.85
import re
string = 'create table 表名 () partition by list(字段)(partition 分区名 values in (具体值));'
# string = 'alter table 表名 add partition partitions 数字;'
# string = 'alter table 表名 reorganize partition 旧分区名1 into (partition 新分区名1 values less than (具体值));'

# value
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
    new_string = '((⏱️=2000))'+new_string
    
    print("替换后的字符串为：", new_string)
    return new_string
AI_reader(string)

