
import os
file_name = os.path.basename(__file__)[2:-3]

p_database = {key + ' ('+file_name+')': value for key, value in {
    
   "删除数据库":"drop database 数据库名称;",
   "创建数据库":"create database 数据库名称;",
   "使用某个数据库":"use 数据库名称;",
   "查看所有数据库":"show databases;",
   "查看当前数据库":"select database(); ",
   "查看某个数据库的创建信息":"show create database 数据库名称; ",
   "查看当前用户":"select user();",

}.items()}





