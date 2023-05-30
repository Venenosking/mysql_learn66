import os
from 调用此函数生成最终语音字符串 import final
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
        "修改数据库的字符编码 有2种方式": "第一种 用navicat 右击数据库名称,选择编辑数据库 第二种 alter database 数据库名称 character set 字符编码名称 collate 检验规则名称",
        "修改数据库名称 有3种方式": "第一种 先把表导出来,再导入新的数据库 第二种 先创建一个新数据库,然后将源数据库下的表重命名到新的数据库 rename table 旧数据库.表名 to 新数据库.表名 第三种 create table 新数据库名称.源数据库表 like 源数据库名称.源数据库表; 但是有弊端,只有表结构没有表数据",

    }.items()}
    return p_database

if __name__ == "__main__":
    final(p_databases())

'((⏱️=1500))修改数据库的字符编码 有2种方式  ((⏱️=1500))第一种((⏱️=800))用navicat忑((⏱️=800))恩 a v i((⏱️=800)) c a t((⏱️=800))右击数据库名称((⏱️=400))然后((⏱️=400))选择编辑数据库((⏱️=800))第二种((⏱️=800))alter((⏱️=800))database((⏱️=800))数据库名称((⏱️=800))character((⏱️=800))set忑((⏱️=800))字符编码名称((⏱️=800))collate((⏱️=800))c o l l((⏱️=800)) a t e((⏱️=800))检验规则名称((⏱️=800))'

