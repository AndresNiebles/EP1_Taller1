import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# -------------------------------
# Entrada de datos
# -------------------------------
x = float(input("Ingrese la coordenada X del vector: "))
y = float(input("Ingrese la coordenada Y del vector: "))
z = float(input("Ingrese la coordenada Z del vector: "))

# -------------------------------
# Crear figura 3D
# -------------------------------
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Dibujar los ejes coordenados
max_range = max(abs(x), abs(y), abs(z), 1)  # Ajuste dinámico de escala
ax.quiver(0, 0, 0, max_range, 0, 0, color='r', arrow_length_ratio=0.05)
ax.quiver(0, 0, 0, 0, max_range, 0, color='g', arrow_length_ratio=0.05)
ax.quiver(0, 0, 0, 0, 0, max_range, color='b', arrow_length_ratio=0.05)

# Dibujar el vector ingresado por el usuario
ax.quiver(0, 0, 0, x, y, z, color='purple', linewidth=2, arrow_length_ratio=0.1)

# Etiquetas de los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Límites de los ejes
ax.set_xlim([-max_range, max_range])
ax.set_ylim([-max_range, max_range])
ax.set_zlim([-max_range, max_range])

# Título
ax.set_title(f"Vector: ({x}, {y}, {z})")

# Mostrar gráfica
plt.show()
