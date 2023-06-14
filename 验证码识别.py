import easyocr,re

# 创建 EasyOCR 对象并加载预训练模型
reader = easyocr.Reader(['en'],recog_network='english_g2')

# 读取验证码图片
image_path = '777new.jpg'
# captcha_image = easyocr.input.Image(image_path)

# 进行验证码识别
result = reader.readtext(image_path,detail = 0)
# print(result)
result=''.join(result).replace(' ','')
pattern = r"\d+"  # 正则表达式模式，匹配一个或多个数字
matched_numbers = re.findall(pattern, result)
result=''.join(matched_numbers).replace(' ','')
print(result)





 
