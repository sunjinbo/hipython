from PIL import Image
from PIL import ImageDraw
from shape import Shape as SHAPE
import random


def createImage(width, height, shape, rgb):
    img = Image.new("RGB", (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    x = random.randint(0, width / 2)
    y = random.randint(0, height / 2)
    w = random.randint(x, width) - x
    h = random.randint(y, height) - y
    if shape == SHAPE.Rectangle:
        draw.rectangle([x,y,x+w,y+h], rgb, rgb)
        img.save("I:/tensorflow/train/rect_" + str(x) + "_" + str(y) + "_" + str(w) + "_" + str(h) + ".jpg")
        pass
    elif shape == SHAPE.Oval:
        draw.ellipse([x,y,x+w,y+h], rgb)
        img.save("I:/tensorflow/train/oval_" + str(x) + "_" + str(y) + "_" + str(w) + "_" + str(h) + ".jpg")
        pass
    else:
        pass

