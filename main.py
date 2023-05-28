

import random,re,os 

# 获取当前目录下所有以"操作"开头的py文件
files = [f for f in os.listdir('.') if f.startswith('操作') and f.endswith('.py')]

# 已经练习的项目列表
has_lear=[]
try:
    while files:
        # 去掉文件名中的"操作"和".py"后缀
        file_names = [f[2:-3] for f in files]
        
        # 给每个文件名前面加上序号
        file_list = []
        for i, f in enumerate(file_names, 1):
            file_list.append(f'{i}. {f}')
        
        # 打印文件列表
        print('涉及: '+','.join(file_list))
        
        # 用户输入对应的序号
        while True:
            num = input("\n请输入要练习的序号(逗号): ")
            numbers = num.split(",")
            if not all(number.isdigit() for number in numbers):
                print("你输入的不是数字,请重新输入!")
                continue
            break
        num = eval(num)
        # 如果只输入一个数值的话
        if type(num) == int:
            num = [num]
        # print(num)
        var_names=[]
        var_list = []
        key_list = []
        var_value={}
        # 导入对应的py文件以v_开头的变量
        if min(num) > 0 and max(num) <= len(files):
            # 本次选择的项目变量
            choice_list=[]
            for k in num:
                module_name = files[k - 1][:-3]  # 去掉".py"后缀
                has_lear.append(module_name[2:])
                choice_list.append(module_name[2:])
                module = __import__(module_name)
                # print('你选择的是: ' + module_name[2:])
                # 获取以"p_"开头的变量名列表
                # var_names =[var_name for var_name in dir(module) if var_name.startswith('p_')]
                
                var_na =[getattr(module, var_name) for var_name in dir(module) if var_name.startswith('p_')]
                for i in var_na:
                    varna2=i()
                    # print(varna2)
                var_names = [(key, value) for key, value in varna2.items()]
                    
                # print(var_names)
                # 给每个变量名前面加上序号
                # var_list = []
                var_value=varna2
                # for i, var_name in enumerate(var_names, 1):
                    # var_value2 = getattr(module, var_name)
                    # var_value.update(var_value2)
                    
                    # print(var_value)    # p_字典列表
                    # 给每个key前面加上序号
                    # key_list = []
                for j, key in enumerate(var_value.keys(), 1):
                    key_list.append(f'{j}. {key}: {var_value[key]}')
                        # key_list.append(f'{j}. {key}')
                # print(list(var_value.keys()))
            print('你选择的是: ' + ','.join(choice_list))
            print('总共有' + str(len(list(var_value.keys()))) + '个问题')
        # else:
        #     print('输入的序号无效')
            # print(key_list)
            n=1
            while list(var_value.keys()):
                # 随机选择一个问题
                random_question = random.choice(list(var_value.keys()))
                # 获取用户输入
                user_input = input("\n问题" + str(n) + ": " + random_question + "\n你的输入: ")
                while not user_input:
                    user_input = input("输入不能为空,请重新输入: ")
                n += 1
            
                # 输出对应的答案
                print("答案:    " + var_value[random_question])
            
                # 判断用户输入是否跟答案一致
                s1 = user_input
                s2 = var_value[random_question]
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
                    print('回答正确 ' + '\033[31m' + '√' + '\033[0m')
                else:
                    print('回答错误 ' + '\033[32m' + '×' + '\033[0m')
                    user_input = input("照着答案再写一遍: ")
            
                # 从字典中删除已经回答过的问题
                del var_value[random_question]
                # print("剩余:"+str(len(list(var_value.keys()))))
            print("\nSuccess," + str(n - 1) + "个问题全部答完,继续加油哦!")
            # has_lear=list(set(has_lear))
            print('已经练习的项目是: '+','.join(has_lear))
            while True:
                num = input("是否需要重新练习 1是 0否: ")
                print('')
                if num =='0':
                    for i in has_lear:
                        try:
                            files.remove('操作' + i + '.py')
                        except ValueError:
                            pass
                    break
                elif num == '1':
                    for i in choice_list:
                        has_lear.remove(i)
                    break
                else:
                    continue
            
            del var_names,module
        else:
            print('输入的序号无效,请重新输入\n')
        
    print('\nSuccess,所有项目都练习完了!')
except KeyboardInterrupt:
    pass




