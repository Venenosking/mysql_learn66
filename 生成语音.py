# https://ttsmaker.com/zh-cn
# 语速 0.85
string = 'create table 表名 () partition by list(字段)(partition 分区名 values in (具体值));'
new_string = ""

for char in string:
    if char == "(":
        new_string += " 左括号 "
    elif char == ")":
        new_string += " 右括号 "
    else:
        new_string += char

# new_string = new_string.replace(" ", "((⏱️=400))",1)
print("替换后的字符串为：", new_string)


