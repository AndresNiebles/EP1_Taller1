import numpy as np

# Variables
a1, a2, a3 , a4, a5, a6, a7, a8, a9 = 1, 2, 3, 4, 5, 6, 7, 8, 9
b1, b2, b3 , b4, b5, b6, b7, b8, b9 = 9, 8, 7, 6, 5, 4, 3, 2, 1

# Matrices
matrizA = np.array([[a1, a2, a3],
                     [a4, a5, a6],
                     [a7, a8, a9]])

matrizB = np.array([[b1, b2, b3],
                     [b4, b5, b6],
                     [b7, b8, b9]])

# Operaciones
suma = matrizA + matrizB
resta = matrizA - matrizB
multiplicacion_elemento = matrizA * matrizB
division = matrizA / matrizB
producto_punto = np.dot(matrizA, matrizB)   #a1b1 + a2b2 + a3b3 ; a4b4 + a5b5 + a6b6 ; a7b7 + a8b8 + a9b9
producto_cruz = np.cross(matrizA, matrizB) # a2b3 - a3b2 ; a3b1 - a1b3 ; a1b2 - a2b1

# Resultados 
print("Matriz A:\n", matrizA)
print("Matriz B:\n", matrizB)
print("\nSuma:\n", suma)
print("\nResta:\n", resta)
print("\nMultiplicación:\n", multiplicacion_elemento)
print("\nDivisión:\n", division)
print("\nProducto Punto:\n", producto_punto)
print("\nProducto Cruz:\n", producto_cruz)
