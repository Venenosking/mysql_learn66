


# 涉及: 1. 分区表,2. 存储过程,3. 数据,4. 数据库,5. 数据表,6. 权限管理,7. 用户管理,8. 索引,9. 视图,10. 角色管理
# 选择要生成的是哪个序号内容,输入数字选择,然后导入该序号的v_开头(把p_开头的字典复制一份出来给v_开头的字典)的字典数据获取它的Key(这里需要分类一下,不然key太多,不好找),然后输入数字选择要生成的key内容,获取key的内容后,判断出内容里面包含的中文,然后提示用户输入对应的中文内容
# alter table 表名 add partition partitions 数字;
# user_input = input("生成Hash分区表: ")

import random,re,os
import mysql.connector
g_module=[]
# 获取当前目录下以 操作 开头的py文件,并且导入它们的全部内容
current_dir = os.getcwd()
def get_import(current_dir):
    # 获取当前目录
    # current_dir = os.getcwd()
    # 遍历当前目录下的所有文件
    for file_name in os.listdir(current_dir):
        # 判断文件名是否以 "操作" 开头，且是 .py 文件
        if file_name.startswith("操作") and file_name.endswith(".py"):
            # 导入该文件的全部内容
            module_name = file_name[:-3]  # 去掉文件扩展名 .py
            g_module.append(module_name[2:])
    for i, item in enumerate(g_module):
        g_module[i] = f"{i + 1}. {item}"
            
            # module = __import__(module_name)
            # globals().update(vars(module))
# 获取p_开头的变量
def get_var():
    # 创建一个字典，包含问题和答案
    qa_dict = {}
    # 获取当前作用域中的所有变量
    all_vars = globals()
    # 使用列表推导式筛选以 'p_' 开头的变量并获取它们的值并添加到列表中
    p_list = [all_vars[var] for var in all_vars if var.startswith('p_')]
    # print(p_list)
    for i in p_list:
        qa_dict.update(i)
    # print('总共有'+str(len(qa_dict))+'个问题')
    # print('涉及: '+','.join(g_module))
    
    # 给列表添加序号
    # for i, item in enumerate(g_module):
    #     g_module[i] = f"{i+1}. {item}"
    # print(g_module)
    print('快速生成: '+','.join(g_module))

last_learn=[]
error_str=''
ture_str=1
user_input=''

new_g_module = []
def get_number(item):
    return int(item.split('.')[0])
# 获取输入的数字
def get_input(ture_str):
    while ture_str:
        while True:
            user_input = input("\n请输入要快速生成的序号(逗号): ")
            numbers = user_input.split(",")
            if not all(number.isdigit() for number in numbers):
                print("你输入的不是数字,请重新输入!")
                continue
            break
    
        user_input = eval(user_input)
        # print(user_input)
        # 如果只输入一个数值的话
        if type(user_input) == int:
            user_input = [user_input]
        # 判断输入的序号最大值和最小值都在g_module列表的最大值和最小值范围之内
        # 找到列表中的最大值和最小值
        max_item = max(g_module, key=get_number)
        min_item = min(g_module, key=get_number)
    
        # print("最大值：", max_item)
        # print("最小值：", min_item)
    
        if max(user_input) <= int(re.findall(r'\d+', max_item)[0]) and min(user_input) >= int(
                re.findall(r'\d+', min_item)[0]):
            ture_str = 0
        else:
            print('你输入的序号不在范围之内,重新输入!')
    return user_input
# 输出用户选择的内容
def get_choice(new_g_module,last_learn):
    # 判断序号对应的问题
    for i in user_input:
        # print(i)
        for j in g_module:
            if int(i) == int(re.findall(r'\d+', j)[0]):
                # print(j)
                new_g_module.append(j)
    # print(new_g_module)
    # 末尾输出练习的项目
    last_learn = new_g_module + last_learn
    # for i in new_g_module:
    #     last_learn.append(i)
    
    new_g_module = [item.split('. ')[1] for item in new_g_module]
    print('你选择快速生成: ' + ','.join(new_g_module))

