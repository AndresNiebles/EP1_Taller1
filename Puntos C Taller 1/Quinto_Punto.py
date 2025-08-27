import matplotlib.pyplot as plt

# Crear la figura
plt.figure(figsize=(10, 6))

# Función para dibujar una letra mediante líneas
def dibujar_letra(coords, desplazamiento_x=0):
    for linea in coords:
        x_vals = [p[0] + desplazamiento_x for p in linea]
        y_vals = [p[1] for p in linea]
        plt.plot(x_vals, y_vals, 'k', linewidth=2)

# Definir coordenadas para algunas letras (ejemplo simplificado)
# Cada letra está compuesta por líneas definidas por pares de puntos [(x1,y1),(x2,y2)]
letras = {
    'S': [[(0, 2), (1, 2)], [(0, 2), (0, 1)], [(0, 1), (1, 1)], [(1, 1), (1, 0)], [(1, 0), (0, 0)]],
    'A': [[(0, 0), (0.5, 2)], [(1, 0), (0.5, 2)], [(0.25, 1), (0.75, 1)]],
    'N': [[(0, 0), (0, 2)], [(0, 2), (1, 0)], [(1, 0), (1, 2)]],
    'T': [[(0, 2), (1, 2)], [(0.5, 2), (0.5, 0)]],
    'I': [[(0.5, 2), (0.5, 0)], [(0, 2), (1, 2)], [(0, 0), (1, 0)]],
    'G': [[(1, 2), (0, 2)], [(0, 2), (0, 0)], [(0, 0), (1, 0)], [(1, 0), (1, 1)], [(0.5, 1), (1, 1)]],
    'O': [[(0, 0), (0, 2)], [(0, 2), (1, 2)], [(1, 2), (1, 0)], [(1, 0), (0, 0)]],
    'E': [[(1, 2), (0, 2)], [(0, 2), (0, 0)], [(0, 0), (1, 0)], [(0, 1), (0.8, 1)]],
    'S': [[(0, 2), (1, 2)], [(0, 2), (0, 1)], [(0, 1), (1, 1)], [(1, 1), (1, 0)], [(1, 0), (0, 0)]],
    'B': [[(0, 0), (0, 2)], [(0, 2), (0.8, 1.8)], [(0.8, 1.8), (0, 1)], [(0, 1), (0.8, 0.2)], [(0.8, 0.2), (0, 0)]],
    'F': [[(0, 0), (0, 2)], [(0, 2), (1, 2)], [(0, 1), (0.8, 1)]],
    'D': [[(0, 0), (0, 2)], [(0, 2), (0.8, 1.8)], [(0.8, 1.8), (0.8, 0.2)], [(0.8, 0.2), (0, 0)]],
    'R': [[(0, 0), (0, 2)], [(0, 2), (0.8, 1.8)], [(0.8, 1.8), (0, 1)], [(0, 1), (0.8, 0)]]
}

# Nombres a dibujar     
nombres = ["SANTIAGO", "ESTEBAN", "FABIAN", "ANDRES"]

# Posición inicial
pos_x = 0
espacio_letra = 1.5  # Separación horizontal entre letras
espacio_nombre = 10  # Separación horizontal entre nombres

# Dibujar cada nombre
for nombre in nombres:
    for letra in nombre:
        if letra in letras:
            dibujar_letra(letras[letra], desplazamiento_x=pos_x)
        pos_x += espacio_letra
    pos_x += espacio_nombre  # Espacio extra entre nombres

# Configuración del gráfico
plt.axis('equal')
plt.axis('off')
plt.title("Nombres dibujados con líneas", fontsize=14)
plt.show()
