import os
from 调用此函数生成最终语音字符串 import final
file_name = os.path.basename(__file__)[2:-3]

def p_s():
    p_ = {key + ' (' + file_name + ')': value for key, value in {
        

    }.items()}
    return p_

if __name__ == "__main__":
    final(p_s())



