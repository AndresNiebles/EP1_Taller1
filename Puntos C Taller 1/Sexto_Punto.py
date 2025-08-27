import cv2
import numpy as np
import matplotlib.pyplot as plt

# Función para obtener contornos y coordenadas de un logo
def obtener_contornos(ruta_imagen):
    # Leer imagen
    imagen = cv2.imread(ruta_imagen, cv2.IMREAD_GRAYSCALE)
    
    # Aplicar umbral binario
    _, binaria = cv2.threshold(imagen, 127, 255, cv2.THRESH_BINARY_INV)
    
    # Encontrar contornos
    contornos, _ = cv2.findContours(binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    # Tomamos el contorno más grande (el principal del logo)
    contorno_principal = max(contornos, key=cv2.contourArea)
    
    # Extraer coordenadas X e Y
    coordenadas = contorno_principal.reshape(-1, 2)
    X, Y = coordenadas[:, 0], coordenadas[:, 1]
    
    return X, Y

# Rutas de los logos (asegúrate de tener las imágenes en el mismo directorio)
logo1 = 'chevrolet.png'
logo2 = 'hyundai.png'

# Obtener coordenadas
X1, Y1 = obtener_contornos(logo1)
X2, Y2 = obtener_contornos(logo2)

# Graficar contornos
plt.figure(figsize=(10, 6))
plt.plot(X1, -Y1, label='Chevrolet', color='gold')
plt.plot(X2, -Y2, label='Hyundai', color='blue')
plt.title('Contornos de Logos')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.axis('equal')
plt.show()
