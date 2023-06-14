from PIL import Image, ImageEnhance, ImageOps, ImageFilter

def enhance_colors_with_edge_detection(image_path, saturation_factor, brightness_factor, contrast_factor):
    # 打开图像文件
    image = Image.open(image_path)

    # 转换为RGB模式
    rgb_image = image.convert('RGB')

    # 创建颜色增强器
    enhancer = ImageEnhance.Color(rgb_image)

    # 调整色彩饱和度
    enhanced_image = enhancer.enhance(saturation_factor)

    # 创建亮度增强器
    enhancer = ImageEnhance.Brightness(enhanced_image)

    # 调整亮度
    enhanced_image = enhancer.enhance(brightness_factor)

    # 直方图均衡化
    # enhanced_image = ImageOps.equalize(enhanced_image)

    # 创建对比度增强器
    enhancer = ImageEnhance.Contrast(enhanced_image)

    # 调整对比度
    enhanced_image = enhancer.enhance(contrast_factor)

    # 应用边缘检测滤波器
    # edge_image = enhanced_image.filter(ImageFilter.FIND_EDGES)

    # 保存处理后的图像
    enhanced_image.save('999new.jpg')

# 使用示例
enhance_colors_with_edge_detection('999.jpg', saturation_factor=8, brightness_factor=4, contrast_factor=2.5)