if __name__ == "__main__":
    # get_import(current_dir)                      # 获取当前目录下以 操作 开头的py文件,并且导入它们的全部内容
    # get_var()                                  # 获取p_开头的变量
    # user_input=get_input(ture_str)             # 获取输入的数字
    # get_choice(new_g_module,last_learn)        # 输出用户选择的内容
    
    # print('快速生成: '+','.join(g_module))
    # user_input = get_input(ture_str)  # 获取输入的数字
    # # print(user_input)
    # get_choice(new_g_module, last_learn)  # 输出用户选择的内容
    
    # Python程序,找出当前目录下以操作开头的py文件,找出来以后把它们的文件名去掉py后缀和操作这两个字,然后放在一个列表里面,并给每个文件名前面加上一个序号,然后用户输入对应的序号,就导入对应的py文件以v_开头的变量,然后给这个变量的key加上序号,再把key打印出来,当用户输入对应的序号,则输出对应的Key内容

    import os

    # 获取当前目录下所有以"操作"开头的py文件
    files = [f for f in os.listdir('.') if f.startswith('操作') and f.endswith('.py')]

    # 去掉文件名中的"操作"和".py"后缀
    file_names = [f[2:-3] for f in files]

    # 给每个文件名前面加上序号
    file_list = []
    for i, f in enumerate(file_names, 1):
        file_list.append(f'{i}. {f}')

    # 打印文件列表
    print(','.join(file_list))

    # 用户输入对应的序号
    num = int(input('请输入对应的序号: '))

    # 导入对应的py文件以v_开头的变量
    if num > 0 and num <= len(files):
        module_name = files[num - 1][:-3]  # 去掉".py"后缀
        print('你选择的是: '+module_name[2:])
        module = __import__(module_name)

        # 获取以"v_"开头的变量名列表
        var_names = [var_name for var_name in dir(module) if var_name.startswith('v_')]

        # 给每个变量名前面加上序号
        var_list = []
        for i, var_name in enumerate(var_names, 1):
            var_value = getattr(module, var_name)

            # 给每个key前面加上序号
            key_list = []
            for j, key in enumerate(var_value.keys(), 1):
                # key_list.append(f'{j}. {key}: {var_value[key]}')
                key_list.append(f'{j}. {key}')

            # 打印key列表
            # print(f'{i}. {var_name}:')
            print('\n'.join(key_list))

            # 用户输入对应的序号
            key_num = int(input('请输入对应的序号: '))

            # 输出对应的Key内容
            if key_num > 0 and key_num <= len(var_value):
                key = list(var_value.keys())[key_num - 1]
                print(f'{key}: {var_value[key]}'+'\n')
            else:
                print('输入的序号无效')
    else:
        print('输入的序号无效')

# Python程序,循环遍历出字符串中的所有中文,并且一个中文到下一个空格为止才能算一个中文,并且每找到一个中文,就提示用户输入一个值来替换这个中文
    import re
    def replace_chinese_chars(string):
        pattern = re.compile('([\u4e00-\u9fa5]+)\d*')
        while True:
            match = pattern.search(string)
            if match is None:
                break
            # chinese_chars = match.group(1)
            chinese_chars = match.group(0)
            replacement = input(f'请为中文"{chinese_chars}"输入一个替换值: ')
            
            string = string[:match.start(1)] + replacement + string[match.end(0):]
            print('    '+string)
        return string

    new_string = replace_chinese_chars(var_value[key])
    print('最终的命令是:    '+new_string+'    '+key+'')
    input("输入任意键将在Mysql中执行该命令...\n")
    # 这里写下一步操作的代码

    # python程序,如何在cmd中运行字符串'alter table xie coalesce partition 8;'
#     import mysql.connector

    # 连接MySQL数据库
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='123456',
        database='stu_tea'
    )

    # 执行SQL查询
    cursor = connection.cursor()
    # cursor.execute('SELECT * FROM customers')
    try:
        cursor.execute(new_string)
    except:
        print('命令运行错误!\n')
    # result = cursor.fetchall()
    
    cursor.execute('show create table t4 ;')
    result = cursor.fetchall()
    # 打印查询结果
    for row in result:
        print(row)

    # 关闭数据库连接
    connection.close()




