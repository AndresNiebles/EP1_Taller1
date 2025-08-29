# Cálculo de la resistencia de una RTD PT100 según la temperatura

# Constantes del sensor PT100
R0 = 100        # Resistencia en 0 °C 
A = 3.9083e-3
B = -5.775e-7
C = -4.183e-12  # Solo se usa para temperaturas < 0 °C
# Temperatura 
temp = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 500, 700, 900] # °C
temp1 = [0, -10, -20, -30, -40, -50, -60, -70, -80, -90, -100, -500, -700, -900] # °C

print("Temperatura (°C) | Resistencia (Ω)")
print("------------------------------------")

for t in temp:
    Rt = R0 * (1 + A*t + B*(t**2))    # Fórmula Callendar–Van Dusen
                                             
    print(f"{t:>10}       | {Rt:.4f}")

for t1 in temp1:
    Rt0 = R0 * (1 + A*t1 + B*(t1**2)+ C*(t1-100)*(t1**3))    # Fórmula Callendar–Van temperaturas < 0 °C
                                             
    print(f"{t1:>10}       | {Rt0:.4f}")