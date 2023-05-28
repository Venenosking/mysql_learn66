import os, re
from 生成语音 import ai_reader_value
file_name = os.path.basename(__file__)[2:-3]

def p_roles():
    p_role = {key + ' (' + file_name + ')': value for key, value in {
       "创建角色": "create role 角色名@主机名;",
       "删除角色": "drop role 角色名称@主机名;",
       "查看角色": "select * from mysql.user;",
       "查看当前角色": "select current_role();",
       "角色分配给用户": "grant 角色名@主机名 to 用户名@主机名;",
       "复制用户权限给其他用户": "grant 用户名@主机名 to 用户名@主机名;",
       "设置默认角色": "set default role 角色名@主机名 to 用户名@主机名;",

    }.items()}
    return p_role


if __name__ == "__main__":
    # -------------------------------生成AI语音字符串-------------------------------------------------
    # 去掉key中的()
    a_part = {re.sub(r'\([^)]*\)', '', key): value for key, value in p_roles().items()}
    # 遍历字典,生成AI语音字符串
    for key, value in a_part.items():
        value = ai_reader_value(value)
        if "/" in key:
            key = key.replace("/", "或者")  # 把/替换成 或者
        key = '((⏱️=1500))' + key
        print('\n', key, value)
    print('\n一共有 ' + str(len(a_part)) + ' 个')



