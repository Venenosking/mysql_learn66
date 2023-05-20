
# 写一个Python程序,先把问题分类,然后从里面随便抽取一个问题,然后获取用户输入,用户输入完之后,在把对应的答案输出来,循环上述操作,直到所有问题都被抽取完
# 写一个Python程序,查看当前目录下是否有操作开头的py文件,有的话就导入该文件的全部内容
import random,re
# from 操作数据表 import *
# from 操作视图 import *
g_module=[]
import os
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

print('涉及: '+','.join(g_module))
new_g_module=[]
error_str=''
ture_str=1
user_input=''
while ture_str:
    user_input = input("\n请输入要练习的序号(逗号): ")
    user_input = eval(user_input)
    # print(user_input)
    # 如果只输入一个数值的话
    if type(user_input)==int:
        user_input = [user_input]
    # 判断输入的序号最大值和最小值都在g_module列表的最大值和最小值范围之内
    if max(user_input) <= int(re.findall(r'\d+', max(g_module))[0]) and min(user_input) >= int(re.findall(r'\d+', min(g_module))[0]):
        ture_str=0
    else:
        print('你输入的序号不对,重新输入!')
        

# 判断序号对应的问题
for i in user_input:
    # print(i)
    for j in g_module:
        if str(i) in j:
            # print(j)
            new_g_module.append(j)
# print(new_g_module)
# 末尾输出练习的项目
last_learn=[]
last_learn=new_g_module

new_g_module = [item.split('. ')[1] for item in new_g_module]
print('你所选择练习项目是: '+','.join(new_g_module))
qa_dict_list=[]
# print(list(qa_dict.keys()))

for j in list(qa_dict.keys()):
    for i in new_g_module:
        if i in j:
            qa_dict_list.append(j)
# print(qa_dict_list)
print('总共有'+str(len(qa_dict_list))+'个问题')
    
    
    
# 循环抽取问题和输出答案
n=1
error_list=[]
while qa_dict_list:
    # 随机选择一个问题
    random_question = random.choice(qa_dict_list)
    # 获取用户输入
    user_input = input("\n问题"+str(n)+": "+random_question+"\n你的输入: ")
    while not user_input:
        user_input = input("输入不能为空,请重新输入: ")
    n+=1

    # 输出对应的答案
    print("答案:    "+qa_dict[random_question])

    # 判断用户输入是否跟答案一致
    s1=user_input
    s2=qa_dict[random_question]
    # 使用正则表达式提取字符串中的英文部分
    pattern = re.compile('[a-zA-Z]+')
    s1_english = pattern.findall(s1)
    s2_english = pattern.findall(s2)

    # 将英文部分连接成字符串并转换为小写进行比较
    s1_combined = ''.join(s1_english).lower()
    s2_combined = ''.join(s2_english).lower()
    # print('\033[31m'+'hello'+'\033[0m') 字体颜色
    # 判断两个字符串是否相等
    if s1_combined == s2_combined:
        print('回答正确 '+'\033[31m'+'√'+'\033[0m')
    else:
        print('回答错误 '+'\033[32m'+'×'+'\033[0m')
        user_input = input("照着答案再写一遍: ")

    # 从字典中删除已经回答过的问题
    # del qa_dict[random_question]
    qa_dict_list.remove(random_question)
# print("\n")
print("\nSuccess,"+str(n-1)+"个问题全部答完,继续加油哦!")
print('此次练习的项目是: '+','.join(last_learn))


