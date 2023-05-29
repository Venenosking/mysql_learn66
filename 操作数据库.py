
import os, re
from 生成语音 import ai_reader_value
file_name = os.path.basename(__file__)[2:-3]

def p_databases():
    p_database = {key + ' (' + file_name + ')': value for key, value in {
       "删除数据库": "drop database 数据库名称;",
       "创建数据库": "create database 数据库名称;",
       "使用某个数据库": "use 数据库名称;",
       "查看所有数据库": "show databases;",
       "查看当前数据库": "select database(); ",
       "查看某个数据库的创建信息": "show create database 数据库名称; ",
       "查看当前用户": "select user();",
       "查看数据库的字符编码 2种方式": "1.用navicat右击数据库名称,选择编辑数据库 2.alter database 数据库名称 character set 字符编码名称 collate 检验规则名称",
       "修改数据库名称 3种方式": "1.先把表导出来,再导入新的数据库 2.先创建一个新数据库,然后将源数据库下的表重命名到新的数据库下 rename table 旧数据库.表名 to 新数据库.表名 3.create table 新数据库名称.源数据库表 like 源数据库名称.源数据库表; 但是有弊端,只有表结构没有表数据",

    }.items()}
    return p_database


if __name__ == "__main__":
    # -------------------------------生成AI语音字符串-------------------------------------------------
    # 去掉key中的()
    a_part = {re.sub(r'\([^)]*\)', '', key): value for key, value in p_databases().items()}
    # 遍历字典,生成AI语音字符串
    for key, value in a_part.items():
        value = ai_reader_value(value)
        if "/" in key:
            key = key.replace("/", "或者")  # 把/替换成 或者
        key = '((⏱️=1500))' + key
        print('\n', key, value)
    print('\n一共有 ' + str(len(a_part)) + ' 个'+' '+str(len(p_databases())))









