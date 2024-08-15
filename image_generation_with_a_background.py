from PIL import Image
import numpy as np
import os
import random

def replace_background(foreground_path, background_path, output_path, threshold=200):
    # Carregar imagens
    foreground = Image.open(foreground_path).convert("RGBA")
    background = Image.open(background_path).convert("RGBA")

    # Redimensionar o fundo para o tamanho da imagem de primeiro plano
    background = background.resize(foreground.size)

    # Converter para arrays numpy
    foreground_array = np.array(foreground)
    background_array = np.array(background)

    # Criar uma máscara para o fundo
    r, g, b, a = foreground_array[:, :, 0], foreground_array[:, :, 1], foreground_array[:, :, 2], foreground_array[:, :, 3]
    mask = (r > threshold) & (g > threshold) & (b > threshold)  # Ajuste o valor de threshold conforme necessário

    # Substituir o fundo usando a máscara
    result_array = background_array.copy()
    result_array[mask] = foreground_array[mask]

    # Converter de volta para imagem
    result_image = Image.fromarray(result_array, "RGBA")

    # Salvar a imagem resultante
    result_image.save(output_path)

# Exemplo de uso

categories = [str(cat[0:-4]) for cat in os.listdir("CAD_Files\stl")]

background_images = [str(bg) for bg in os.listdir("background_images")]


for cat in categories:
    for image in os.listdir(fr'images\{cat}'):
        num = random.randint(0, len(background_images)-1) 
        replace_background(fr'images\{cat}\{image}', fr"background_images\{background_images[num]}", fr'images\{cat}\background_{image}')
        
