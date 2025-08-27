import math  # Para usar pi y potencias

# Valores inicializados
presion = 6e5  # Presión en Pa (6 bar = 600000 Pa)
diametro_cilindro = 0.05  # 50 mm en metros
diametro_vastago = 0.02   # 20 mm en metros

# Cálculo de áreas
area_piston = math.pi * (diametro_cilindro / 2) ** 2
area_vastago = math.pi * (diametro_vastago / 2) ** 2

# Fuerzas
fuerza_avance = presion * area_piston
fuerza_retroceso = presion * (area_piston - area_vastago)

# Mostrar resultados
print("=== Cálculo de fuerzas del cilindro neumático ===")
print(f"Presión: {presion} Pa")
print(f"Diámetro del cilindro: {diametro_cilindro*1000:.0f} mm")
print(f"Diámetro del vástago: {diametro_vastago*1000:.0f} mm")
print(f"Área del pistón: {area_piston:.6f} m²")
print(f"Área del vástago: {area_vastago:.6f} m²")
print(f"\nFuerza de avance: {fuerza_avance:.2f} N")
print(f"Fuerza de retroceso: {fuerza_retroceso:.2f} N")
