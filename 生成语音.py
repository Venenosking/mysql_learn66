# https://ttsmaker.com/zh-cn
# 语速 0.85
import re
# string = 'create table 表名 () partition by list(字段)(partition 分区名 values in (具体值));'
# 处理字典中的value
def ai_reader_value(string):
    new_string = ""
    # 替换左右括号
    for char in string:
        if char == "(":
            new_string += " 左括号 "
        elif char == ")":
            new_string += " 右括号 "
        else:
            new_string += char
    # 把' 替换成引号
    new_string = new_string.replace("'", " 引号 ")
    # 合并多个空格
    new_string = re.sub(r'\s+', ' ', new_string)
    # 字符末尾是  s的替换成寺 t替换成忑 d替换成的  
    new_string = new_string.replace("s ", "s寺 ")
    new_string = new_string.replace("t ", "t忑 ")
    new_string = new_string.replace("d ", "d的 ")
    new_string = new_string.replace("/", "或者")
    new_string = new_string.replace("-", "-杠").replace("*", "星号").\
        replace("mysql", "买色抠((⏱️=400))").replace(".", "点((⏱️=400))").replace(" to ", " 兔 ")
    
    # 句中加800ms间隔时间 
    new_string = new_string.replace(" ", "((⏱️=800))")
    # 开头加1.5s间隔时间
    new_string = '((⏱️=1500))'+new_string
    # print("替换后的字符串为：", new_string)
    return new_string


