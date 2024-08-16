import os

categories = [str(cat[0:-4]) for cat in os.listdir("CAD_Files\stl")]

for cat in categories:
    for file in os.listdir(fr"images\zoom\{cat}"):
        os.rename(fr"images\zoom\{cat}\{file}", fr"images\{cat}\{file}")