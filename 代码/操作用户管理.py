import os
from 调用此函数生成最终语音字符串 import final
file_name = os.path.basename(__file__)[2:-3]

def p_users():
    p_user = {key + ' (' + file_name + ')': value for key, value in {
        "创建用户": "create user 用户名@主机名 identified by '密码';",
        "删除用户": "drop user 用户名@主机名;",
        "修改用户名或主机名": "先 mysql -u 用户名 -p 切换到当前用户,然后rename user 旧用户名@旧主机名 to 新用户名@新主机名 ;",
        "修改用户密码": "alter user 用户名@主机名 identified by '新密码';",
        "查看所有用户": "select * from mysql.user;",
        "查看当前用户": "select user(); ",

    }.items()}
    return p_user

if __name__ == "__main__":
    final(p_users())



