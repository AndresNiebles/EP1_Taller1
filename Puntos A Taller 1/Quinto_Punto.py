import math  

# Rotación eje X
def rotacion_x(angulo_radianes):
    cos_a = math.cos(angulo_radianes)
    sin_a = math.sin(angulo_radianes)

    matriz = [
        [1,      0,       0],
        [0,  cos_a,  -sin_a],
        [0,  sin_a,   cos_a]
    ]
    return matriz

# Rotación eje Y
def rotacion_y(angulo_radianes):
    cos_a = math.cos(angulo_radianes)
    sin_a = math.sin(angulo_radianes)

    matriz = [
        [ cos_a, 0, sin_a],
        [     0, 1,     0],
        [-sin_a, 0, cos_a]
    ]
    return matriz

# Rotación alrededor del eje Z
def rotacion_z(angulo_radianes):
    cos_a = math.cos(angulo_radianes)
    sin_a = math.sin(angulo_radianes)

    matriz = [
        [cos_a, -sin_a, 0],
        [sin_a,  cos_a, 0],
        [    0,      0, 1]
    ]
    return matriz



angulo = 45                          # Ángulo en grados
angulo_radianes = math.radians(45)   # Ángulo en radianes

print(f"Rotación en X ({angulo}°):")
for fila in rotacion_x(angulo_radianes):
    print(fila)

print(f"\nRotación en Y ({angulo}°):")
for fila in rotacion_y(angulo_radianes):
    print(fila)

print(f"\nRotación en Z ({angulo}°):")
for fila in rotacion_z(angulo_radianes):
    print(fila)
