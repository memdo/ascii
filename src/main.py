from PIL import Image

image = Image.open("src/image.jpg")
image = image.convert("L")

max_height = 30
ratio = 2.5

x = image.width
y = image.height

image = image.resize((int(x/y*max_height*ratio), max_height), Image.ANTIALIAS)
