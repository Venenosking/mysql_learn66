


# 涉及: 1. 分区表,2. 存储过程,3. 数据,4. 数据库,5. 数据表,6. 权限管理,7. 用户管理,8. 索引,9. 视图,10. 角色管理
# 选择要生成的是哪个序号内容,输入数字选择,然后导入该序号的v_开头(把p_开头的字典复制一份出来给v_开头的字典)的字典数据获取它的Key(这里需要分类一下,不然key太多,不好找),然后输入数字选择要生成的key内容,获取key的内容后,判断出内容里面包含的中文,然后提示用户输入对应的中文内容
# alter table 表名 add partition partitions 数字;
# user_input = input("生成Hash分区表: ")

import random,re,os
g_module=[]
# 获取当前目录下以 操作 开头的py文件,并且导入它们的全部内容
def get_import():
    # 获取当前目录
    current_dir = os.getcwd()
    # 遍历当前目录下的所有文件
    for file_name in os.listdir(current_dir):
        # 判断文件名是否以 "操作" 开头，且是 .py 文件
        if file_name.startswith("操作") and file_name.endswith(".py"):
            # 导入该文件的全部内容
            module_name = file_name[:-3]  # 去掉文件扩展名 .py
            g_module.append(module_name[2:])
            module = __import__(module_name)
            globals().update(vars(module))
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
    for i, item in enumerate(g_module):
        g_module[i] = f"{i+1}. {item}"
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
    get_import()        # 获取当前目录下以 操作 开头的py文件,并且导入它们的全部内容
    get_var()           # 获取p_开头的变量
    user_input=get_input(ture_str)             # 获取输入的数字
    get_choice(new_g_module,last_learn)        # 输出用户选择的内容
    
    
    