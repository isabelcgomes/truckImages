import matplotlib.pyplot as plt
import matplotlib.patches as patches
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits import mplot3d

from  PIL import Image 

import numpy as np
from stl import mesh
import random
import os
import scipy as sp
import cv2
   

def plot_stl(file_path, output_path_prefix, angleelev, angleazim, angleroll):
    # Carregar o arquivo STL
    your_mesh = mesh.Mesh.from_file(file_path)

    # Criar uma figura para cada vista (frontal, superior, lateral)


    # Vista frontal
    fig = plt.figure()
    ax = fig.add_subplot(131, projection='3d')
    ax.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors, facecolors='w'))
    scale = your_mesh.points.flatten()
    ax.auto_scale_xyz(scale, scale, scale)
    ax.view_init(elev=angleelev, azim=angleazim, roll=angleroll)
    ax.set_facecolor('black')
    plt.axis('off')
    plt.savefig(fr'images\{output_path_prefix}\{output_path_prefix}_{angleelev}_{angleazim}_{angleroll}.png', bbox_inches='tight', pad_inches=0)
    plt.close('all')



categories = [str(cat[0:-4]) for cat in os.listdir("CAD_Files\stl")]

angles = [(0, 0, 0), (90, 90, 0), (0, 90, 0), (90, 0, 0), (45, 0, 0), (0, 45, 0), (45, 90, 0), (90, 45, 0), (45, 45, 0)]

x = 0
while x < 200:
    angles.append((random.randint(-180, 180), random.randint(-180, 180), random.randint(-180, 180)))
    x+=1


for cat in categories:
    try:
        os.makedirs(fr'images\{cat}')
    except:
        pass

for cat in os.listdir(fr'images'):
    for doubleangle in angles:
        plot_stl(fr'CAD_Files\stl\{cat}.stl', fr"{cat}", doubleangle[0], doubleangle[1], doubleangle[2])
