import re
from 生成语音 import ai_reader_value


# -----------------生成AI语音字符串-------------------------------------------------
# 去掉key中的()
def final(p_views):
    # print(p_views.items())
    pp=p_views.items()
    # for i,j in p_views.items():
    #     print(i,j)
    a_part = {re.sub(r'\([^)]*\)', '', key): value for key, value in pp}
    # 遍历字典,生成AI语音字符串
    for key, value in a_part.items():
        value = ai_reader_value(value)
        if "/" in key:
            key = key.replace("/", "或者")  # 把/替换成 或者
        key = '((⏱️=1500))' + key
        print('\n', key, value)
    print('\n一共有 ' + str(len(a_part)) + ' 个'+' '+str(len(pp)))



