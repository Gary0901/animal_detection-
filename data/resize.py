from PIL import ImageGrab
from PIL import Image

img = Image.open('')   # 截图
width = img.size[0]   # 获取宽度
height = img.size[1]   # 获取高度
img = img.resize((int(width*0.3), int(height*0.3)), Image.ANTIALIAS)
img.save("love.jpg")

