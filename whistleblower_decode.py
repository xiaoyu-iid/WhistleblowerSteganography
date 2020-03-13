#!/usr/bin/env python3

###############################################################################
#
# stegno_decode.py decodes hidden text in joshua_tree.png.
# 
# joshua_tree.png used the Least Significant Bit (LSB) technique. In 
# joshua_tree.png, each pixel has three values (RGB). The rightmost bits of 
# each value are replaced by the hidden message.
#
# PNG formats are used as PNG files are lossless compressed images.
#
# You will need the Pillow module (pip install Pillow).
#
# 隐写内容为《人物》杂志公众号文章《发哨子的人》。
# 文｜龚菁琦
# 编辑｜金石
# 摄影｜尹夕远
#
# joshua_tree.png by JW
#
###############################################################################

from PIL import Image
import base64

# stores all binary bits
extracted_text = ""

# retracts LSB from every pixel
with Image.open("joshua_tree.png") as image:
    width, height = image.size
    for x in range(0, width):
        for y in range(0, height):
            pixel = list(image.getpixel((x, y)))
            for n in range(0,3):
                extracted_text += str(pixel[n]&1)

# binary->base64->text, write to file decode_text.txt
file = open("decode_text.txt", "wb")
file.write(base64.b64decode("".join([chr(int(x, 2)) for x in [extracted_text[i:i+8] for i in range(0, len(extracted_text), 8)]])))

# EOF
