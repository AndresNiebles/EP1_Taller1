import math  # Librería sqrt, atan2, acos

# Coordenadas rectangulares 

x = 4.5
y = 5.5
z = 6.5

# Conversión a coordenadas cilíndricas

r = math.sqrt(x**2 + y**2)    # r = √(x² + y²)
theta = math.atan2(y, x)  # atan2(y, x) en radianes

# Conversión a coordenadas esféricas 

rho = math.sqrt(x**2 + y**2 + z**2) # √(x² + y² + z²)
phi = math.acos(z / rho) if rho != 0 else 0  # arccos(z / ρ) angulo polar // Evita división por cero

# Resultados

print("\nCoordenadas Rectangulares (x, y, z):")
print(f"x = {x}, y = {y}, z = {z}")

print("\nCoordenadas Cilíndricas (r, θ, z):")
print(f"r = {r:.3f}, θ = {theta:.3f} rad, z = {z}")

print("\nCoordenadas Esféricas (ρ, θ, φ):")
print(f"ρ = {rho:.3f}, θ = {theta:.3f} rad, φ = {phi:.3f} rad")
