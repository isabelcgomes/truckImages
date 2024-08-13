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
   
categories = [str(cat[0:-4]) for cat in os.listdir("CAD_Files\stl")]

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

def generate_random_zoom_image(path, cat, data, index):
    img_array = cv2.imread(os.path.join(path,cat,data))
    Z = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)

    # Configura o tamanho da imagem
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Plota a imagem
    c = ax.imshow(Z, cmap='viridis', interpolation='none')

    # Gera uma área de zoom aleatória
    height, width, chanels = Z.shape
    zoom_x = random.uniform(0.1, 0.5) * width
    zoom_y = random.uniform(0.1, 0.5) * height
    x_center = random.uniform(0.25 * width, 0.75 * width)
    y_center = random.uniform(0.25 * height, 0.75 * height)

    # Define os limites da área de zoom
    xmin = max(0, x_center - zoom_x / 2)
    xmax = min(width, x_center + zoom_x / 2)
    ymin = max(0, y_center - zoom_y / 2)
    ymax = min(height, y_center + zoom_y / 2)

    # Adiciona um retângulo para visualizar a área de zoom
    rect = patches.Rectangle((xmin, ymin), xmax - xmin, ymax - ymin, linewidth=1, edgecolor='red', facecolor='none')
    ax.add_patch(rect)
    
    # Define os limites do zoom
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymax, ymin)  # Nota: o eixo y está invertido para que o zoom apareça corretamente

    # Mostra a imagem
    plt.axis('off')
    plt.savefig(fr'images\{cat}\{data[0:-4]}_zoom{index}.png', bbox_inches='tight', pad_inches=0)
    plt.close('all')

angles = [(0, 0, 0), (90, 90, 0), (0, 90, 0), (90, 0, 0), (45, 0, 0), (0, 45, 0), (45, 90, 0), (90, 45, 0), (45, 45, 0)]
angles=[]

x = 0 

for cat in os.listdir(fr'images'):
    while len(os.listdir(os.path.join(fr'images', cat))) < 1000:

        while x < 5:
            angles.append((random.randint(-180, 180), random.randint(-180, 180), random.randint(-180, 180)))
            x += 1

        for doubleangle in angles:
            plot_stl(fr'CAD_Files\stl\{cat}.stl', fr"{cat}", doubleangle[0], doubleangle[1], doubleangle[2])
            print(fr'imagens para {cat} geradas com sucesso')

        for file in os.listdir(fr"images\{cat}"):
            i = 0
            while i < 100:
                generate_random_zoom_image(fr"images", cat, file, i)
                print(fr'imagens para {file} geradas com sucesso')
                i += 1

        for image in os.listdir(fr'images\{cat}'):
            im = Image.open(fr'images\{cat}\{image}') 
            extrema = im.convert("L").getextrema()
            if extrema == (0, 76) or extrema == (76,255):
                print(f"entire {image}")
                os.remove(fr'images\{cat}\{image}')

for cat in categories:
    if len(os.listdir(os.path.join(fr'images', cat))) > 1000:
        not_removes = list(os.listdir(os.path.join(fr'images', cat)))
        removes = not_removes[:10:]

        for rem in not_removes:
            if rem not in removes:
                os.remove(os.path.join(fr'images', cat, rem))
