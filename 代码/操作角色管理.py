import os
from 调用此函数生成最终语音字符串 import final
file_name = os.path.basename(__file__)[2:-3]

def p_roles():
    p_role= {key + ' (' + file_name + ')': value for key, value in {
        "创建角色": "create role 角色名@主机名;",
        "删除角色": "drop role 角色名称@主机名;",
        "查看角色": "select * from mysql.user;",
        "查看当前角色": "select current_role();",
        "把角色分配给用户": "grant 角色名@主机名 to 用户名@主机名;",
        "复制用户权限给其他用户": "grant 用户名@主机名 to 用户名@主机名;",
        "设置默认角色": "set default role 角色名@主机名 to 用户名@主机名;",

    }.items()}
    return p_role

if __name__ == "__main__":
    final(p_roles())



