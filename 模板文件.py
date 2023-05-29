import os, re
from 生成语音 import ai_reader_value
file_name = os.path.basename(__file__)[2:-3]

def p_s():
    p_ = {key + ' (' + file_name + ')': value for key, value in {
            

    }.items()}
    return p_


if __name__ == "__main__":
    # -------------------------------生成AI语音字符串-------------------------------------------------
    # 去掉key中的()
    a_part = {re.sub(r'\([^)]*\)', '', key): value for key, value in p_s().items()}
    # 遍历字典,生成AI语音字符串
    for key, value in a_part.items():
        value = ai_reader_value(value)
        if "/" in key:
            key = key.replace("/", "或者")  # 把/替换成 或者
        key = '((⏱️=1500))' + key
        print('\n', key, value)
    print('\n一共有 ' + str(len(a_part)) + ' 个'+' '+str(len(p_s())))



