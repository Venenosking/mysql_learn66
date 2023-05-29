import os, re
from 生成语音 import ai_reader_value
file_name = os.path.basename(__file__)[2:-3]

def p_grants():
    p_grant = {key + ' (' + file_name + ')': value for key, value in {
       "授予用户权限": "grant 权限名称 on 数据库名.表名 to 用户名@主机名 with grant option;",
       "授予角色权限 ": "grant 权限名称 on 数据库名.表名 to 角色名@主机名 with grant option;",
       "撤销权限": "revoke 权限名称 on 数据库名.表名 from 用户名@主机名;",
       "撤销全部权限": "revoke all,grant option from 用户名@主机名;",
       "查看用户权限": "show grants for 用户名@主机名 ;",
       "查看角色赋予用户之后的用户权限": "show grants for 用户名@主机名 using 角色名;",
       "查看角色权限": "show grants for 角色名@主机名 ;",

    }.items()}
    return p_grant


if __name__ == "__main__":
    # -------------------------------生成AI语音字符串-------------------------------------------------
    # 去掉key中的()
    a_part = {re.sub(r'\([^)]*\)', '', key): value for key, value in p_grants().items()}
    # 遍历字典,生成AI语音字符串
    for key, value in a_part.items():
        value = ai_reader_value(value)
        if "/" in key:
            key = key.replace("/", "或者")  # 把/替换成 或者
        key = '((⏱️=1500))' + key
        print('\n', key, value)
    print('\n一共有 ' + str(len(a_part)) + ' 个'+' '+str(len(p_grants())))



