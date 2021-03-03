from PIL import Image, ImageDraw, ImageFont, ImageFilter
import sys, os

if(len(sys.argv) !=4):
    print("{} <v|h> <folder path> <output name>".format(sys.argv[0]))
    sys.exit(1)

choice = sys.argv[1]
imgdir = sys.argv[2]
exts = ["png", "jpg", "jpeg"]
ws = []
hs = []
for i in os.listdir(imgdir):
    if(i.endswith('jpg') or i.endswith('png')):
        im = Image.open(os.path.join(imgdir, i)).convert('RGBA')
        ws.append(im.width)
        hs.append(im.height)

if(sys.argv[1] == 'v'):
    w = max(ws)
    h = sum(hs)
else:
    w = sum(ws)
    h = max(hs)
im = Image.new(size=(w, h), mode="RGBA")
c = 0
for i in sorted(os.listdir(imgdir)):
    if(i.endswith('jpg') or i.endswith('png')):
        print("Joining image", i)
        ip = Image.open(os.path.join(imgdir, i)).convert('RGBA')
        if(sys.argv[1] == 'v'):
            p = sum(hs[:c])
            im.paste(ip, (0, p))
            c += 1
        else:
            p = sum(ws[:c])
            im.paste(ip, (p, 0))
            c += 1
out = os.path.join(os.getcwd(), sys.argv[3])
im.save(out)
print("Image saved at", out)
