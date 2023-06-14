import os
from 调用此函数生成最终语音字符串 import final
file_name = os.path.basename(__file__)[2:-3]

def p_commands():
    p_command = {key + ' (' + file_name + ')': value for key, value in {
        "可以直接执行SQL语句,无需登录mysql服务器 只需要加-e,多条SQL语句之间用分号隔开":"mysql -u 用户名 -p -e 双引号 select语句1 ; select语句2 双引号",
        "查看每个数据库中数据表的数量和数据的总条数":"mysqlshow -u root -p --count",
        "查看具体某个数据库中数据表的数量和数据的总条数":"mysqlshow -u root -p 数据库名 --count",

    }.items()}
    return p_command

if __name__ == "__main__":
    final(p_commands())






