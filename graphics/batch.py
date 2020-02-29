from img import createImage
from array import array
from shape import Shape as SHAPE
import random


colors = [(255, 0, 0), (255, 255, 0), (0, 255, 0), (0, 255, 255), (0, 0, 255)]

if __name__ == "__main__":
    for i in range(0, 500):
        print("create an image " + str(i))
        rand = random.randint(1, 250)
        index = random.randint(0, len(colors) - 1)
        rgb = colors[index]
        if rand <= 50:
            createImage(100, 100, SHAPE.Rectangle, rgb)
        else:
            createImage(100, 100, SHAPE.Oval, rgb)
