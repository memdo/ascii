from PIL import Image

image = Image.open("src/image.jpg")
image = image.convert("L")


characters = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$" 
max_height = 50
ratio = 2.5
output = ""

x = image.width
y = image.height

image = image.resize((int(x/y*max_height*ratio), max_height), Image.ANTIALIAS)

for h in range(image.height):
    for w in range(image.width):
        print(w, h)
        brightness = 255 - image.getpixel((w, h))
        output += characters[brightness // 4]
    output += "\n"

print(output)
