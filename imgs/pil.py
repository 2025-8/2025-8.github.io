from PIL import Image

# 打开图像
image = Image.open("cb.png")
image=image.convert('RGBA') 
# 获取图像的宽度和高度
width, height = image.size

# 遍历每个像素
for x in range(width):
    for y in range(height):
        # 获取像素RGB值
        r, g, b,a = image.getpixel((x, y))

        # 检查是否为白色像素
        if r >= 200 and g >= 200 and b >= 200:
            # print(111)
            # 将透明度设置为0
            image.putpixel((x, y), (0, 0, 0, 0))
        else:
            image.putpixel((x,y),(r+50,b+50,g+50,1000))

image.save('1.png')