import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from stl import mesh  # Você precisa instalar essa biblioteca usando pip install numpy-stl

# Função para carregar o arquivo STL e extrair os vértices e faces
def load_stl(filename):
    your_mesh = mesh.Mesh.from_file(filename)
    return your_mesh.vectors

# Função para criar a imagem PNG
def create_png_from_stl(stl_filename, output_png):
    # Carregar o arquivo STL
    vertices = load_stl(stl_filename)

    # Preparar a figura 3D
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='2d')

    # Plotar a malha STL
    mesh = Poly3DCollection(vertices)
    ax.add_collection3d(mesh)

    # Definir os limites do gráfico para garantir que a malha seja totalmente visível
    max_dim = np.max(vertices.flatten())
    min_dim = np.min(vertices.flatten())
    ax.set_xlim(min_dim, max_dim)
    ax.set_ylim(min_dim, max_dim)
    ax.set_zlim(min_dim, max_dim)

    # Salvar a imagem como PNG
    plt.savefig(output_png)
    plt.close(fig)

# Exemplo de uso
if __name__ == "__main__":
    stl_file = "exemplo.stl"  # Substitua pelo caminho do seu arquivo STL
    output_png = "saida.png"  # Nome do arquivo de saída PNG

    create_png_from_stl(stl_file, output_png)
    print(f"Imagem PNG gerada: {output_png}")
