import requests
import random
import urllib.parse

url = "https://www.text-to-speech.cn/getSpeek.php"

user_agent_list = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
]

headers = {
    "User-Agent": random.choice(user_agent_list),
    "Cookie": urllib.parse.quote("Hm_lvt_b38a22175a63114a18d55183d7ddb4c4=1685196094,1686657997; Hm_lpvt_b38a22175a63114a18d55183d7ddb4c4=1686657997; language=ä¸­æ–‡ï¼ˆæ™®é€šè¯ï¼Œç®€ä½“ï¼‰; voice=zh-CN-YunxiNeural; kbitrate=audio-16khz-32kbitrate-mono-mp3; role=0; style=assistant; speed=0; pitch=0", safe='')}

data = {
    "language": "中文（普通话，简体）",
    "voice": "zh-CN-YunxiNeural",
    "text": "IGMP（Internet Group Management Protocol）是一种用于在IP网络中管理组播组的协议。它允许主机和路由器之间通信，以便确定哪些主机属于哪些组播组。IGMP还允许主机加入或离开组播组，并通知路由器有关组播组成员的变化。IGMP可以帮助网络管理员有效地管理组播流量，提高网络性能和可靠性。",
    "role": "0",
    "style": "assistant",
    "rate": "0",
    "pitch": "0",
    "kbitrate": "audio-16khz-32kbitrate-mono-mp3",
    "silence": "",
    "styledegree": "2",
}

response = requests.post(url, headers=headers, data=data)
print(response.text)


# 修改上述代码 把正在语音播放的文字用黄色背景标记出来，播放完毕后再取消背景

