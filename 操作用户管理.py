
import os
file_name = os.path.basename(__file__)[2:-3]

p_user = {key + ' ('+file_name+')': value for key, value in {
    "创建用户":"create user 用户名@主机名 identified by 密码;",
    "删除用户":"drop user 用户名@主机名;",
    # "":"",

}.items()}


