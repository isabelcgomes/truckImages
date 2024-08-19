import os

categories = [str(cat[0:-4]) for cat in os.listdir("CAD_Files\stl")]

for cat in categories:
    try:
        for file in os.listdir(fr'overimages\bg\{cat}'):
                os.rename(fr"overimages\bg\{cat}\{file}", fr"overimages\{cat}\{file}")
        for file in os.listdir(fr'overimages\{cat}'):
            os.rename(fr"overimages\{cat}\{file}", fr"images\{cat}\{file}")
    except:
         next