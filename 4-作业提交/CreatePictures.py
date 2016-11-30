# 导入所需模块库

from PIL import Image

from PIL import ImageDraw

from PIL import ImageFont

work_dir = "E:/实心实验/Python&Inquisit/"
ra=(0,1,2,3,4)
for p in ra:
    m = p * 10
    gray_image = Image.new("RGB", size=(1000, 1000), color=(m,m,m))
    txt = "A"
    font = ImageFont.truetype("C:/Windows/Fonts/Arial.ttf", size=400)
    draw = ImageDraw.Draw(gray_image , mode="RGB")
# 告诉计算机我们在什么位置画，画什么，用什么颜色，用什么字体！
    draw.text((300, 300), txt, fill=(255,255,255), font=font)
# 把图片从内存保存到硬盘吧，注意我们要存放在什么文件夹中！
    name = "A"+str(p)+".jpg"
    gray_image.save(work_dir + name, "bmp")
    gray_image = Image.open(work_dir+name)
#crop pictures
    blank_image = Image.open(work_dir + name)
    out = blank_image.crop(box=(55, 113, 855, 913))
    out.save(work_dir + name)


