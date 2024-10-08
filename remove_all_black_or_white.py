from  PIL import Image 
import os
  
# opening a multiband image

categories = [str(cat[0:-4]) for cat in os.listdir("CAD_Files\stl")]

def remove_images(path, cat, image):
    im = Image.open(fr'{path}\{cat}\{image}') 
    extrema = im.convert("L").getextrema()
    if extrema != (0, 255):
        os.remove(fr'{path}\{cat}\{image}')


# for cat in categories:
#     for image in os.listdir(fr'images\zoom\{cat}'):
#         im = Image.open(fr'images\zoom\{cat}\{image}') 
#         extrema = im.convert("L").getextrema()
#         if extrema != (0, 255):
#             print(f"Remove {image}")
#             os.remove(fr'images\zoom\{cat}\{image}')

