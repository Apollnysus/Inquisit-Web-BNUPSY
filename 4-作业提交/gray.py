#created by Jiting Liu 11/29/2016

from PIL import Image
import os

work_dir = os.getcwd()
print os.getcwd()

im = Image.open(work_dir+'/common.jpg')

i=0
for i in range(0,16):
     pix = im.load()
     width = im.size[0]
     height = im.size[1]
     for x in range(width):
         for y in range(height):
             r, g, b = pix[x, y]
             r = (r* 30 +g* 59+b*11+50)/100
             r = r+1*i
             g = r+1*i
             b = r+1*i
             pix[x,y]=r,g,b
     im.save(work_dir+'/'+str(i)+'.bmp')
