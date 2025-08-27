import numpy as np                         # la librería NumPy,  manejo de vectores y matrices.

#Variables
a1, a2, a3 = 8, 7, -11
b1, b2, b3 = 5, -6, 15

# Vectores
VectorA = np.array([a1, a2, a3])           #crea un arreglo apartir de una lista
VectorB = np.array([b1, b2, b3])  

# Operaciones
suma = VectorA + VectorB  
resta = VectorA - VectorB 
producto_punto = np.dot(VectorA, VectorB)   # a1*b1 + a2*b2 + a3*b3 
producto_cruz = np.cross(VectorA, VectorB)  # a2b3 - a3b2 ; a3b1 - a1b3 ; a1b2 - a2b1
division = np.divide(VectorA, VectorB)  

# Resultados
print("Vector A:", VectorA)  
print("Vector B:", VectorB)  
print("\nSuma:", suma)  
print("Resta:", resta)  
print("Producto Punto:", producto_punto)  
print("Producto Cruz:", producto_cruz)  
print("División:", division)  

