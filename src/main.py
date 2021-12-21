"""
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from PIL import Image

image = Image.open("src/image.jpg")
image = image.convert("RGB")

characters = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$" 
max_height = 50
ratio = 2.5
items = []
output = ""

x = image.width
y = image.height

image = image.resize((int(x/y*max_height*ratio), max_height), Image.ANTIALIAS)

for i in image.getdata():
    items.append(i)

for h in range(image.height):
    for w in range(image.width):
        item = items[h*image.width + w]
        brightness = int(0.21 * item[0] + 0.72 * item[1] + 0.07 * item[2])
        output += characters[brightness // 4]
    output += "\n"

print(output)
