# needs PIL image library: "pip install pillow"

from PIL import Image

maxCount = 255
imgSize = (512, 512)
reRange = (-2.0, 0.5)
imRange = (-1.25, 1.25)
reStep = (reRange[1] - reRange[0]) / float(imgSize[0])
imStep = (imRange[1] - imRange[0]) / float(imgSize[1])

def iterate(z0):
    count = 0
    z = z0
    while abs(z) <= 2.0 and count < maxCount:
        z = z ** 2 + z0
        count += 1
    return count

def draw():
    for y in range(imgSize[1]):
        for x in range(imgSize[0]):
            re = reRange[0] + reStep * x
            im = imRange[0] + imStep * y
            count = iterate(complex(re, im))
            r = (count * 8) & 255
            g = r
            b = r
            img.putpixel((x, y), (r, g, b))

img = Image.new('RGB', imgSize)
draw()
img.save('mandelbrot.png')
