import os
import pandas as pd

categories = [cat for cat in os.listdir('images')]

myDataFrame = {}

for cat in categories:
    myDataFrame[cat] = len(os.listdir(fr'images\{cat}'))


print(myDataFrame)
