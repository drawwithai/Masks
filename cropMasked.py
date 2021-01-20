# #!/usr/local/bin/python3
# import numpy as np
# from PIL import Image, ImageDraw
#
# # Open the input image as numpy array, convert to RGB
# img=Image.open("rose.png").convert("RGB")
# npImage=np.array(img)
# h,w=img.size
#
# # Create same size alpha layer with circle
# alpha = Image.new('L', img.size,0)
# draw = ImageDraw.Draw(alpha)
# draw.pieslice([0,0,500,500],90,360,fill=255)
#
# # Convert alpha Image to numpy array
# npAlpha=np.array(alpha)
#
# # Add alpha layer to RGB
# npImage=np.dstack((npImage,npAlpha))
#
# # Save with alpha
# Image.fromarray(npImage).save('cropped.png')
from PIL import Image

img = Image.open('result.png')
img = img.convert("RGBA")
datas = img.getdata()

newData = []
for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

img.putdata(newData)
img.save("cropped.png", "PNG")
