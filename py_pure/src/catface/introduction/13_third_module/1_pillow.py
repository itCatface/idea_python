# -pillow[python的]
from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random

# 打开图片
image = Image.open('../../introduction_dir/girl.jpg')

# 输出图片原始宽高
w, h = image.size
print('Original image size: %s * %s' % (w, h))

# 调整图片宽高并保存(缩放)
image.thumbnail((w // 2, h // 2))
print('Original image size: %s * %s' % (w // 2, h // 2))
image.save('../../newDir/girl_copy.jpg', 'jpeg')

# 图片模糊操作并保存
image = image.filter(ImageFilter.BLUR)
image.save('../../newDir/girl_blur.jpg', 'jpeg')


# -验证码
# 随机字母
def rnd_char():
    return chr(random.randint(65, 90))


# 随机颜色1
def rnd_color():
    return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)


# 随机颜色2
def rnd_color2():
    return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)


# 240 x 60
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象
font = ImageFont.truetype('C:\Windows\Fonts\BRUSHSCI.TTF', 36)
# 创建Draw对象
draw = ImageDraw.Draw(image)
# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rnd_color())
# 输出文字
for t in range(4):
    draw.text((60 * t + 10, 10), rnd_char(), font=font, fill=rnd_color2())
# 模糊
image = image.filter(ImageFilter.BLUR)
image.save('../../newDir/code.jpg', 'jpeg')
