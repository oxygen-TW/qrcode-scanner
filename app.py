import pyzbar.pyzbar as pyzbar
from PIL import Image, ImageGrab
import argparse
import sys
from os import remove
import clipboard

#參數解析
parser = argparse.ArgumentParser()

parser.add_argument("-c","--clipboard", help="Decode QR code from clipboard", action='store_true')
parser.add_argument("-i","--image", help="Decode QR code from image", default="", type=str)
parser.add_argument("-b","--copyback", help="If you want copy decode text to clipboard.", action='store_true')

args = parser.parse_args()

imgPath = "tmp.png"

if(args.clipboard):
    try:
        im = ImageGrab.grabclipboard()
        im.save(imgPath)
    except AttributeError:
        print("Failed to load image from clipbiard!")
        input("Press any key to continue...")
        sys.exit(1)
else:
    if(args.image != ""):
        try:
            im = Image.open(args.image)
            im.save(imgPath)
        except FileNotFoundError:
            print("Failed to load image from image path!")
            input("Press any key to continue...")
            sys.exit(1)
    else:
        print("Image path error.")

#讀取與解碼
img = Image.open(imgPath)
texts = pyzbar.decode(img)

if(texts == []):
    print("Failed to decode QR code!")
    input("Press any key to continue...")
    sys.exit(2)

for text in texts:
    line = text.data.decode("utf-8")
    print(line)

    if(args.copyback):
        clipboard.copy(line)
        print("Text has copied to clipboard!")

input("Press any key to continue...")

#刪除暫存圖片 提升安全性考量
try:
    remove(imgPath)
except FileNotFoundError:
    pass