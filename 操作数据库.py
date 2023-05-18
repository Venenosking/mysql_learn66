
import os
file_name = os.path.basename(__file__)[2:-3]

p_database = {key + ' ('+file_name+')': value for key, value in {
    
   "删除数据库":"drop database 数据库名称;",
   "创建数据库":"create database 数据库名称;",
   "使用某个数据库":"use 数据库名称;",

}.items()}





