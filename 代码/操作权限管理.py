import os
from 调用此函数生成最终语音字符串 import final
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
    final(p_grants())



