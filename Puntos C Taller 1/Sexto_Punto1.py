import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Rutas de las imágenes
ruta_logo1 = r"C:\Users\santi\Documents\ClaseEP1\SantiagoSuazaF\Puntos C Taller 1\chevrolet1.png"
ruta_logo2 = r"C:\Users\santi\Documents\ClaseEP1\SantiagoSuazaF\Puntos C Taller 1\Mazda.png"


# Función para procesar cada logo
def procesar_logo(ruta, nombre_logo):
    # Leer imagen
    img = cv2.imread(ruta)
    if img is None:
        print(f"Error: No se pudo cargar la imagen {ruta}")
        return None

    # Convertir a escala de grises
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Binarización (umbral adaptativo)
    _, binaria = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

    # Encontrar contornos
    contornos, _ = cv2.findContours(binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # Tomamos el contorno más grande 
    contorno = max(contornos, key=cv2.contourArea)

    # Extrae coordenadas
    coordenadas = contorno.reshape(-1, 2)  # Nx2 (X,Y)

    # Crear tabla
    df = pd.DataFrame(coordenadas, columns=["X", "Y"])
    print(f"\nCoordenadas del contorno para el logo {nombre_logo}:")
    #print(df.to_string(index=False))

    # Dibujar contorno en la imagen
    img_contorno = img.copy()
    cv2.drawContours(img_contorno, [contorno], -1, (0, 255, 0), 2)

    return img_contorno

# Procesar ambos logos
logo1 = procesar_logo(ruta_logo1, "Chevrolet")
logo2 = procesar_logo(ruta_logo2, "Mazda")


# Mostrar imágenes con contornos
if logo1 is not None and logo2 is not None:
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(logo1, cv2.COLOR_BGR2RGB))
    plt.title("Logo Chevrolet")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(logo2, cv2.COLOR_BGR2RGB))
    plt.title("Logo Mazda")
    plt.axis("off")

    plt.show()
