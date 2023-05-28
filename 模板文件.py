


s={


 "创建角色":"create role 角色名@主机名;",
   "删除角色":"drop role 角色名称@主机名;",
   "查看角色":"select * from mysql.user;",
   "查看当前角色":"select current_role();",
   "角色分配给用户":"grant 角色名@主机名 to 用户名@主机名;",
   "复制用户权限给其他用户":"grant 用户名@主机名 to 用户名@主机名;",
   "设置默认角色":"set default role 角色名@主机名 to 用户名@主机名;",

   
   
}