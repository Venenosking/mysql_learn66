import os, re
from 生成语音 import ai_reader_value
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
    # -------------------------------生成AI语音字符串-------------------------------------------------
    # 去掉key中的()
    a_part = {re.sub(r'\([^)]*\)', '', key): value for key, value in p_users().items()}
    # 遍历字典,生成AI语音字符串
    for key, value in a_part.items():
        value = ai_reader_value(value)
        if "/" in key:
            key = key.replace("/", "或者")  # 把/替换成 或者
        key = '((⏱️=1500))' + key
        print('\n', key, value)
    print('\n一共有 ' + str(len(a_part)) + ' 个'+' '+str(len(p_users())))



