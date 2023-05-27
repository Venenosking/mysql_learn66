# 51 47


import pygame

# 初始化pygame
pygame.init()

# 加载mp3文件
pygame.mixer.music.load('测试.mp3')

# 播放mp3文件
pygame.mixer.music.play()

# 等待音频播放完毕
while pygame.mixer.music.get_busy():
    continue

# 退出pygame
pygame.quit()

