from PIL import Image

brightness_to_char = " .'^*#@$"

with Image.open('Random-Img.png') as im:
    im.show()
