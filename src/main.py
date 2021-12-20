from PIL import Image

image = Image.open("src/image.jpg")
image = image.convert("L")
