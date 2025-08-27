# Cálculo de la resistencia de una RTD PT100 según la temperatura

# Constantes del sensor PT100
R0 = 100           # Resistencia en 0 °C 
A = 3.9083e-3
B = -5.775e-7

# Temperatura 
temp = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 500, 700, 900] # °C

print("Temperatura (°C) | Resistencia (Ω)")
print("------------------------------------")

for t in temp:
    Rt = R0 * (1 + A*t + B*(t**2))    # Fórmula Callendar–Van Dusen
                                             
    print(f"{t:>10}       | {Rt:.4f}")
