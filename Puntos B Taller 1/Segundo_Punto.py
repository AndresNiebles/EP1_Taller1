import random  # librería para generar números aleatorios

# Solicitud de la cantidad de números a generar
cantidad = int(input("¿Cuántos números aleatorios desea generar? "))

# Solicitud del rango
minimo = int(input("Ingrese el valor mínimo del rango: "))
maximo = int(input("Ingrese el valor máximo del rango: "))

# Generar números aleatorios
print("\nNumeros aleatorios generados:")
for i in range(cantidad):
    numero = random.randint(minimo, maximo)  # Genera un número entero aleatorio en el rango
    print(f"Numero {i+1}: {numero}")
