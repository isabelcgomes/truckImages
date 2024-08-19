import os
import random
import matplotlib.pyplot
from PIL import Image

import image_generation
import zoom_images
import image_generation_with_a_background
import remove_all_black_or_white

categories = [str(cat[0:-4]) for cat in os.listdir("CAD_Files\stl")]
background_images = [str(bg) for bg in os.listdir("background_images")]

for cat in categories:
    try:
        os.makedirs(fr'overimages\{cat}')
        os.makedirs(fr'overimages\zoom\{cat}')
        os.makedirs(fr'overimages\bg\{cat}')
    except:
        next

for cat in categories:
    if len(os.listdir(fr"images\{cat}")) < 2024:
        angles = []
        diff = (2024 - len(os.listdir(fr"images\{cat}")))//3
        x = 0
        while x < diff:
            angles.append((random.randint(-180, 180), random.randint(-180, 180), random.randint(-180, 180)))
            x+=1
        for doubleangle in angles:
            image_generation.plot_stl(fr'CAD_Files\stl\{cat}.stl', fr"{cat}", "overimages", doubleangle[0], doubleangle[1], doubleangle[2])
        for file in os.listdir(fr"overimages\{cat}"):
            i = 0
            while i < 2:
                zoom_images.generate_random_zoom_image(fr"overimages", cat, file, i)
                i += 1
        for image in os.listdir(fr'overimages\zoom\{cat}'):
            remove_all_black_or_white.remove_images("overimages\zoom", cat, image)
        for file in os.listdir(fr'overimages\zoom\{cat}'):
            os.rename(fr"overimages\zoom\{cat}\{file}", fr"overimages\{cat}\{file}")
        for image in os.listdir(fr'overimages\{cat}'):
            num = random.randint(0, len(background_images)-1) 
            image_generation_with_a_background.replace_background(fr'overimages\{cat}\{image}', fr"background_images\{background_images[num]}", fr'overimages\bg\{cat}\background_{image}')
    else:
        next

        















    