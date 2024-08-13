import scipy as sp
import matplotlib.pyplot as plt
import numpy as np
import os
import cv2
import matplotlib.patches as patches
import random
   
categories = []
for cat in os.listdir("CAD_Files\stl"):
      categories.append(str(cat[0:-4]))

# for cat in categories:
#     os.makedirs(fr'images\zoom\{cat}')

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
    plt.savefig(fr'images\zoom\{cat}\{data[0:-4]}_zoom{index}.png', bbox_inches='tight', pad_inches=0)
    plt.close('all')


for cat in categories:
    for file in os.listdir(fr"images\{cat}"):
        i = 0
        while i < 5:
            generate_random_zoom_image(fr"images", cat, file, i)
            print(fr'imagens para {file} geradas com sucesso')
            i += 1
