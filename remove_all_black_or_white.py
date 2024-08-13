from  PIL import Image 
import os
  
# opening a multiband image

categories = []
for cat in os.listdir("CAD_Files\stl"):
      categories.append(str(cat[0:-4]))
for cat in categories:
    for image in os.listdir(fr'images\zoom\{cat}'):
        im = Image.open(fr'images\zoom\{cat}\{image}') 
        extrema = im.convert("L").getextrema()
        if extrema == (0, 76) or extrema == (76,255):
            print(f"entire {image}")
            os.remove(fr'images\zoom\{cat}\{image}')
